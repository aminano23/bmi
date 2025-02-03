height = int(input("Enter height (in cm): "))
weight = int(input("Enter weight (in kg): "))

bmi = weight / (height / 100) ** 2

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal weight")
elif 25 <= bmi <= 29.9:
    print("Overweight")
elif 30 <= bmi <= 34.9:
    print("Obesity Class I")
elif 35 <= bmi <= 39.9:
    print("Obesity Class II")
elif bmi >= 40:
    print("Obesity Class III")
