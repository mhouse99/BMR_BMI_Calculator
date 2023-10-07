def get_weight():
    """Converts pounds to kilograms if needed and returns it."""
    weight_unit = input("What is your weight unit: lbs/kg: ").lower()
    while weight_unit != 'lbs' and weight_unit != 'kg':     # Makes sure the user has entered the correct input
        print("Invalid input. Please enter either 'lbs' or 'kg'.")
        weight_unit = input("What is your weight unit: lbs/kg: ").lower()
    weight = float(input("What is your weight: "))  # Input weight in chosen unit lbs or kg
    if weight_unit == 'lbs':
        convert_kg = input("Convert weight from lbs to kg?: yes/no: ").lower()  # If user only knows weight in lbs,
        # will be given the option to convert to kg
        if convert_kg == 'yes':
            weight = weight * 0.453592  # Converts weight from pounds to kilograms
    return weight


def get_height():
    """Converts height from feet'inches format to inches or centimeters and returns it."""
    height_unit = input("What is your height unit: inches/cm: ").lower()
    while height_unit != 'inches' and height_unit != 'cm':  # Makes sure the user has entered the correct input
        print("Invalid input. Please enter either 'inches' or 'cm'.")
        height_unit = input("what is your height unit: inches/cm: ")
    feet = int(input("What is your height (feet): "))
    inches = float(input("What is your height (inches): "))
    height = feet * 12 + inches     # Converts feet and inches to only inches
    if height_unit == 'cm':
        height = height * 2.54  # Convert height from inches to cm
    return height


def get_age():
    """Returns the inputted age."""
    age = float(input("What is your age: "))
    return age


def get_exercise_level():
    """Returns the level of activity selected."""
    exercise_level = input("Sedentary (little to no exercise): (A)\n"
                           "Lightly active (1-3 days a week of exercise): (B)\n"
                           "Moderately active (3-5 days a week of exercise): (C)\n"
                           "Very active (6-7 days a week of exercise): (D)\n"
                           "Pick A/B/C/D: ").upper()
    return exercise_level


def calculate_cals(exercise_level, bmr_result):
    """Returns the amount of calories based on exercise level and the result of Basal Metabolic Rate (BMR)."""
    if exercise_level == "A":
        cals = bmr_result * 1.2
    elif exercise_level == "B":
        cals = bmr_result * 1.375
    elif exercise_level == "C":
        cals = bmr_result * 1.55
    elif exercise_level == "D":
        cals = bmr_result * 1.725
    else:
        print("Unable to calculate.")
    return cals


def check_bmi(bmi):
    """Returns Body Mass Index (BMI)."""
    if bmi <= 18.5:
        print(f"Your BMI is {bmi:.2f}:\n and you are underweight.")
    elif 18.5 <= bmi <= 24.9:
        print(f"Your BMI is {bmi:.2f}:\n and you are a normal weight.")
    elif 25 <= bmi <= 29.9:
        print(f"Your BMI is {bmi:.2f}:\n and you are overweight.")
    elif bmi >= 30:
        print(f"Your BMI is {bmi:.2f}:\n and you are obese.")
    else:
        print("Unable to Calculate.")
    return bmi


def bmi_bmr():
    """Calculates BMR or BMI based on information inputted."""
    name = input("What is your name? ")
    bmi_bmr = input("Do you want to calculate: BMI/BMR: ").upper()
    while bmi_bmr != "BMI" and bmi_bmr != "BMR":    # Makes sure user has entered correct input
        print("Invalid input. Please enter either 'BMI' or 'BMR'.")
        bmi_bmr = input("Do you want to calculate: BMI/BMR? ").upper()

    gen = input("What is your gender: F/M: ").upper()
    while gen != "F" and gen != "M":    # Makes sure user has entered the correct input
        print("Invalid input. Please enter either 'F' or 'M'.")
        gen = input("What is your gender: F/M: ").upper()

    met_imp = input("What do you prefer: Metric/Imperial: ")
    while met_imp != "Metric" and met_imp != "Imperial":    # Makes sure user has entered the correct input
        print("Invalid input. Please enter 'Metric' or 'Imperial'.")
        met_imp = input("What do you prefer: Metric or Imperial: ")

    if met_imp == "Imperial" and gen == "F" and bmi_bmr == "BMR":   # If user has entered "Imperial", "F", and "BMR";
        # program will continue and calculate BMR
        weight = get_weight()
        height = get_height()
        age = get_age()
        exercise_level = get_exercise_level()
        bmr_result = 655.4 + (4.35 * weight) + (4.7 * height) - (4.676 * age)  # Produces your BMR (Female) so that
        # amount of calories needed can be calculated
        cals = calculate_cals(exercise_level, bmr_result)
        print(f"{name}, your BMR is {bmr_result:.2f} and you will need {cals:.2f} calories per day.")
    elif met_imp == "Imperial" and gen == "M" and bmi_bmr == "BMR":    # If user has entered "Imperial", "M", and
        # "BMR"; program will continue and calculate BMR
        weight = get_weight()
        height = get_height()
        age = get_age()
        exercise_level = get_exercise_level()
        bmr_result = 66.47 + (6.24 * weight) + (12.7 * height) - (6.755 * age)  # Produces your BMR (Male) so that
        # amount of calories needed can be calculated
        cals = calculate_cals(exercise_level, bmr_result)
        print(f"{name}, your BMR is {bmr_result:.2f} and you will need {cals:.2f} calories per day.")
    if met_imp == "Metric" and gen == "F" and bmi_bmr == "BMR":     # If user has entered "Metric", "F", and "BMR";
        # the program will continue and calculate BMR
        weight = get_weight()
        height = get_height()
        age = get_age()
        exercise_level = get_exercise_level()
        bmr_result = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)  # Produces your BMR (Female) so
        # that amount of calories needed can be calculated
        cals = calculate_cals(exercise_level, bmr_result)
        print(f"{name}, your BMR is {bmr_result:.2f} and you will need {cals:.2f} calories per day.")
    elif met_imp == "Metric" and gen == "M" and bmi_bmr == "BMR":   # If user has entered "Metric", "M", and "BMR";
        # the program will continue and calculate BMR
        weight = get_weight()
        height = get_height()
        age = get_age()
        exercise_level = get_exercise_level()
        bmr_result = 66.5 + (13.397 * weight) + (4.799 * height) - (5.677 * age)  # Produces your BMR (Male) so
        # that amount of calories needed can be calculated
        cals = calculate_cals(exercise_level, bmr_result)
        print(f"{name}, your BMR is {bmr_result:.2f} and you will need {cals:.2f} calories per day.")

    if bmi_bmr == "BMI" and met_imp == "Imperial":  # If user inputs "BMI" and "Imperial"; program will continue to
        # calculate BMI
        weight = get_weight()
        height = get_height()
        bmi = (weight / (height ** 2)) * 703  # Imperial system conversion to calculate BMI
        check_bmi(bmi)
    if bmi_bmr == "BMI" and met_imp == "Metric":    # If user inputs "BMI" and "Metric"; program will continue to
        # calculate BMI
        weight = get_weight()
        height = get_height()
        bmi = weight / (height / 100) ** 2  # Metric system conversion to calculate BMI
        check_bmi(bmi)


bmi_bmr()