import json
from typing import Dict, Any
from .types import Signal, Impedance, Noise, Truth
from .resonance import ResonanceTuner
from .entropy import EntropyGate
from .temporal import ChronoHelix
from .observer import ObserverCore
from .dawn import DawnProtocol

class ControlConfig:
    """Loads control parameters from config.json."""
    def __init__(self, path: str = "config/charter.json") -> None:
        with open(path, "r") as f:
            self._data: Dict[str, Any] = json.load(f)

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

class InferenceControlPlane:
    """High-level orchestrator for inference-time stabilization."""
    def __init__(self, config_path: str = "config/charter.json") -> None:
        config = ControlConfig(config_path)
        self.resonance = ResonanceTuner(config)
        self.entropy = EntropyGate(config)
        self.temporal = ChronoHelix()
        self.observer = ObserverCore(config)
        self.dawn = DawnProtocol(config)

    def run(self, raw_input: str, source_impedance: float = 50.0, noise_floor: str = "") -> str | None:
        # Casting raw types to Semantic Types
        sig = Signal(raw_input)
        imp = Impedance(source_impedance)
        noise = Noise(noise_floor)

        # 1. Input Stage (Returns: Signal, Telemetry)
        # FIX: Unpacking the tuple
        s1, t1 = self.resonance.tune(sig, imp)
        
        # 2. Filter Stage (Returns: Signal, Telemetry)
        # FIX: Unpacking the tuple
        s2, t2 = self.entropy.process(s1)
        
        # 3. Temporal Integration (Returns: Signal)
        s3 = self.temporal.integrate(s2)

        # 4. Observation & Telemetry (Returns: Truth | None, Telemetry)
        truth, t4 = self.observer.observe(s3, noise)
        
        if truth is None:
            return None # Circuit Breaker

        # 5. Output Stage (Adaptive Ramp)
        # Uses telemetry from the Observer to decide gain
        final_output = self.dawn.ramp(truth, t4)
        
        return str(final_output)