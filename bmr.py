# Basal Metabolic Rate Calculator
weight = int(input("Enter your weight in kilograms: \n")) #79
height = int(input("Enter your height in centimeters: \n")) #183
age = int(input("Enter your age in years: \n")) #37
gender = str(input("Are you male or female (m/f)?"))

if gender == "m":
    gender = True
elif gender == "f":
    gender = False
else:
    print("Error")
    quit()

    
# Mifflin St. Jear Equation for males
if gender:
    bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
else:
    bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
bmr = round(bmr)
print(bmr)
