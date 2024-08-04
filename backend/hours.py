
from datetime import datetime
from flask import jsonify
def hourbased(number_of_employees, individual_work_hours, target_work_hours, individual_work_days, start_day_str, end_day_str):
    # Convert start_day_str and end_day_str to datetime objects
    #Year is 2 digits, 24 not 2024
    start_day = datetime.strptime(start_day_str, "%d/%m/%y").date()
    end_day = datetime.strptime(end_day_str, "%d/%m/%y").date()

    today = datetime.now().date()

    if start_day <= today:
        return jsonify({"error": "The start date must be after today."}), 400

    difference_in_days = (end_day - start_day).days

    if difference_in_days < 0:
        return jsonify({"error": "The end date must be after the start date."}), 400

    # Calculate total work hours needed
    total_work_hours_needed = difference_in_days * target_work_hours
    # Calculate the total available work hours
    total_available_hours = individual_work_hours * individual_work_days * 4 * number_of_employees
    # Calculating the number of employees needed
    if total_available_hours >= total_work_hours_needed:
        return jsonify({"message": "You do not need additional employees to finish this task."})
    else:
        number_of_employees_needed = (total_work_hours_needed - total_available_hours) / (individual_work_hours * individual_work_days *4)
        number_of_employees_needed = int(number_of_employees_needed) + 1  # Round up

        return jsonify({"message": f"You need {number_of_employees_needed} additional employees to finish this task."})

