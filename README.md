
# CloudShield AI – DFIR Platform

CloudShield AI is a specialized Digital Forensics and Incident Response (DFIR) dashboard. It simulates cyber-attacks and demonstrates autonomous AI-driven response steps, including IP blocking, process termination, and forensic data collection.

## 🚀 Features

* **Real-time Incident Simulation:** Trigger "Brute Force," "Malware," or "Unauthorized Access" scenarios.
* **AI Analysis:** Context-aware reasoning for each specific attack type.
* **Automated Response:** Visualizes the lifecycle of an incident from detection to resolution.
* **Modern UI:** A high-contrast, "SOC-style" dashboard built for readability and data density.
* **Flask API:** A lightweight Python backend handling state management and logic.

## 🛠️ Tech Stack

* **Frontend:** HTML5, CSS3 (Glassmorphism UI), JavaScript (ES6 Fetch API)
* **Backend:** Python 3.x, Flask, Flask-CORS

---

## 📥 Installation & Setup

### 1. Clone or Download
Place the `app.py` (backend) and `index.html` (frontend) files in the same project directory.

### 2. Set Up Virtual Environment (Recommended)
```powershell
# Create environment
python -m venv .venv

# Activate environment
# On Windows:
& ".\.venv\Scripts\Activate.ps1"
# On Mac/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install flask flask-cors
```

---

## 🚦 How to Run

### Step 1: Start the Backend
Navigate to the project folder and run the Flask server:
```powershell
python app.py
```
* The server will start at `http://127.0.0.1:5000`.
* Keep this terminal window open.

### Step 2: Launch the Frontend
Simply open `index.html` in any modern web browser (Chrome, Edge, or Firefox).

### Step 3: Simulate
1.  Click **"Simulate Attack"** to generate a new incident.
2.  Watch the **Timeline** and **Response Steps** update automatically.
3.  Click **"Reset"** to clear the incident and log it into the **Incident History** table.

---

## 📁 Project Structure

* `app.py` – Flask server containing the attack logic and API routes.
* `index.html` – The dashboard UI and JavaScript for UI updates.
* `.venv/` – (Optional) Python virtual environment files.

## ⚠️ Troubleshooting

* **"Connection Failed" Error:** Ensure the Flask terminal says `Running on http://127.0.0.1:5000`. If you changed the port in Python, you must update the URL in the `index.html` script.
* **CORS Errors:** If the browser blocks the request, ensure `flask-cors` is installed and `CORS(app)` is present in `app.py`.
* **Blank Terminal:** If `python app.py` does nothing, ensure the file is saved and you are in the correct directory.

---
