from flask import Flask, jsonify, render_template
from Backend.cpu_monitoring import MonitorCpuSpike
from Backend.logs_monitoring import MonitorLogs

app = Flask(__name__, template_folder="Frontend", static_folder="Frontend/static")

# Route for login page
@app.route('/')
def login_page():
    return render_template("login_page.html")

# Route for dashboard
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

# Route for fetching CPU alerts
@app.route('/api/cpu-alerts', methods=['GET'])
def cpu_alerts():
    # Example: Fetch alerts dynamically (replace with real backend logic)
    alerts = [
        {"time": "2025-01-24 12:34:56", "message": "High CPU usage detected!"},
        {"time": "2025-01-24 12:45:10", "message": "CPU spike resolved."}
    ]
    return jsonify(alerts)

# Route for fetching log alerts
@app.route('/api/log-alerts', methods=['GET'])
def log_alerts():
    # Example: Fetch alerts dynamically (replace with real backend logic)
    alerts = [
        {"time": "2025-01-24 13:00:00", "message": "Critical log deletion detected!"},
        {"time": "2025-01-24 13:15:00", "message": "Unauthorized access to honeypot file!"}
    ]
    return jsonify(alerts)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
