# ============================================================
# FAILSAFE AI - SYNTHETIC FMEA KNOWLEDGE BASE
# ============================================================
#
# IMPORTANT:
# This dataset is synthetic and created for demonstration.
# It does NOT contain proprietary or company-confidential data.
#
# Each entry represents a generic industrial failure pattern.
# ============================================================


FMEA_KNOWLEDGE_BASE = [

    # ---------------- HYDRAULIC SYSTEM ----------------

    {
        "equipment": "hydraulic system",
        "component": "hydraulic seal",
        "failure_mode": "seal degradation",
        "causes": [
            "wear",
            "temperature exposure",
            "material degradation"
        ],
        "effects": [
            "fluid leakage",
            "pressure loss",
            "equipment downtime"
        ],
        "severity": 8,
        "occurrence": 5,
        "detection": 4,
        "actions": [
            "Inspect seal condition",
            "Monitor leakage",
            "Establish preventive replacement intervals"
        ]
    },

    {
        "equipment": "hydraulic system",
        "component": "hydraulic pump",
        "failure_mode": "pump cavitation",
        "causes": [
            "inadequate inlet pressure",
            "restricted suction line",
            "incorrect operating conditions"
        ],
        "effects": [
            "pump damage",
            "reduced flow",
            "system pressure instability"
        ],
        "severity": 9,
        "occurrence": 4,
        "detection": 5,
        "actions": [
            "Inspect suction line",
            "Monitor inlet pressure",
            "Check operating conditions"
        ]
    },

    {
        "equipment": "hydraulic system",
        "component": "hydraulic hose",
        "failure_mode": "hose leakage",
        "causes": [
            "abrasion",
            "aging",
            "excessive pressure"
        ],
        "effects": [
            "fluid loss",
            "pressure reduction",
            "safety risk"
        ],
        "severity": 9,
        "occurrence": 5,
        "detection": 4,
        "actions": [
            "Inspect hose condition",
            "Replace damaged hoses",
            "Monitor pressure"
        ]
    },


    # ---------------- PNEUMATIC SYSTEM ----------------

    {
        "equipment": "pneumatic system",
        "component": "pneumatic actuator",
        "failure_mode": "actuator slow response",
        "causes": [
            "air leakage",
            "low air pressure",
            "contamination"
        ],
        "effects": [
            "increased cycle time",
            "production delay",
            "inconsistent operation"
        ],
        "severity": 6,
        "occurrence": 6,
        "detection": 4,
        "actions": [
            "Inspect air lines",
            "Check pressure levels",
            "Inspect actuator seals"
        ]
    },

    {
        "equipment": "pneumatic system",
        "component": "control valve",
        "failure_mode": "valve sticking",
        "causes": [
            "contamination",
            "lubrication issues",
            "component wear"
        ],
        "effects": [
            "loss of control",
            "actuator malfunction",
            "production interruption"
        ],
        "severity": 8,
        "occurrence": 4,
        "detection": 5,
        "actions": [
            "Inspect valve condition",
            "Improve filtration",
            "Establish preventive maintenance"
        ]
    },


    # ---------------- CONVEYOR ----------------

    {
        "equipment": "conveyor system",
        "component": "drive bearing",
        "failure_mode": "bearing wear",
        "causes": [
            "inadequate lubrication",
            "overloading",
            "continuous operation"
        ],
        "effects": [
            "increased vibration",
            "conveyor stoppage",
            "material flow disruption"
        ],
        "severity": 8,
        "occurrence": 7,
        "detection": 4,
        "actions": [
            "Monitor vibration",
            "Improve lubrication schedule",
            "Inspect bearing condition"
        ]
    },

    {
        "equipment": "conveyor system",
        "component": "conveyor belt",
        "failure_mode": "belt misalignment",
        "causes": [
            "uneven loading",
            "roller misalignment",
            "belt wear"
        ],
        "effects": [
            "material spillage",
            "belt damage",
            "production interruption"
        ],
        "severity": 7,
        "occurrence": 6,
        "detection": 3,
        "actions": [
            "Inspect roller alignment",
            "Monitor belt tracking",
            "Correct uneven loading"
        ]
    },


    # ---------------- ELECTRIC MOTOR ----------------

    {
        "equipment": "electric motor",
        "component": "motor bearing",
        "failure_mode": "bearing overheating",
        "causes": [
            "lubrication degradation",
            "excessive loading",
            "misalignment"
        ],
        "effects": [
            "motor failure",
            "unplanned downtime",
            "production interruption"
        ],
        "severity": 9,
        "occurrence": 5,
        "detection": 5,
        "actions": [
            "Monitor bearing temperature",
            "Check lubrication",
            "Inspect alignment"
        ]
    },

    {
        "equipment": "electric motor",
        "component": "motor winding",
        "failure_mode": "winding insulation degradation",
        "causes": [
            "thermal stress",
            "overloading",
            "moisture exposure"
        ],
        "effects": [
            "electrical failure",
            "motor shutdown",
            "production downtime"
        ],
        "severity": 9,
        "occurrence": 4,
        "detection": 6,
        "actions": [
            "Monitor winding temperature",
            "Perform insulation testing",
            "Check motor loading"
        ]
    },


    # ---------------- INDUSTRIAL PUMP ----------------

    {
        "equipment": "industrial pump",
        "component": "pump impeller",
        "failure_mode": "impeller wear",
        "causes": [
            "abrasive fluid",
            "continuous operation",
            "corrosion"
        ],
        "effects": [
            "reduced flow",
            "lower process efficiency",
            "increased energy consumption"
        ],
        "severity": 7,
        "occurrence": 6,
        "detection": 6,
        "actions": [
            "Monitor flow rate",
            "Inspect impeller condition",
            "Monitor pump efficiency"
        ]
    },

    {
        "equipment": "industrial pump",
        "component": "mechanical seal",
        "failure_mode": "mechanical seal leakage",
        "causes": [
            "seal wear",
            "misalignment",
            "thermal stress"
        ],
        "effects": [
            "fluid leakage",
            "pump efficiency loss",
            "equipment downtime"
        ],
        "severity": 8,
        "occurrence": 5,
        "detection": 4,
        "actions": [
            "Inspect seal condition",
            "Check shaft alignment",
            "Monitor leakage"
        ]
    },


    # ---------------- MIXER ----------------

    {
        "equipment": "industrial mixer",
        "component": "mixing shaft",
        "failure_mode": "shaft misalignment",
        "causes": [
            "mechanical wear",
            "improper alignment",
            "excessive loading"
        ],
        "effects": [
            "increased vibration",
            "shaft damage",
            "production interruption"
        ],
        "severity": 8,
        "occurrence": 5,
        "detection": 4,
        "actions": [
            "Check shaft alignment",
            "Monitor vibration",
            "Inspect coupling"
        ]
    }
]


def get_all_failure_modes():
    """Return the complete synthetic knowledge base."""
    return FMEA_KNOWLEDGE_BASE


def search_equipment(equipment_name):
    """
    Return failure modes associated with an equipment type.
    Uses simple keyword matching.
    """

    equipment_name = equipment_name.lower().strip()

    matches = []

    for item in FMEA_KNOWLEDGE_BASE:

        if equipment_name in item["equipment"]:
            matches.append(item)

    return matches