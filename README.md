# **Traffic Light System**

This project simulates a traffic light system using a **Raspberry Pi 4** and three LEDs. The system mimics the operation of a standard traffic light, where the **green**, **amber (yellow)**, and **red** LEDs light up in sequence.

---

## **Features**
- **Simple Simulation**: Replicates the functionality of real-world traffic lights.
- **Timing Control**:
  - **Green Light**: On for 4 seconds.
  - **Amber Light**: On for 2 seconds (controls the transition).
  - **Red Light**: On for 4 seconds.
- Designed to be lightweight and easy to set up without additional libraries.

---

## **Hardware Requirements**
- **Raspberry Pi 4**
- 3 LEDs:
  - Green
  - Amber (Yellow)
  - Red
- 3 corresponding resistors (10Ω)
- Breadboard and jumper wires for connections.

---

## **Wiring Diagram**

![Traffic Light Wiring Diagram](./src/raspberry-pi-traffic-lights.png)
- Connect the LEDs to the Raspberry Pi GPIO pins:
  - **Green LED**: GPIO Pin `17`
  - **Amber LED**: GPIO Pin `23`
  - **Red LED**: GPIO Pin `22`
- The other terminal of each LED should be connected to a resistor and then to the ground.

---


## **Setup Instructions**
1. **Connect the LEDs and Resistors**:
   - Use the wiring diagram above to set up the circuit on your breadboard.
2. **Transfer the Code**:
   - Copy the `traffic_light.py` script to your Raspberry Pi.

---

## **How to Run the Code**
1. Ensure that Python 3 is installed on your Raspberry Pi.
2. Open a terminal and navigate to the directory containing `traffic_light.py`.
3. Run the script using the following command:
   ```bash
   python3 traffic_light.py
