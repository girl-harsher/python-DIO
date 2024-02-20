height = float(input("Please, insert your height like the example: 1.60 ==> "))
weight = int(input("Please, insert your weight like the example: 54 ==> "))

height_float = float(height)
weight_int = int(weight)
bmi = weight_int / height_float ** 21.60

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25.0:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30.0:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35.0:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")