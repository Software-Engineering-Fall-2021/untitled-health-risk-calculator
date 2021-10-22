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
    try:
        overall_score = 0
        age = int(input("Enter your age in years: "))
        height_in_inches = int(input("Enter your height in inches: "))
        weight_in_pounds = int(input("Enter your weight in pounds: "))
        systolic_bp = int(input("Enter your systolic blood pressure: "))
        diastolic_bp = int(input("Enter your diastolic blood pressure: "))
        diabetes = input("Do you have a family history of diabetes? (y/n): ")
        cancer = input("Do you have a family history of cancer? (y/n): ")
        alzheimers = input("Do you have a family history of alzheimers? (y/n): ")
    except Exception as ex:
        print("Please enter only whole numbers or letters.")
    

    age_score = find_age_score(age)
    bmi_score = find_bmi(height_in_inches, weight_in_pounds)
    disease_score = find_disease_score(diabetes, cancer, alzheimers)
    bp_score = find_bp_score(systolic_bp, diastolic_bp)

    overall_score = age_score + bmi_score + disease_score + bp_score
    print(f"Overall score is {overall_score}")

    final_score = find_risk(overall_score)
    print(f"According to your numbers, you are {final_score}")
