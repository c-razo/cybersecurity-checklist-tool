from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/checklist')
def checklist():
    return render_template('checklist.html')

from flask import request

@app.route('/results', methods=['POST'])
def results():
    # Get responses
    firewall = request.form.get('firewall')
    router = request.form.get('router')
    wifi = request.form.get('wifi')
    antivirus = request.form.get('antivirus')
    os_updates = request.form.get('os_updates')
    data_backup = request.form.get('data_backup')
    data_encryption = request.form.get('data_encryption')

    # Calculate score
    score = 0
    fields = [firewall, router, wifi, antivirus, os_updates, data_backup, data_encryption]
    for field in fields:
        if field == "yes":
            score += 1

    # Generate recommendations
    total_questions = len(fields)
    if score == total_questions:
        recommendations = "Excellent! Your business is well-secured."
    elif score >= total_questions * 0.7:
        recommendations = "Good job! Consider addressing a few areas to improve further."
    elif score >= total_questions * 0.4:
        recommendations = "Needs improvement. Focus on addressing critical areas."
    else:
        recommendations = "Critical! Immediate action is required to secure your business."

    # Return score and recommendations
    return f"Your Score: {score}/{total_questions}<br>{recommendations}"

if __name__ == "__main__":
    app.run(debug=True)

