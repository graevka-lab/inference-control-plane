import json
from typing import Dict, Any

class TelemetryLogger:
    def __init__(self, path: str = "telemetry.log") -> None:
        self.path = path

    def log(self, data: Dict[str, Any]) -> None:
        with open(self.path, "a") as f:
            f.write(json.dumps(data) + "\n")
            
from .telemetry import TelemetryLogger

self.telemetry = TelemetryLogger()
...
truth, telemetry = self.observer.observe(s3, noise)

self.telemetry.log(telemetry)
