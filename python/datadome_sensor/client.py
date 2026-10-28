import requests
from typing import Optional, Dict, Any

class DataDomeClient:
    """Enterprise client for DataDome v4.x Anti-Bot Sensor Emulation."""
    
    def __init__(self, rapidapi_key: str, host: str = "datadome-v4-x-sensor-emulation-device-telemetry-suite.p.rapidapi.com"):
        self.rapidapi_key = rapidapi_key
        self.host = host
        self.base_url = f"https://{host}/api/v1/datadome"

    def generate_sensor(self, target_url: str, device_type: str = "desktop", user_agent: Optional[str] = None) -> Dict[str, Any]:
        """Generate genuine browser/device sensor payload to bypass DataDome checkpoints."""
        headers = {
            "x-rapidapi-host": self.host,
            "x-rapidapi-key": self.rapidapi_key,
            "Content-Type": "application/json"
        }
        body = {
            "url": target_url,
            "device_type": device_type
        }
        if user_agent:
            body["user_agent"] = user_agent

        response = requests.post(f"{self.base_url}/sensor", json=body, headers=headers, timeout=12)
        response.raise_for_status()
        return response.json()
