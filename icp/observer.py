from typing import Any, Tuple, Dict
from .types import Signal, Noise, Truth

class ObserverCore:
    """
    Reference State and Telemetry Monitor.
    Provides ground truth reference with acknowledged noise.
    """
    def __init__(self, config: Any) -> None:
        self.snr_threshold = config.get("snr_threshold", 0.5)
        self.reference_length = config.get("reference_length", 128)

    def measure_snr(self, signal: Signal, noise: Noise) -> float:
        signal_power = len(signal)
        noise_power = max(len(noise), 1)
        return signal_power / noise_power

    def compute_error(self, signal: Signal) -> float:
        return abs(len(signal) - self.reference_length) / self.reference_length

    def observe(self, signal: Signal, noise: Noise) -> Tuple[Truth | None, Dict[str, float]]:
        snr = self.measure_snr(signal, noise)
        error = self.compute_error(signal)

        telemetry = {
            "snr": snr,
            "error": error,
            "signal_power": float(len(signal))
        }

        if snr < self.snr_threshold:
            return None, telemetry

        return Truth(signal), telemetry
