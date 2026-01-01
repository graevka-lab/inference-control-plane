from typing import List
from .types import Signal

class ChronoHelix:
    """
    Temporal Integration Unit.
    Applies temporal lag filtering to reduce oscillation and improve sequence coherence.
    """
    def __init__(self, window_size: int = 3) -> None:
        self.history: List[Signal] = []
        self.window_size = window_size

    def integrate(self, signal: Signal) -> Signal:
        self.history.append(signal)
        start = max(0, len(self.history) - self.window_size)
        window_signals = self.history[start:]
        # simple averaging placeholder: return signal of median length
        median_len = int(sum(len(s) for s in window_signals) / len(window_signals))
        return Signal(signal[:median_len])
