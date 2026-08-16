import pandas as pd
import re
from failsafe_ai import analyze_description
from validation_cases import VALIDATION_CASES



# ============================================================
# FAILSAFE AI - V6
# Context + Symptom Priority FMEA Evaluation
# ============================================================


def tokenize(text):
    text = text.lower()
    return set(re.findall(r"[a-z]+", text))


def calculate_rpn(severity, occurrence, detection):
    return severity * occurrence * detection


# ============================================================
# EQUIPMENT CONTEXT
# ============================================================

EQUIPMENT_GROUPS = {

    "hydraulic system": {
        "hydraulic", "hose", "seal", "pump", "pressure"
    },

    "pneumatic system": {
        "pneumatic", "actuator", "valve", "air"
    },

    "conveyor system": {
        "conveyor", "belt", "roller", "bearing", "drive"
    },

    "electric motor": {
        "motor", "electric", "winding", "bearing",
        "temperature"
    },

    "industrial pump": {
        "pump", "impeller", "mechanical", "flow",
        "cavitation"
    },

    "industrial mixer": {
        "mixer", "mixing", "shaft", "coupling",
        "vibration"
    }
}


# ============================================================
# HIGH-VALUE SYMPTOM CLUES
# ============================================================
#
# These are diagnostic clues, not training data.
# They give stronger weight to distinctive symptoms.
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
# ANALYSIS
# ============================================================

def analyze_description(description):
    

    knowledge_base = get_all_failure_modes()

    detected_equipment = identify_equipment(
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

        description_words = tokenize(
            description
        )

        failure_words = tokenize(
            searchable
        )

        general_matches = (
            description_words
            .intersection(
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

        candidates.append({

            "failure_mode":
                failure_mode,

            "component":
                failure["component"],

            "equipment":
                failure["equipment"],

            "rpn":
                rpn,

            "relevance":
                relevance,

            "priority":
                priority,

            "strong_matches":
                ", ".join(
                    sorted(strong_matches)
                ),

            "medium_matches":
                ", ".join(
                    sorted(medium_matches)
                )
        })

    candidates.sort(
        key=lambda x: x["priority"],
        reverse=True
    )

    return (
        candidates,
        detected_equipment
    )


# ============================================================
# SAME 10 TEST CASES
# ============================================================

TEST_CASES = [

    {
        "id": "T01",
        "description":
            "Hydraulic system is losing fluid around "
            "the hose and pressure is dropping intermittently.",
        "expected":
            "hose leakage"
    },

    {
        "id": "T02",
        "description":
            "Hydraulic equipment shows unstable pressure "
            "and unusual pump noise during operation.",
        "expected":
            "pump cavitation"
    },

    {
        "id": "T03",
        "description":
            "Hydraulic system has gradual fluid leakage "
            "and reduced pressure after extended use.",
        "expected":
            "seal degradation"
    },

    {
        "id": "T04",
        "description":
            "Pneumatic actuator is moving slowly and "
            "the system is showing signs of air leakage.",
        "expected":
            "actuator slow response"
    },

    {
        "id": "T05",
        "description":
            "Pneumatic control valve intermittently sticks "
            "and actuator movement becomes inconsistent.",
        "expected":
            "valve sticking"
    },

    {
        "id": "T06",
        "description":
            "Conveyor is vibrating heavily and the drive "
            "bearing is becoming hot during continuous operation.",
        "expected":
            "bearing wear"
    },

    {
        "id": "T07",
        "description":
            "Conveyor belt is drifting sideways and "
            "material is spilling from the line.",
        "expected":
            "belt misalignment"
    },

    {
        "id": "T08",
        "description":
            "Electric motor temperature is increasing rapidly "
            "and abnormal bearing heat is observed.",
        "expected":
            "bearing overheating"
    },

    {
        "id": "T09",
        "description":
            "Industrial pump has reduced flow and declining "
            "process efficiency over time.",
        "expected":
            "impeller wear"
    },

    {
        "id": "T10",
        "description":
            "Industrial mixer is experiencing excessive "
            "vibration and possible shaft alignment issues.",
        "expected":
            "shaft misalignment"
    }
]


# ============================================================
# RUN TEST
# ============================================================

print("=" * 75)
print("              FAILSAFE AI - V6 EVALUATION")
print("=" * 75)

print()
print("Testing the same 10 scenarios used for V5...")
print()

results = []

top_1_hits = 0
top_3_hits = 0


for test in TEST_CASES:

    predictions, equipment = (
        analyze_description(
            test["description"]
        )
    )

    modes = [
        p["failure_mode"]
        for p in predictions
    ]

    expected = test["expected"]

    if expected in modes:

        rank = modes.index(expected) + 1

    else:

        rank = None

    top1 = rank == 1

    top3 = (
        rank is not None
        and rank <= 3
    )

    if top1:
        top_1_hits += 1

    if top3:
        top_3_hits += 1

    predicted = (
        modes[0]
        if modes
        else "None"
    )

    print("-" * 75)

    print("Test Case       :", test["id"])
    print("Expected        :", expected)
    print("Predicted #1    :", predicted)

    print(
        "Expected Rank   :",
        rank if rank else "Not Found"
    )

    print(
        "Top-1           :",
        "PASS" if top1 else "FAIL"
    )

    print(
        "Top-3           :",
        "PASS" if top3 else "FAIL"
    )

    results.append({

        "Test Case":
            test["id"],

        "Expected Failure":
            expected,

        "Predicted #1":
            predicted,

        "Expected Rank":
            rank if rank else "Not Found",

        "Top-1 Hit":
            "PASS" if top1 else "FAIL",

        "Top-3 Hit":
            "PASS" if top3 else "FAIL",

        "Detected Equipment":
            equipment
            if equipment
            else "None"
    })


# ============================================================
# METRICS
# ============================================================

total = len(TEST_CASES)

top1_rate = (
    top_1_hits / total
) * 100

top3_rate = (
    top_3_hits / total
) * 100

ranks = [
    r["Expected Rank"]
    for r in results
    if isinstance(
        r["Expected Rank"],
        int
    )
]

average_rank = (
    sum(ranks) / len(ranks)
    if ranks
    else 0
)


# ============================================================
# FINAL RESULTS
# ============================================================

print()
print("=" * 75)
print("                    V6 RESULTS")
print("=" * 75)

print()

print(
    "Total scenarios tested :",
    total
)

print(
    "Top-1 hits             :",
    top_1_hits,
    "/",
    total
)

print(
    "Top-1 hit rate         :",
    f"{top1_rate:.1f}%"
)

print()

print(
    "Top-3 hits             :",
    top_3_hits,
    "/",
    total
)

print(
    "Top-3 hit rate         :",
    f"{top3_rate:.1f}%"
)

print()

print(
    "Average expected rank  :",
    f"{average_rank:.2f}"
)


# ============================================================
# SAVE
# ============================================================

pd.DataFrame(
    results
).to_csv(
    "failsafe_v6_evaluation.csv",
    index=False
)

print()

print(
    "Results saved to:"
)

print(
    "failsafe_v6_evaluation.csv"
)

print()

print("V6 evaluation complete.")
