height = 1.75
weight = 97

bmi = weight/ (height ** 2)

if bmi > 18.5:
    print("Your bmi is above weight", bmi)
elif bmi < 18.5:
    print("Your bmi is below weight", bmi)
elif 18.5 <= 25:
    print("Your bmi is equal or above weight", bmi)