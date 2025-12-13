# piLedSignal

## Project Description
`piLedSignal` is a Python-based project designed to control LED signals on a Raspberry Pi using the Pi5Neo library. It includes functionality to:
- Illuminate LEDs with various colors.
- Check network connectivity and internet availability.

This project is ideal for Raspberry Pi enthusiasts who want to integrate LED signaling with network status monitoring.

---

## Features
- **LED Control**: Illuminate LEDs with predefined or custom colors.
- **Network Monitoring**: Check local network and internet connectivity.

---

## Requirements
The project requires the following Python dependencies:

```
certifi==2025.11.12
charset-normalizer==3.4.4
idna==3.11
Pi5Neo==1.0.6
requests==2.32.5
spidev==3.8
urllib3==2.6.2
```

Install the dependencies using:
```bash
pip install -r requirements.txt
```

---

## File Structure
- `src/piLedSignal.py`: Contains the main logic for LED illumination.
- `src/netcheck.py`: Handles network and internet connectivity checks.
- `requirements.txt`: Lists the required Python packages.

---

## Setup and Compilation
1. Clone the repository:
   ```bash
   git clone https://github.com/tirtharajsinha/customization_linux.git
   cd customization_linux/raspiCustomization/piLedSignal
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:
   ```bash
   python src/piLedSignal.py
   ```

---

## Build the executable
1. Actiavte the Virtual environment
2. install pyinstaller 
    ```
    pip install pyinstaller
    ```
3. Build
    ```
    pyinstaller --onefile ./src/piLedSignal.py

    ```
4. Run the executable
    ```
    ./dist/piLedSignal
    ```


## Autostart on Boot
1. Generate the installer and save in prefered path.
2. Modify the 


## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author
Developed by Tirtharaj Sinha.