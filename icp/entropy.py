from typing import List, Any
from .types import Signal, Entropy

class EntropyGate:
    """
    Soft Noise Filter with Entropy Bounding.
    Applies gain reduction to parasitic patterns.
    """
    def __init__(self, config: Any) -> None:
        self.entropy_limit = config.get("entropy_limit", 1.0)
        self.entropy_window = config.get("entropy_window", 16)
        self.parasitic_signatures: List[str] = config.get("parasitic_signatures", [])

    def estimate_entropy(self, signal: Signal) -> Entropy:
        window_signal = signal[-self.entropy_window:] if len(signal) > self.entropy_window else signal
        unique_chars = len(set(window_signal))
        total_chars = max(len(window_signal), 1)
        return Entropy(unique_chars / total_chars)

    def soft_filter(self, signal: Signal) -> Signal:
        filtered = signal
        for pattern in self.parasitic_signatures:
            if pattern in filtered:
                filtered = Signal(filtered.replace(pattern, ""))
        return filtered

    def process(self, signal: Signal) -> (Signal, dict):
        entropy = self.estimate_entropy(signal)
        
        # Meta-Uncertainty Heuristic:
        # High entropy usually implies high uncertainty, but we add noise sensitivity
        uncertainty = float(entropy) * 0.5  # Placeholder heuristic
        
        telemetry = {
            "entropy": float(entropy),
            "meta_uncertainty": uncertainty
        }
        
        # Adaptive Thresholding:
        # If uncertainty is high, we lower the allowed entropy threshold
        adaptive_limit = self.entropy_limit / (1.0 + uncertainty)
        
        if float(entropy) > adaptive_limit:
            signal = self.soft_filter(signal)
            
        return signal, telemetry