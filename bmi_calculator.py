

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


print("===== BMI Calculator =====")

try:
    # User Input
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Input Validation
    if weight <= 0 or weight > 500:
        print("Invalid weight! Please enter a value between 1 and 500 kg.")

    elif height <= 0 or height > 3:
        print("Invalid height! Please enter a value between 0.5 and 3 meters.")

    else:
        # BMI Calculation
        bmi = calculate_bmi(weight, height)

        # BMI Category
        category = bmi_category(bmi)

        # Display Result
        print("\n===== BMI Result =====")
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")
