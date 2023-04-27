def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)
    print("BMI = " + str(bmi))

    if bmi < 18.5:
        print("user is underweight")
    elif bmi > 25:
        print("user is overweight")
    else:
        print("user is normal weight")


calculate_bmi(weight=57, height=1.73)