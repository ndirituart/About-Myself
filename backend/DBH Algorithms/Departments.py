# Define the departments and their proportions
departments = {
    'hr': 0.2,
    'marketing': 0.1,
    'finance': 0.1,
    'production': 0.3,
    'research': 0.05,
    'customer_service': 0.25
}

# Get the number of employees

number_of_employees = int(input("How many employees do you have?: "))
#Since research team is optional we can ask if company needs them really
#Few companies like Pharmaceuticals need researchers majority don't

# Ask if the company needs research employees
research_employees_needed = input("Do you need research employees? (Y/N): ").strip().upper()

# Calculate the number of employees in each department
def calculate_department_employees(number_of_employees, research_needed):
    if research_needed == 'N':
        departments['production'] += departments['research']
        departments['research'] = 0
    else:
        departments['research'] = research_employees_needed
    HR_employees = 0.2 * number_of_employees
    Marketing_employees = 0.1 * number_of_employees
    Finance_employees = 0.1 * number_of_employees
    Production_employees = 0.3 * number_of_employees
    Research_employees = 0
    Research_employees_needed = 0.05 * number_of_employees
    Customer_service_employees = 0.25 * number_of_employees

    print(f"HR employees: {HR_employees}")
    print(f"Marketing employees: {Marketing_employees}")
    print(f"Finance employees: {Finance_employees}")
    print(f"Production employees: {Production_employees}")
    print(f"Research employees: {Research_employees}")
    print(f"Research employees needed: {Research_employees_needed}")
    print(f"Customer service employees: {Customer_service_employees}")

# Call the function to calculate and print the number of employees in each department
calculate_department_employees(number_of_employees, research_employees_needed)
