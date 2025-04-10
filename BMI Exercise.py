height = float(input("Please input your height in inches. "))
weight = float(input("Please input your weight in pounds. "))
bmi = (weight * 703) / (height * height)
rounded_bmi = round(bmi, 2)

if bmi < 16.0:
    print("Severely Underweight")
elif 16.0 <= bmi <= 18.4:
    print(f"Your bmi of {rounded_bmi} makes you Underweight")
elif 18.5 <= bmi <= 24.9:
    print(f"Your bmi of {rounded_bmi} makes you Normal")
elif 25.0 <= bmi <= 29.9:
    print(f"Your bmi of {rounded_bmi} makes you Overweight")
elif 30.0 <= bmi <= 34.9:
    print(f"Your bmi of {rounded_bmi} makes you Moderately Obese")
elif 35.0 <= bmi <= 39.9:
    print(f"Your bmi of {rounded_bmi} makes you Moderately Obese")
else:
    print(f"Your bmi of {rounded_bmi} makes you fat as hell.")