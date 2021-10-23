from flask import Flask, request, render_template
import webbrowser
import _calc as c

# main.py - Healthcare Risk Calculator - Fall 2021 Software Engineering
# Team Untitled
# Description: Handles Flask routing and the web application
# Version 1

app = Flask(__name__)

# Test dictionary entry
value_dictionary = {
    'age': 21,
    'weight': 200,
    'height': 72,
    'systolic': 80,
    'diastolic': 102,
    'diabetes': 'n',
    'cancer': 'n',
    'alz': 'n'
}

# Routing for index page.
@app.route("/")
def index():
    return render_template("index.html")

# Calculation handler.
@app.route("/server_app", methods=["GET", "POST"])
def server_app():
    age = request.form.get("age")
    height = request.form.get("height")
    weight = request.form.get("weight")
    sys_bp = request.form.get("sys_bp")
    dia_bp = request.form.get("dia_bp")
    diabetes = request.form.get("diabetes")
    cancer = request.form.get("cancer")
    alz = request.form.get("alz")

    age_flag = False
    bmi_flag = False
    bp_flag = False
    history_flag = False

    # Find age score.
    if (age is not None) and (float(age) < 120) and (float(age) > 0):
        age_score = c.find_age_score(float(age))
    else:
        age_score = "ERROR: PLEASE PROVIDE A VALID AGE"
        age_flag = True
    
    # Find bmi score.
    if (height is not None) and (weight is not None) and (float(height) < 110) and (float(height) > 24) and (float(weight) < 1000) and (float(weight) > 50):
        bmi_score = c.find_bmi(float(height), float(weight))
    else:
        bmi_score = "ERROR: PLEASE PROVIDE A VALID HEIGHT AND WEIGHT"
        bmi_flag = True
    
    # Find bp score.
    if (sys_bp is not None) and (dia_bp is not None) and (float(sys_bp) < 210) and (float(sys_bp) > 80) and (float(dia_bp) < 150) and (float(weight) > 50):
        bp_score = c.find_bp_score(float(sys_bp), float(dia_bp))
    else:
        bp_score = "ERROR: PLEASE PROVIDE VALID BLOOD PRESSURE SCORES"
        bp_flag = True

    # Find all scores.
    if (diabetes == "y" or diabetes == "n") and (cancer == "y" or cancer == "n") and (alz == "y" or alz == "n"):
        history_score = c.find_disease_score(diabetes, cancer, alz)
    else:
        history_score = "ERROR: PLEASE PROVIDE A VALID ANSWER TO HEALTH HISTORY QUESTIONS"
        history_flag = True 

    # Find overall score
    if (age_flag is not True) and (bmi_flag is not True) and (bp_flag is not True) and (history_flag is not True):
        overall_score = age_score + bmi_score + bp_score + history_score   
        insurance_status = c.find_risk(int(overall_score))
        print(f"According to your score you are {insurance_status}")
    else:
        insurance_status = "ERROR, PLEASE USE VALID STATS IN THE CALCULATOR AND TRY AGAIN."

    return render_template('index.html',
                           age=age,
                           weight=weight,
                           height=height,
                           sys_bp=sys_bp,
                           dia_bp=dia_bp,
                           diabetes=diabetes,
                           cancer=cancer,
                           alz=alz,
                           age_score = age_score,
                           bmi_score = bmi_score,
                           bp_score = bp_score,
                           history_score = history_score,
                           status=insurance_status)
    
if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000)
