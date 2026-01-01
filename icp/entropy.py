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
        telemetry = {"entropy": float(entropy)}
        if float(entropy) > self.entropy_limit:
            signal = self.soft_filter(signal)
        return signal, telemetry
