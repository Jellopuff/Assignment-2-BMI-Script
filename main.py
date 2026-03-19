def BMI_calc(height, weight):
    vals = height.split("\'")
    kgWeight = weight * 0.45
    meterHeight = (int(vals[0])*12 + int(vals[1])) * 0.025

    BMI = round(kgWeight / (meterHeight ** 2), 1)
    return classification(BMI)

def classification(BMI):
    category = ""

    if(BMI >= 19.5): #boundary shift
        if(BMI >= 25):
            if(BMI >= 30):
                category = "Obese"
            else:
                category = "Overweight"
        else:
            category = "Normal weight"
    else:
        category = "Underweight"

    print(f"BMI: {BMI}\nCategory: {category}")
    quit()

BMI = 0.0 #edit for testing purposes, 0.0 for default behavior
if(BMI != 0.0):
    {
        classification(BMI)
    }

print("Enter your height in feet and inches (in the form X'Y, including if Y is 0): ")
height = str(input(""))
print("Enter your weight in pounds: ")
weight = float(input(""))

BMI_calc(height, weight)

