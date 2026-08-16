import re

from fmea_knowledge_base import get_all_failure_modes


# ============================================================
# FAILSAFE AI - V6
# Context + Symptom Priority FMEA Decision Support
# ============================================================


# ============================================================
# BASIC UTILITIES
# ============================================================

def tokenize(text):
    """
    Convert text into lowercase keyword tokens.
    """
    text = text.lower()
    return set(re.findall(r"[a-z]+", text))


def calculate_rpn(severity, occurrence, detection):
    """
    Calculate standard FMEA Risk Priority Number.
    """
    return severity * occurrence * detection


def risk_level(rpn):
    """
    Convert RPN into a qualitative risk level.
    """
    if rpn >= 200:
        return "CRITICAL"
    elif rpn >= 120:
        return "HIGH"
    elif rpn >= 60:
        return "MEDIUM"
    else:
        return "LOW"


# ============================================================
# EQUIPMENT CONTEXT
# ============================================================

EQUIPMENT_GROUPS = {

    "hydraulic system": {
        "hydraulic",
        "hose",
        "seal",
        "pump",
        "pressure"
    },

    "pneumatic system": {
        "pneumatic",
        "actuator",
        "valve",
        "air"
    },

    "conveyor system": {
        "conveyor",
        "belt",
        "roller",
        "bearing",
        "drive"
    },

    "electric motor": {
        "motor",
        "electric",
        "winding",
        "bearing",
        "temperature"
    },

    "industrial pump": {
        "pump",
        "impeller",
        "mechanical",
        "flow",
        "cavitation"
    },

    "industrial mixer": {
        "mixer",
        "mixing",
        "shaft",
        "coupling",
        "vibration"
    }
}


# ============================================================
# HIGH-VALUE SYMPTOM CLUES
# ============================================================

SYMPTOM_CLUES = {

    "seal degradation": {

        "strong": {
            "gradual",
            "seal",
            "degradation",
            "deterioration",
            "aging"
        },

        "medium": {
            "leakage",
            "leak",
            "pressure",
            "fluid"
        }
    },


    "hose leakage": {

        "strong": {
            "hose",
            "abrasion",
            "damaged",
            "burst",
            "crack"
        },

        "medium": {
            "leakage",
            "leak",
            "fluid",
            "pressure"
        }
    },


    "belt misalignment": {

        "strong": {
            "drifting",
            "drift",
            "sideways",
            "tracking",
            "misalignment",
            "misaligned"
        },

        "medium": {
            "belt",
            "spilling"
        }
    },


    "bearing wear": {

        "strong": {
            "bearing",
            "vibration",
            "wear"
        },

        "medium": {
            "heat",
            "hot",
            "noise"
        }
    },


    "bearing overheating": {

        "strong": {
            "bearing",
            "overheating",
            "temperature"
        },

        "medium": {
            "heat",
            "hot"
        }
    },


    "pump cavitation": {

        "strong": {
            "cavitation",
            "noise",
            "unstable"
        },

        "medium": {
            "pressure",
            "pump"
        }
    },


    "impeller wear": {

        "strong": {
            "impeller",
            "flow",
            "efficiency"
        },

        "medium": {
            "reduced",
            "output"
        }
    },


    "actuator slow response": {

        "strong": {
            "slow",
            "actuator",
            "movement"
        },

        "medium": {
            "air",
            "leakage"
        }
    },


    "valve sticking": {

        "strong": {
            "sticking",
            "sticks",
            "valve"
        },

        "medium": {
            "inconsistent",
            "movement"
        }
    },


    "shaft misalignment": {

        "strong": {
            "shaft",
            "alignment",
            "misalignment"
        },

        "medium": {
            "vibration",
            "coupling"
        }
    }
}


# ============================================================
# EQUIPMENT DETECTION
# ============================================================

def identify_equipment(description):

    words = tokenize(description)

    best_equipment = None
    best_score = 0

    for equipment, keywords in EQUIPMENT_GROUPS.items():

        score = len(
            words.intersection(keywords)
        )

        if score > best_score:

            best_score = score
            best_equipment = equipment

    return best_equipment


# ============================================================
# SYMPTOM SCORE
# ============================================================

def calculate_symptom_score(
    description,
    failure_mode
):

    words = tokenize(description)

    clues = SYMPTOM_CLUES.get(
        failure_mode,
        {}
    )

    strong = clues.get(
        "strong",
        set()
    )

    medium = clues.get(
        "medium",
        set()
    )

    strong_matches = (
        words.intersection(strong)
    )

    medium_matches = (
        words.intersection(medium)
    )

    score = (
        len(strong_matches) * 40
        + len(medium_matches) * 10
    )

    return (
        score,
        strong_matches,
        medium_matches
    )


# ============================================================
# ANALYSIS ENGINE
# ============================================================

def analyze_description(description):

    knowledge_base = get_all_failure_modes()

    detected_equipment = identify_equipment(
        description
    )

    description_words = tokenize(
        description
    )

    candidates = []

    for failure in knowledge_base:

        failure_mode = failure["failure_mode"]

        # ----------------------------------------------------
        # EQUIPMENT MATCH
        # ----------------------------------------------------

        equipment_score = 0

        if detected_equipment == failure["equipment"]:

            equipment_score = 50

        # ----------------------------------------------------
        # GENERAL WORD MATCH
        # ----------------------------------------------------

        searchable = " ".join([

            failure_mode,

            " ".join(
                failure["causes"]
            ),

            " ".join(
                failure["effects"]
            )
        ])

        failure_words = tokenize(
            searchable
        )

        general_matches = (
            description_words.intersection(
                failure_words
            )
        )

        general_score = (
            len(general_matches) * 10
        )

        # ----------------------------------------------------
        # SPECIFIC SYMPTOM SCORE
        # ----------------------------------------------------

        (
            symptom_score,
            strong_matches,
            medium_matches
        ) = calculate_symptom_score(
            description,
            failure_mode
        )

        # ----------------------------------------------------
        # TOTAL RELEVANCE
        # ----------------------------------------------------

        relevance = (
            equipment_score
            + general_score
            + symptom_score
        )

        # Ignore extremely weak candidates

        if relevance < 20:
            continue

        # ----------------------------------------------------
        # RPN
        # ----------------------------------------------------

        rpn = calculate_rpn(
            failure["severity"],
            failure["occurrence"],
            failure["detection"]
        )

        # ----------------------------------------------------
        # PRIORITY
        # ----------------------------------------------------

        priority = (
            relevance * 2
            + rpn
        )

        candidate = failure.copy()

        candidate["RPN"] = rpn

        candidate["Risk Level"] = risk_level(
            rpn
        )

        candidate["Relevance Score"] = relevance

        candidate["Priority Score"] = priority

        candidate["Equipment Match"] = (
            equipment_score
        )

        candidate["Strong Matches"] = (
            ", ".join(
                sorted(strong_matches)
            )
            if strong_matches
            else ""
        )

        candidate["Medium Matches"] = (
            ", ".join(
                sorted(medium_matches)
            )
            if medium_matches
            else ""
        )

        candidate["Matched Symptoms"] = (
            ", ".join(
                sorted(
                    strong_matches.union(
                        medium_matches
                    )
                )
            )
            if strong_matches or medium_matches
            else "None"
        )

        candidates.append(candidate)

    candidates.sort(
        key=lambda x: x["Priority Score"],
        reverse=True
    )

    return (
        candidates,
        detected_equipment
    )
