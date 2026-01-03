from typing import NewType, List
Signal = NewType("Signal", str)
Noise = NewType("Noise", str)
Truth = NewType("Truth", str)
Phase = NewType("Phase", float)
Entropy = NewType("Entropy", float)
Impedance = NewType("Impedance", float)
SignalHistory = List[Signal]
Uncertainty = NewType("Uncertainty", float)