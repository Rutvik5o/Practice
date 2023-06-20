# Exercise 7

weight=float(input("Enter Weight In KG:"))

height=float(input("Enter Height In Feet:"))

bmi=round(weight/height**2)

if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are underweight.")

elif bmi <25:
   print(f"Your BMI is {bmi} and you are a Normal Weight.")

elif bmi < 30:
    print(f"Your BMI is {bmi} and you are OverWeight.")

elif bmi <35:
    print(f"Your BMI is {bmi} and you are obese.")

else:
    print(f"Your BMI is {bmi} and you are clinically obese.")