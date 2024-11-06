from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Use session to store the report data
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    user_details = data['userDetails']
    responses = data['responses']

    # Extract individual responses
    stress = int(responses[0])
    loneliness = int(responses[1])
    sleep = int(responses[2])
    sadness = int(responses[3])
    concentration = int(responses[4])

    # Detailed analysis for each question
    analysis = {}

    # Stress
    if stress <= 3:
        analysis['stress'] = "You have been feeling low stress recently, which is a good sign."
    elif stress <= 7:
        analysis['stress'] = "You seem to be dealing with moderate stress. Consider practicing relaxation techniques."
    else:
        analysis['stress'] = "High stress levels can affect your overall well-being. It may be helpful to try mindfulness or seek support."

    # Loneliness
    if loneliness <= 3:
        analysis['loneliness'] = "You don't often feel lonely, which is great for your mental health."
    elif loneliness <= 7:
        analysis['loneliness'] = "You may experience some loneliness from time to time. Consider socializing more or engaging in community activities."
    else:
        analysis['loneliness'] = "Frequent feelings of loneliness can impact mental health. It might be worth reaching out to a close friend, counselor, or professional."

    # Sleep Quality
    if sleep <= 3:
        analysis['sleep'] = "You seem to be getting good quality sleep, which is essential for your mental health."
    elif sleep <= 7:
        analysis['sleep'] = "Your sleep quality is moderate. Try to establish a consistent sleep schedule for better rest."
    else:
        analysis['sleep'] = "Poor sleep quality can lead to mental health concerns. Try improving your sleep environment or consider sleep therapy."

    # Sadness
    if sadness <= 3:
        analysis['sadness'] = "You rarely feel sad, which is great for your emotional well-being."
    elif sadness <= 7:
        analysis['sadness'] = "Feeling sad sometimes is normal, but if it persists, try engaging in uplifting activities."
    else:
        analysis['sadness'] = "Frequent sadness may indicate depression. It's important to seek support from loved ones or a mental health professional."

    # Concentration
    if concentration <= 3:
        analysis['concentration'] = "You seem to have good concentration, which is a positive sign."
    elif concentration <= 7:
        analysis['concentration'] = "Moderate difficulty in concentration may indicate some mental fatigue. Resting or reducing distractions might help."
    else:
        analysis['concentration'] = "Difficulty concentrating can be a sign of mental strain or anxiety. Consider reducing stress or practicing focus exercises."

    # Calculate overall score
    score = stress + loneliness + sleep + sadness + concentration
    final_report = ""

    if score <= 15:
        final_report = "Your mental well-being appears to be in good shape. Keep taking care of yourself."
    elif score <= 30:
        final_report = "You're experiencing some moderate mental strain. It's important to incorporate self-care practices."
    else:
        final_report = "You might be facing significant mental challenges. Seeking help from a mental health professional is strongly recommended."

    # Store the report and analysis in the session
    from flask import session
    session['report'] = final_report
    session['analysis'] = analysis

    return jsonify({"report": final_report, "detailed_analysis": analysis})

@app.route('/report')
def report():
    # Get the report and analysis from the session
    from flask import session
    report = session.get('report')
    analysis = session.get('analysis')

    if report is None or analysis is None:
        return redirect(url_for('index'))  # Redirect if no data found

    return render_template('report.html', report=report, analysis=analysis)

if __name__ == '__main__':
    app.run(debug=True)
