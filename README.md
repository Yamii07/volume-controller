
# 🎚️ Hand Gesture Volume Controller

A Python-based volume controller using **OpenCV** and **MediaPipe** that allows you to control your system volume with simple hand gestures via webcam.

---

## 🛠️ Features

- 📷 Real-time hand tracking using MediaPipe  
- ✋ Control system volume by changing the distance between your thumb and index finger  
- 🔊 Visual feedback for volume level on screen  
- 🧠 Intuitive gesture-based interface  

---

## 📦 Dependencies

Install the required libraries:

```bash
pip install opencv-python mediapipe numpy pycaw comtypes
```

> **Note:** `pycaw` only works on Windows.

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/Yamii07/volume-controller-hand-gestures.git
cd volume-controller-hand-gestures
```

2. Run the script:

```bash
python volume_control.py
```

3. Show your hand to the webcam and pinch your **thumb and index finger** to adjust the volume.

---

## 🧠 How It Works

- **MediaPipe** detects hand landmarks in real time.  
- Calculates the distance between **landmark 4 (thumb tip)** and **landmark 8 (index finger tip)**.  
- Maps that distance to a system volume range (0% - 100%).  
- Adjusts volume using **pycaw** on Windows.

---

## 📁 Project Structure

```
volume-controller-hand-gestures/
├── htmmod.py             # Modules for main File
├── volume_control.py     # Main script
├── README.md             # Project documentation
```

---

## ✅ Requirements

- 3.6 < Python < 3.12
- Webcam  
- Windows OS (required for volume control)

---

## 👨‍💻 Author

**Purshottam Kumar**  
GitHub: [@Yamii07](https://github.com/Yamii07)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
