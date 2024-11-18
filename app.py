from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/checklist')
def checklist():
    return render_template('checklist.html')

@app.route('/results', methods=['POST'])
def results():
    # Get responses from the form
    firewall = request.form.get('firewall')
    router = request.form.get('router')
    wifi = request.form.get('wifi')
    antivirus = request.form.get('antivirus')
    os_updates = request.form.get('os_updates')
    data_backup = request.form.get('data_backup')
    data_encryption = request.form.get('data_encryption')

    # Calculate score and count unknowns
    score = 0
    unknown_count = 0
    fields = [firewall, router, wifi, antivirus, os_updates, data_backup, data_encryption]

    for field in fields:
        if field == "yes":
            score += 1
        elif field == "unknown":
            unknown_count += 1

    # Generate recommendations
    total_questions = len(fields)
    if score == total_questions:
        recommendations = "Excellent! Your business is well-secured."
    elif score >= total_questions * 0.7:
        recommendations = "Good job! Address the 'I don't know' areas to improve further."
    elif score >= total_questions * 0.4:
        recommendations = f"Needs improvement. Focus on the 'no' responses and {unknown_count} 'I don't know' areas."
    else:
        recommendations = "Critical! Immediate action is required to secure your business."

    # Save results to a file
    with open("results.txt", "w") as file:
        file.write(f"Your Score: {score}/{total_questions}\n")
        file.write(f"Unknown responses: {unknown_count}\n")
        file.write(f"Recommendations: {recommendations}\n")

    # Return score, unknowns, and recommendations
    return f"Your Score: {score}/{total_questions}<br>Unknown responses: {unknown_count}<br>{recommendations}"

if __name__ == "__main__":
    app.run(debug=True)

