def calculate_bmi(weight,height):
    bmi = weight / (height**2)

    if bmi < 18.5:
        print("BMI:", round(bmi,2), "Underweight")
    elif bmi < 25:
        print("BMI:", round(bmi, 2), "Normal")
    elif bmi < 30:
        print("BMI:", round(bmi,2), "Overweight")
    else:
        print("BMI:", round(bmi,2), "Obese")

    return bmi
calculate_bmi(60, 1.65)
