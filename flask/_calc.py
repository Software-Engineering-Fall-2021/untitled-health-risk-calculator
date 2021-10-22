# _calc.py - Healthcare Risk Calculator - Fall 2021 Software Engineering
# Team Untitled
# Description: Handles all calculation and conversions for scores.
# Version 1

# Find score based on age.
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

# Calculate BMI and return score based on BMI.
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

# Find total disease score based on diabetes, alzheimers, and cancer.
def find_disease_score(dia, canc, alz):
    score = 0
    if dia.lower() != 'n':
        score += 10
    if canc.lower() != 'n':
        score += 10
    if alz.lower() != 'n':
        score += 10
    return score

# Converter for the risk scores.
def find_risk(score):
    if score <= 20:
        return 'LOW RISK'
    elif score <= 50:
        return 'MODERATE RISK'
    elif score <= 75:
        return 'HIGH RISK'
    else:
        return 'UNINSURABLE'

# Find blood pressure score based on systolic and diastolic.
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