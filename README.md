# Farm21 IoT Dashboard

An intelligent agriculture control system built on Raspberry Pi for the CS50 final project. Farm21 monitors environmental conditions and automates the control of critical farming systems through a real-time web dashboard.

## Overview

Farm21 is an IoT-based farm management system that combines sensor monitoring and automated device control. It enables remote monitoring of humidity, temperature, and light levels while allowing users to control pumps, fans, and lighting systems through a web interface.

## Features

- **Real-time Sensor Monitoring**
  - Humidity & Temperature sensor (DHT-like sensor on GPIO 20)
  - Light-dependent resistor (LDR) sensor on GPIO 16 for ambient light detection

- **Device Control via Relay Modules**
  - Pump control (GPIO 13)
  - Fan control (GPIO 19)
  - Light control (GPIO 26)

- **Web-based Dashboard**
  - Monitor sensor readings in real-time
  - Toggle devices on/off with a single click
  - Responsive interface for desktop and mobile access

## Hardware Requirements

- Raspberry Pi (any model with GPIO pins)
- DHT-type humidity & temperature sensor
- Light-dependent resistor (LDR) sensor
- 3-channel relay module
- Pump, fan, and lighting fixtures
- Jumper wires and GPIO connectors

## Software Requirements

- Python 3.x
- Flask
- RPi.GPIO library
- Modern web browser

## Installation

### 1. Install Dependencies

```bash
pip install flask RPi.GPIO
```

### 2. GPIO Configuration

The application uses the following GPIO pins (BCM mode):

| Component | GPIO Pin | Purpose |
|-----------|----------|---------|
| Humidity/Temp Sensor | 20 | Input |
| LDR Sensor | 16 | Input |
| Pump Relay | 13 | Output |
| Fan Relay | 19 | Output |
| Light Relay | 26 | Output |

### 3. Run the Application

```bash
python main.py
```

The web server will start on `0.0.0.0:80` (requires sudo/root privileges for port 80).

## Usage

1. Access the dashboard via your browser: `http://<raspberry-pi-ip>`
2. View real-time sensor status at the top of the dashboard
3. Use the control buttons to toggle pump, fan, and light relays

### Device Control

Click the **TURN ON** or **TURN OFF** buttons next to each device to control them:
- **Pump**: Controls water pumping/irrigation
- **Fan**: Controls ventilation/cooling
- **Light**: Controls lighting system

## Project Structure

```
farm21-cs50/
├── main.py              # Flask application & GPIO management
├── templates/
│   └── index.html       # Web dashboard interface
├── static/
│   └── master.css       # Stylesheet for the dashboard
├── README.md            # This file
└── LICENSE
```

## Technical Details

### Backend (main.py)
- **Framework**: Flask
- **GPIO Control**: RPi.GPIO library in BCM mode
- **Routes**:
  - `/` - Main dashboard with current device status
  - `/<deviceName>/<action>` - Endpoint to control devices (on/off)

### Frontend (index.html)
- HTML5 structure with embedded Jinja2 templating
- Dynamic button states based on relay status
- Direct links to control endpoints for device toggling

### Styling (master.css)
- Clean, responsive dashboard design
- Visual feedback for device status
- Mobile-friendly layout

## Author

Created as the CS50 final project.

## License

See [LICENSE](LICENSE) file for details.
