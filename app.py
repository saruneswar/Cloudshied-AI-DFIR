from flask import Flask, jsonify
from flask_cors import CORS
import random
from datetime import datetime
import uuid

app = Flask(__name__)

# This is critical for allowing your HTML file to talk to this Python script
CORS(app)

# Global store for the incident state
current_incident = None

def get_attack_logic(attack_type):
    """Provides specific AI reasoning and steps based on attack type."""
    logic = {
        "Brute Force": {
            "ai": "Detected 50+ failed login attempts from a single source. Pattern matches 'Credential Stuffing'.",
            "steps": ["Source IP Null-routed", "User Account Locked", "MFA Challenge Triggered"]
        },
        "Malware": {
            "ai": "Signature-based detection identified 'Trojan.Win32' executing in temp directory.",
            "steps": ["Process Terminated", "File Quarantined", "Network Segment Isolated"]
        },
        "Unauthorized Access": {
            "ai": "Anomalous geolocation detected. User 'Admin' logged in from an unexpected ASN.",
            "steps": ["Session Invalidated", "SSH Keys Rotated", "Admin Escalation Logged"]
        }
    }
    return logic.get(attack_type)

@app.route('/incident', methods=['GET'])
def incident():
    global current_incident
    attack_type = random.choice(["Brute Force", "Malware", "Unauthorized Access"])
    severity = random.choice(["Low", "Medium", "High"])
    details = get_attack_logic(attack_type)

    current_incident = {
        "id": f"INC-{str(uuid.uuid4())[:8].upper()}",
        "status": "Active",
        "start_time": datetime.now().strftime("%H:%M:%S"),
        "end_time": None,
        "ip": f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}",
        "type": attack_type,
        "severity": severity,
        "ai": details["ai"],
        "steps": details["steps"]
    }
    print(f"--- ATTACK DETECTED: {current_incident['type']} from {current_incident['ip']} ---")
    return jsonify(current_incident)

@app.route('/resolve', methods=['GET'])
def resolve():
    global current_incident
    if current_incident:
        current_incident["status"] = "Resolved"
        current_incident["end_time"] = datetime.now().strftime("%H:%M:%S")
        print(f"--- INCIDENT RESOLVED: {current_incident['id']} ---")
        return jsonify(current_incident)
    return jsonify({"error": "No active incident"}), 404

@app.route('/current', methods=['GET'])
def current():
    return jsonify(current_incident if current_incident else {"status": "Idle"})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "Backend is Online", "timestamp": datetime.now().strftime("%H:%M:%S")})

if __name__ == '__main__':
    print("\n" + "="*40)
    print(" CLOUDSHIELD AI BACKEND INITIALIZED")
    print(" Listening at: http://127.0.0.1:5000")
    print("="*40 + "\n")
    app.run(host='127.0.0.1', port=5000, debug=True)