class Employee:
  def __init__(self, emp_id, name, monthly_salary):
    self.emp_id = emp_id
    self.name = name
    self.monthly_salary = monthly_salary

  def annual_salary(self):
    return self.monthly_salary * 12
  
  def calculate_bonus(self, percentage):
    return self.annual_salary() * (percentage / 100)
  
  def display(self):
    print("Employee ID: ", self.emp_id)
    print("Name: ", self.name)
    print("Monthly Salary: ", self.monthly_salary)
    print("Annual Salary: ", self.annual_salary())

emp = Employee(101, "Rahul", 50000)
emp.display()
bonus = emp.calculate_bonus(10)
print("Bonus Amount: ", bonus)