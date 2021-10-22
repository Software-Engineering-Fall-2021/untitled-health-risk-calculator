import webbrowser

from flask import Flask, request, render_template

app = Flask(__name__)

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


@app.route("/")
def index():
    return render_template("index.html")


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

    age_score = find_age_score(float(age))
    bmi_score = find_bmi(float(height), float(weight))
    bp_score = find_bp_score(float(sys_bp), float(dia_bp))
    history_score = find_disease_score(diabetes, cancer, alz)
    overall_score = age_score + bmi_score + bp_score + history_score

    insurance_status = find_risk(int(overall_score))
    print(f"According to your score you are {insurance_status}")

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


def find_age_score(age):
    score = 0
    if age < 30:
        score = score
    elif age < 45:
        score += 10
    elif age < 60:
        score += 20
    else:
        score += 30
    return score


def find_bmi(height, weight):
    score = 0
    bmi = (weight/height/height) * 703
    if bmi < 24.9:
        score = score
    elif bmi < 29.9:
        score += 30
    else:
        score += 75
    return score


def find_disease_score(dia, canc, alz):
    score = 0
    if dia.lower() != 'n':
        score += 10
    if canc.lower() != 'n':
        score += 10
    if alz.lower() != 'n':
        score += 10
    return score


def find_risk(score):
    if score <= 20:
        return 'low risk'
    elif score <= 50:
        return 'moderate risk'
    elif score <= 75:
        return 'high risk'
    else:
        return 'uninsurable'


def find_bp_score(sys, dia):
    score = 0
    if sys < 120 and dia < 80:
        score = score
    elif sys < 130 and dia < 80:
        score += 15
    elif sys < 140 or dia < 90:
        score += 30
    elif sys < 180 or dia > 90:
        score += 75
    else:
        score += 100
    return score
    

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000)