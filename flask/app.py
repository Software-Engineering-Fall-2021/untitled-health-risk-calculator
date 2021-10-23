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

    # Find all scores.
    if (age is not None) and (height is not None) and (weight is not None) and (sys_bp is not None) and (dia_bp is not None) and (diabetes is "y" or diabetes is "n") and (cancer is "y" or cancer is "n") and (alz is "y" or alz is "n"):
        age_score = c.find_age_score(float(age))
        bmi_score = c.find_bmi(float(height), float(weight))
        bp_score = c.find_bp_score(float(sys_bp), float(dia_bp))
        history_score = c.find_disease_score(diabetes, cancer, alz)
        overall_score = age_score + bmi_score + bp_score + history_score

        # Calculate Risk and return.
        try:
            insurance_status = c.find_risk(int(overall_score))
            print(f"According to your score you are {insurance_status}")
        except:
            insurance_status = "ERROR, PLEASE USE VALID STATS IN THE CALCULATOR AND TRY AGAIN."
        
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
                           status=insurance_status)
    
if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000)
