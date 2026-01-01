# ICP Inference Sequence

This document describes a single inference pass through ICP.

---

## Sequence

1. **Input Reception**
   - Raw user input is cast to `Signal`

2. **Resonance Tuning**
   - Source impedance compared to internal impedance
   - Gain adjusted under mismatch

3. **Entropy Measurement**
   - Lexical diversity estimated
   - Parasitic patterns attenuated if needed

4. **Temporal Integration**
   - Signal collapsed into a stable intermediate form

5. **Observation**
   - SNR measured
   - Deviation from reference computed
   - Telemetry emitted

6. **Decision**
   - If instability exceeds thresholds → suppression
   - Otherwise → Truth accepted

7. **Output Ramp**
   - Output gain applied based on stability
   - Final output released

---

## Failure Path

```text
Low SNR → Observer suppresses output → system halts safely

---

Key Property

At no point does ICP:

modify model weights

access logits

require retraining

All control is external, deterministic, and reversible.