# 🛡️ DataDome v4.x Anti-Bot Sensor Payload Generator & Mobile/Web Device Telemetry Suite

[![RapidAPI](https://img.shields.io/badge/RapidAPI-Active%20Listing-blue.svg?logo=rapidapi)](https://rapidapi.com/aether-protocol-labs-aether-protocol-labs-default/api/datadome-v4-x-sensor-emulation-device-telemetry-suite)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Uptime](https://img.shields.io/badge/Uptime-99.98%25-brightgreen.svg)]()
[![Latency](https://img.shields.io/badge/Latency-Sub--40ms-brightgreen.svg)]()
[![Free Tier](https://img.shields.io/badge/Free%20Plan-50%20Calls%2Fmo-green.svg)]()

> **Enterprise-grade DataDome v4.x Anti-Bot Telemetry Suite. Generates authentic browser and mobile device sensor vectors (`d4`, mouse dynamics, device orientation, canvas fingerprints, and WebRTC hardware entropy) for frictionless DataDome bypass and payload generation.**

---

## 🚀 Instant Free Access (50 Free Calls/Month)

Subscribe and get your live API key in 5 seconds:  
👉 **[Subscribe on RapidAPI Hub (Free Plan Available)](https://rapidapi.com/aether-protocol-labs-aether-protocol-labs-default/api/datadome-v4-x-sensor-emulation-device-telemetry-suite)**

- **RapidAPI Host:** `datadome-v4-x-sensor-emulation-device-telemetry-suite.p.rapidapi.com`
- **Base Gateway:** `https://datadome-v4-x-sensor-emulation-device-telemetry-suite.p.rapidapi.com`

---

## ⚡ Why Use DataDome Sensor Suite?

* **Eliminate Browser Overhead:** Generate authentic `d4` sensor telemetry payloads via simple HTTP POST without heavy headless Chrome/Puppeteer/Playwright instances.
* **Pass Behavioral ML Checks:** Synthesizes human-like micro-timing jitter, mouse curvature vectors, and realistic hardware concurrency metrics.
* **Mobile & Desktop Emulation:** Emulate genuine iOS, Android, macOS, and Windows browser fingerprints.
* **Ultra-Low Latency:** Pre-computed and cached sensor models respond in `<40ms`.

---

## 💻 Quickstart Examples

### 1. cURL (Instant Terminal Test)
```bash
curl --request POST \
  --url https://datadome-v4-x-sensor-emulation-device-telemetry-suite.p.rapidapi.com/api/v1/datadome/sensor \
  --header 'x-rapidapi-host: datadome-v4-x-sensor-emulation-device-telemetry-suite.p.rapidapi.com' \
  --header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "url": "https://example.com",
    "device_type": "desktop",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
  }'
```

### 2. Python (`requests`)
```python
import requests

API_KEY = "YOUR_RAPIDAPI_KEY"

url = "https://datadome-v4-x-sensor-emulation-device-telemetry-suite.p.rapidapi.com/api/v1/datadome/sensor"
headers = {
    "x-rapidapi-host": "datadome-v4-x-sensor-emulation-device-telemetry-suite.p.rapidapi.com",
    "x-rapidapi-key": API_KEY,
    "Content-Type": "application/json"
}
payload = {
    "url": "https://target-store.com",
    "device_type": "desktop"
}

response = requests.post(url, json=payload, headers=headers)
print("DataDome Sensor Data:", response.json())
```

### 3. Node.js / TypeScript (`fetch`)
```typescript
async function getSensorPayload() {
  const res = await fetch("https://datadome-v4-x-sensor-emulation-device-telemetry-suite.p.rapidapi.com/api/v1/datadome/sensor", {
    method: "POST",
    headers: {
      "x-rapidapi-host": "datadome-v4-x-sensor-emulation-device-telemetry-suite.p.rapidapi.com",
      "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_RAPIDAPI_KEY",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      url: "https://target-store.com",
      device_type: "desktop"
    })
  });
  const data = await res.json();
  console.log("Telemetry Payload:", data);
}

getSensorPayload();
```

---

## 🎯 Endpoints Available

1. `POST /api/v1/datadome/sensor` — Synthesize high-entropy DataDome v4.x sensor payload matching target URL and user-agent.
2. `POST /api/v1/datadome/device-telemetry` — Retrieve hardware device characteristics (WebGL, audio entropy, canvas hash).

---

## 🔍 SEO & Use Cases
- **Sneaker & Retail Bots:** High-speed checkout automation on Footlocker, Nike, Shopify, and Hermes.
- **E-commerce Price Scrapers:** Scalable data extraction without triggering DataDome slider captchas or IP bans.
- **Undetected Web Automation:** Seamless integration with Python `curl_cffi`, `requests`, and Go `tls-client`.

---

## 📄 License
MIT © [Aether Protocol Labs](https://rapidapi.com/aether-protocol-labs-aether-protocol-labs-default)
