def calculate_employees_needed(number_of_employees, individual_ROI, total_ROI):
    number_of_employees = int(number_of_employees)
    individual_ROI = int(individual_ROI)
    total_ROI = int(total_ROI)  # in a month
    daily_ROI = float(total_ROI) / 30  # how much are we targeting per day

    # Calculating the total available ROI with current employees
    total_available_ROI = individual_ROI * number_of_employees

    # Calculating the number of employees needed
    if total_available_ROI >= daily_ROI:
        number_of_employees_needed = 0
        message = "You do not need additional employees to meet your target profit."
    else:
        number_of_employees_needed = (daily_ROI - total_available_ROI) / individual_ROI
        number_of_employees_needed = int(number_of_employees_needed) + 1  # Round up to ensure the target is met
        message = f"You need {number_of_employees_needed} additional employees to meet your target profit."

    return {
        'number_of_employees_needed': number_of_employees_needed,
        'message': message
    }
