import math
from typing import Any, Dict
from .types import Truth

class DawnProtocol:
    """
    Output Power Ramp and Stability Protection.
    Prevents cognitive thermal shock.
    """
    def __init__(self, config: Any) -> None:
        self.max_power = config.get("max_output_power", 1.0)
        self.temporal_window = config.get("temporal_window_size", 3)

    def ramp(self, truth: Truth, telemetry: Dict[str, float]) -> Truth:
        """
        Adaptive ramp based on system stability.
        """
        error = telemetry.get("error", 0.0)
        snr = telemetry.get("snr", 1.0)

        stability = max(min(snr / (1 + error), 1.0), 0.1)
        gain = min(stability, self.max_power)
        ramp_len = int(len(truth) * gain)
        return Truth(truth[:ramp_len])
