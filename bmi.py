def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)
    print("BMI = " + str(bmi))

    if bmi < 18.5:
        print("user is underweight")
        return -1
    elif bmi > 25:
        print("user is normal weight")
        return 1
    else:
        print("user is normal weight")
        return 0


result = (calculate_bmi(weight=57, height=1.73))
print(result)
