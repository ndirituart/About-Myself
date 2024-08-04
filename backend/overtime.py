def calculate_overtime_needed(number_of_employees, individual_work_hours, overtime_allowed, overtime_hours, total_hours):
    # Calculating the total available work hours with current employees (regular hours + overtime)
    regular_working_hours_per_week = individual_work_hours * 5 * number_of_employees
    overtime_working_hours_per_week = overtime_hours * overtime_allowed * number_of_employees
    total_working_hours_per_week = regular_working_hours_per_week + overtime_working_hours_per_week

    # Calculating the number of weeks needed to complete the total hours of work
    weeks_needed = total_hours / total_working_hours_per_week

    # Calculating the number of employees needed
    if weeks_needed <= 1:
        number_of_employees_needed = 0
        message = "You do not need additional employees to finish this task within a week."
    else:
        additional_hours_needed = total_hours - total_working_hours_per_week
        additional_employees_needed = additional_hours_needed / (individual_work_hours * 5 + overtime_hours * overtime_allowed)
        number_of_employees_needed = int(additional_employees_needed) + 1  # Round up to ensure the workload is covered
        message = f"You need {number_of_employees_needed} additional employees to finish this task."

    return {
        'number_of_employees_needed': number_of_employees_needed,
        'message': message
    }
