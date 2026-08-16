# FailSafe AI

### Context-Aware FMEA Risk Decision Support

FailSafe AI is a prototype decision-support tool that analyzes natural-language descriptions of industrial equipment problems and prioritizes potential failure modes using FMEA-based risk information.

The system combines:

- Equipment context detection
- Diagnostic symptom matching
- Symptom-priority weighting
- FMEA Risk Priority Number (RPN)
- Failure-mode relevance scoring
- Recommended maintenance actions

---

## Problem

Traditional keyword-based failure-mode matching can produce false positives when multiple failure modes share common symptoms such as:

- leakage
- vibration
- pressure loss
- overheating

FailSafe AI improves prioritization by combining equipment context with diagnostic symptom evidence and FMEA risk.

---

## Approach

The system follows the pipeline:

User Description
↓
Equipment Context Detection
↓
Failure Mode Candidate Generation
↓
Diagnostic Symptom Weighting
↓
FMEA Risk Calculation
↓
Priority Ranking
↓
Recommended Actions

---

## Example

### Input

> Hydraulic system is losing fluid around the hose and pressure is dropping intermittently.

### Output

**Detected Equipment:** Hydraulic System

**Priority Diagnosis:** Hose Leakage

**RPN:** 180

**Risk Level:** HIGH

**Relevance Score:** 140

**Priority Score:** 460

### Recommended Actions

- Inspect hose condition
- Replace damaged hoses
- Monitor pressure

---

## V5 → V6 Improvement

The V6 version introduced diagnostic symptom weighting to give stronger importance to distinctive symptoms.

| Metric | V5 | V6 |
|---|---:|---:|
| Scenarios tested | 10 | 10 |
| Top-1 identification | 80% | 100% |
| Top-3 identification | 100% | 100% |
| Average expected rank | 1.30 | 1.00 |

V6 achieved:

**100% Top-1 identification across 10 unseen synthetic industrial scenarios.**

---

## Validation

The initial evaluation used 10 unseen synthetic industrial scenarios.

Additional holdout scenarios were developed separately to support broader validation without modifying the V6 scoring logic.

The current prototype should not be interpreted as a universally validated industrial diagnostic system. Broader validation across more equipment types, failure modes, and real-world maintenance descriptions remains future work.

---

## Current Knowledge Base

The prototype currently contains synthetic FMEA failure patterns covering:

- Hydraulic systems
- Pneumatic systems
- Conveyor systems
- Electric motors
- Industrial pumps
- Industrial mixers

The knowledge base is synthetic and does not contain proprietary or company-confidential data.

---

## Technology

- Python
- Pandas
- Regular expressions
- FMEA methodology
- Streamlit

---

## Dashboard

A Streamlit dashboard provides an interactive interface for entering equipment problems and viewing:

- Detected equipment
- Priority failure mode
- RPN
- Risk level
- Diagnostic evidence
- Potential causes
- Potential effects
- Recommended actions
- Alternative failure modes

---

## Limitations & Future Work

Future improvements could include:

- Larger and more diverse validation datasets
- Additional equipment categories
- Additional failure modes
- Real-world maintenance descriptions
- Improved semantic language understanding
- Confidence calibration
- Expert validation
- Historical failure-data integration

---

## Disclaimer

FailSafe AI is a prototype decision-support system for demonstration and research purposes.

Its outputs should be validated by qualified domain experts before being used for actual maintenance or safety decisions.