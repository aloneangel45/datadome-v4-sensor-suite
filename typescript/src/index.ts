export interface SensorOptions {
  url: string;
  deviceType?: "desktop" | "mobile";
  userAgent?: string;
}

export class DataDomeClient {
  private rapidApiKey: string;
  private host: string;

  constructor(apiKey: string, host = "datadome-v4-x-sensor-emulation-device-telemetry-suite.p.rapidapi.com") {
    this.rapidApiKey = apiKey;
    this.host = host;
  }

  async generateSensor(options: SensorOptions) {
    const res = await fetch(`https://${this.host}/api/v1/datadome/sensor`, {
      method: "POST",
      headers: {
        "x-rapidapi-host": this.host,
        "x-rapidapi-key": this.rapidApiKey,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        url: options.url,
        device_type: options.deviceType || "desktop",
        user_agent: options.userAgent
      })
    });

    if (!res.ok) {
      throw new Error(`DataDome API error: ${res.status} ${res.statusText}`);
    }
    return await res.json();
  }
}
