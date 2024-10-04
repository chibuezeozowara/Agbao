print("Welcome to Sir Isaac's Body Mass Index Calculator")
Weight=(float(input("\nEnter your Weight in Kilograms: ")))
Height=(float(input("Enter your Height in Meters: ")))
BMI=Weight/(Height**2)
print(f"\nYour BMI is: {BMI:.1f}")
print("Your BMI is: " + str(BMI))
if(BMI<18.5):
    print("You're Underweight")
elif(18.5<BMI<24.9):
    print("You're Normal")
elif(24.9<BMI<29.9):
    print("You're Overweight")
else:
    print("You're Obese")