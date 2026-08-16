from failsafe_ai import analyze_description
from validation_cases import VALIDATION_CASES

import pandas as pd


# ============================================================
# FAILSAFE AI - V6 HOLDOUT VALIDATION
# ============================================================

print("=" * 75)
print("          FAILSAFE AI - V6 HOLDOUT VALIDATION")
print("=" * 75)

print()
print("Testing 30 additional unseen scenarios...")
print()


# ============================================================
# INITIALIZE
# ============================================================

results = []

top_1_hits = 0
top_3_hits = 0


# ============================================================
# RUN VALIDATION CASES
# ============================================================

for test in VALIDATION_CASES:

    predictions, detected_equipment = analyze_description(
        test["description"]
    )

    # Get ranked failure modes
    modes = [
        prediction["failure_mode"]
        for prediction in predictions
    ]

    expected = test["expected"]

    # --------------------------------------------------------
    # FIND RANK OF EXPECTED FAILURE MODE
    # --------------------------------------------------------

    if expected in modes:
        rank = modes.index(expected) + 1
    else:
        rank = None

    # --------------------------------------------------------
    # TOP-1 / TOP-3
    # --------------------------------------------------------

    top1 = rank == 1

    top3 = (
        rank is not None
        and rank <= 3
    )

    if top1:
        top_1_hits += 1

    if top3:
        top_3_hits += 1

    # --------------------------------------------------------
    # TOP PREDICTION
    # --------------------------------------------------------

    predicted = (
        modes[0]
        if modes
        else "None"
    )

    # --------------------------------------------------------
    # PRINT RESULT
    # --------------------------------------------------------

    print("-" * 75)

    print(
        "Test Case       :",
        test["id"]
    )

    print(
        "Expected        :",
        expected
    )

    print(
        "Predicted #1    :",
        predicted
    )

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

    print(
        "Equipment       :",
        detected_equipment
        if detected_equipment
        else "None"
    )

    # --------------------------------------------------------
    # SAVE RESULT
    # --------------------------------------------------------

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
            detected_equipment
            if detected_equipment
            else "None"
    })


# ============================================================
# CALCULATE METRICS
# ============================================================

total = len(VALIDATION_CASES)

top1_rate = (
    top_1_hits / total
) * 100

top3_rate = (
    top_3_hits / total
) * 100


# ------------------------------------------------------------
# AVERAGE EXPECTED RANK
# ------------------------------------------------------------

ranks = [
    result["Expected Rank"]
    for result in results
    if isinstance(
        result["Expected Rank"],
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
print("                    HOLDOUT RESULTS")
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
# FAILED CASES
# ============================================================

print()
print("=" * 75)
print("                    FAILED CASES")
print("=" * 75)

print()

failed_cases = [
    result
    for result in results
    if result["Top-1 Hit"] == "FAIL"
]

if not failed_cases:

    print("No Top-1 failures.")

else:

    for failure in failed_cases:

        print("-" * 75)

        print(
            "Test Case     :",
            failure["Test Case"]
        )

        print(
            "Expected      :",
            failure["Expected Failure"]
        )

        print(
            "Predicted     :",
            failure["Predicted #1"]
        )

        print(
            "Expected Rank :",
            failure["Expected Rank"]
        )

        print(
            "Equipment     :",
            failure["Detected Equipment"]
        )


# ============================================================
# SAVE RESULTS
# ============================================================

df = pd.DataFrame(results)

df.to_csv(
    "failsafe_v6_holdout_results.csv",
    index=False
)


# ============================================================
# COMPLETE
# ============================================================

print()
print("=" * 75)
print("Validation results saved to:")
print("failsafe_v6_holdout_results.csv")
print("=" * 75)

print()
print("V6 holdout validation complete.")

