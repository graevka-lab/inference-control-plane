# Control Law (PID-lite)

This document describes the control logic used by the Inference Control Plane (ICP).

ICP does not implement a full PID controller.
Instead, it uses a **PID-inspired heuristic control law** adapted for inference-time systems.

---

## Control Objective

Maintain inference stability by bounding:
- entropy growth
- signal deviation
- noise amplification

The objective is **stability**, not optimality.

---

## Signals

### Measured Signals
- Entropy (H)
- Signal-to-noise ratio (SNR)
- Signal length (L)

### Reference Signals
- Entropy limit H_ref
- Reference length L_ref
- Minimum acceptable SNR

---

## Error Signals

```text
e_entropy = max(0, H - H_ref)
e_length  = |L - L_ref| / L_ref
e_snr     = max(0, SNR_ref - SNR)

Errors are normalized to [0, 1].

---

Control Actions
Resonance Control (P-like)

Adjusts internal impedance based on mismatch

Acts immediately on deviation

ΔZ ∝ e_length

---

Entropy Control (I-like)

Accumulates entropy violations

Applies soft filtering after repeated instability

ΣH_violation → filter strength

---

Dawn Control (D-like damping)

Reduces output gain under rapid instability

Prevents sudden amplification

gain ∝ 1 / (1 + e_entropy + e_snr)

---

Why Not Full PID?

No continuous time base

No precise physical plant

Noise-dominated measurements

ICP favors interpretability and robustness over mathematical optimality.

---

Summary

ICP uses:

Proportional response to deviation

Integral response to persistent entropy

Derivative-like damping at output

This is sufficient to enforce stability in inference-time systems.