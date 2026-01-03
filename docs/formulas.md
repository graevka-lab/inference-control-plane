# Mathematical Framework of ICP

## 1. Free Energy of Inference
ICP minimizes the variational free energy of the inference process:

$$
\mathcal{F}_{\text{inf}} = \underbrace{\mathbb{E}[H(t)]}_{\text{Entropy Production}} + \underbrace{D_{\mathrm{KL}}(Q(h_t) \| P(h_t \mid u))}_{\text{Impedance Mismatch}} - \underbrace{\gamma \cdot \mathcal{C}(h_t)}_{\text{Resonance Gain}} + \underbrace{\lambda \cdot U(t)}_{\text{Meta-Uncertainty}}
$$

Where:
*   $H(t)$: Token-level entropy.
*   $D_{\mathrm{KL}}$: Divergence between actual ($Q$) and intended ($P$) trajectory.
*   $\mathcal{C}(t)$: Coherence (resonance).
*   $U(t)$: Meta-uncertainty.

## 2. Phase Locking Condition (Multi-Agent)
For agents $i$ and $j$, synchronization occurs when phase difference is bounded:

$$
|\phi_i(t) - \phi_j(t)| < \epsilon
$$

## 3. Adaptive Entropy Threshold
The entropy limit $H_{max}$ is modulated by uncertainty $U(t)$:

$$
H_{max}^{adaptive}(t) = \frac{H_{max}}{1 + U(t)}
$$