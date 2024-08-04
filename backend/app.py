from flask import Flask, request, jsonify
from flask_cors import CORS

from hours import hourbased
from overtime import calculate_overtime_needed
from sales import calculate_employees_needed


app = Flask(__name__)

#Installing CORS to connect the GUI and the model 
CORS(app, resources={r"/calculate-hours": {"origins": "*"}})
@app.route('/calculate-hours', methods=['POST'])
def calculate():
    data = request.get_json()

    number_of_employees = data['number_of_employees']
    individual_work_hours = data['individual_work_hours']
    target_work_hours = data['target_work_hours']
    individual_work_days = data['individual_work_days']
    start_day = data['start_day']
    end_day = data['end_day']

    return hourbased(number_of_employees, individual_work_hours, target_work_hours, individual_work_days, start_day, end_day)

@app.route('/overtime', methods=['POST'])
def evaluate():
    data = request.get_json()

    number_of_employees=data['number_of_employees']
    individual_work_hours=data['individual_work_hours']
    overtime_allowed=data['overtime_allowed']
    overtime_hours=data['overtime_allowed']
    total_hours=data['total_hours']
    
    return calculate_overtime_needed(number_of_employees, individual_work_hours, overtime_allowed, overtime_hours, total_hours)
    
@app.route('/sales', methods=['POST'])
def calculate_employees():
    data = request.get_json()
    
    response = calculate_employees_needed(
        number_of_employees=data.get('number_of_employees'),
        individual_ROI=data.get('individual_ROI'),
        total_ROI=data.get('total_ROI')
    )

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)