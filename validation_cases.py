
VALIDATION_CASES = [

    # ========================================================
    # HOSE LEAKAGE
    # ========================================================

    {
        "id": "V01",
        "description":
            "Hydraulic pressure falls gradually while a small "
            "amount of fluid is visible near the flexible connection.",
        "expected":
            "hose leakage"
    },

    {
        "id": "V02",
        "description":
            "A flexible hydraulic line shows physical surface damage "
            "and the reservoir level decreases during operation.",
        "expected":
            "hose leakage"
    },

    {
        "id": "V03",
        "description":
            "The hydraulic circuit requires repeated fluid top-ups "
            "and the pressure loss becomes more noticeable at higher load.",
        "expected":
            "hose leakage"
    },


    # ========================================================
    # PUMP CAVITATION
    # ========================================================

    {
        "id": "V04",
        "description":
            "The pump produces a rattling sound and its delivery "
            "becomes unstable when operating near maximum demand.",
        "expected":
            "pump cavitation"
    },

    {
        "id": "V05",
        "description":
            "Hydraulic flow fluctuates unexpectedly and the pump "
            "develops a distinctive noisy operating condition.",
        "expected":
            "pump cavitation"
    },

    {
        "id": "V06",
        "description":
            "The pumping unit becomes noisy while discharge pressure "
            "oscillates instead of remaining steady.",
        "expected":
            "pump cavitation"
    },


    # ========================================================
    # SEAL DEGRADATION
    # ========================================================

    {
        "id": "V07",
        "description":
            "A hydraulic unit develops a progressively worsening "
            "loss of fluid containment after several months of service.",
        "expected":
            "seal degradation"
    },

    {
        "id": "V08",
        "description":
            "Fluid loss is minor initially but gradually increases "
            "as the equipment continues to age.",
        "expected":
            "seal degradation"
    },

    {
        "id": "V09",
        "description":
            "The hydraulic assembly shows progressive deterioration "
            "around the sealing interface with a corresponding loss "
            "of system pressure.",
        "expected":
            "seal degradation"
    },


    # ========================================================
    # ACTUATOR SLOW RESPONSE
    # ========================================================

    {
        "id": "V10",
        "description":
            "The pneumatic cylinder takes noticeably longer than "
            "normal to complete its stroke.",
        "expected":
            "actuator slow response"
    },

    {
        "id": "V11",
        "description":
            "Command signals are being received, but the pneumatic "
            "mechanism responds with a noticeable delay.",
        "expected":
            "actuator slow response"
    },

    {
        "id": "V12",
        "description":
            "The actuator movement has become sluggish during "
            "repeated machine cycles.",
        "expected":
            "actuator slow response"
    },


    # ========================================================
    # VALVE STICKING
    # ========================================================

    {
        "id": "V13",
        "description":
            "The pneumatic control mechanism occasionally remains "
            "in its previous position before moving to the commanded state.",
        "expected":
            "valve sticking"
    },

    {
        "id": "V14",
        "description":
            "Actuator motion becomes unpredictable because the "
            "control valve does not transition smoothly between positions.",
        "expected":
            "valve sticking"
    },

    {
        "id": "V15",
        "description":
            "The pneumatic circuit sometimes fails to respond correctly "
            "until the control element moves again.",
        "expected":
            "valve sticking"
    },


    # ========================================================
    # BEARING WEAR
    # ========================================================

    {
        "id": "V16",
        "description":
            "A conveyor drive develops increasing mechanical noise "
            "and vibration after prolonged service.",
        "expected":
            "bearing wear"
    },

    {
        "id": "V17",
        "description":
            "The rotating support assembly becomes increasingly noisy "
            "and rough during continuous conveyor operation.",
        "expected":
            "bearing wear"
    },

    {
        "id": "V18",
        "description":
            "Progressive deterioration of the rotating support is "
            "accompanied by increased vibration and frictional heat.",
        "expected":
            "bearing wear"
    },


    # ========================================================
    # BELT MISALIGNMENT
    # ========================================================

    {
        "id": "V19",
        "description":
            "Material repeatedly accumulates along one side of the "
            "conveyor instead of remaining centered.",
        "expected":
            "belt misalignment"
    },

    {
        "id": "V20",
        "description":
            "The conveyor material path gradually shifts toward "
            "one edge during operation.",
        "expected":
            "belt misalignment"
    },

    {
        "id": "V21",
        "description":
            "Product begins falling from the side of the conveyor "
            "while the belt no longer follows its intended centerline.",
        "expected":
            "belt misalignment"
    },


    # ========================================================
    # BEARING OVERHEATING
    # ========================================================

    {
        "id": "V22",
        "description":
            "The motor support area reaches an unusually high "
            "operating temperature during sustained running.",
        "expected":
            "bearing overheating"
    },

    {
        "id": "V23",
        "description":
            "Temperature around the rotating support increases "
            "rapidly even though the motor remains operational.",
        "expected":
            "bearing overheating"
    },

    {
        "id": "V24",
        "description":
            "An electric drive shows abnormal thermal buildup "
            "concentrated near its rotating support.",
        "expected":
            "bearing overheating"
    },


    # ========================================================
    # IMPELLER WEAR
    # ========================================================

    {
        "id": "V25",
        "description":
            "The industrial pump delivers progressively less fluid "
            "despite operating under the same process conditions.",
        "expected":
            "impeller wear"
    },

    {
        "id": "V26",
        "description":
            "Pump output has declined steadily and the equipment "
            "requires longer operation to achieve the same process result.",
        "expected":
            "impeller wear"
    },

    {
        "id": "V27",
        "description":
            "The pumping system has gradually lost its ability to "
            "maintain the previous throughput level.",
        "expected":
            "impeller wear"
    },


    # ========================================================
    # SHAFT MISALIGNMENT
    # ========================================================

    {
        "id": "V28",
        "description":
            "An industrial mixer develops increasing vibration "
            "during rotation, particularly at higher operating speed.",
        "expected":
            "shaft misalignment"
    },

    {
        "id": "V29",
        "description":
            "The rotating assembly produces excessive vibration "
            "after maintenance involving the drive connection.",
        "expected":
            "shaft misalignment"
    },

    {
        "id": "V30",
        "description":
            "A mixer experiences abnormal rotational movement "
            "and vibration following installation of the drive assembly.",
        "expected":
            "shaft misalignment"
    }
]