print("Welcome to Python Project 2 - BMI Calculator!!!")

Name = input("Enter your Name:")
Weight = float(input("Enter your Weight:"))
Height = float(input("Enter your Height:"))

bmi = Weight /float (Height/100)**2

if (bmi<18.5):
    print(Name)
    print("Your BMI is Under weight!!!")

elif (bmi>=18.5 and bmi<25):
    print(Name)
    print("Your BMI is normal and healthy!!!")

elif (bmi>=25 and bmi<30):
    print(Name)
    print("Your BMI is Over weight!!!")

else:
    print(Name)
    print("Your BMI is Obese!!!")

