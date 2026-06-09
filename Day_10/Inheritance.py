class Staff:
  def __init__(self, name, basic_salary):
    self.name = name
    self.basic_salary = basic_salary
  def display(self):
    print(f"Name: {self.name}")
    print(f"Basic Salary: Rs. {self.basic_salary}")

class Professor(Staff):
  def __init__(self, name, basic_salary, research_allowance):
    super().__init__(name, basic_salary)
    self.research_allowance = research_allowance
  def calculate_salary(self):
    return self.basic_salary + self.research_allowance  

class LabAssistant(Staff):
  def __init__(self, name, basic_salary, lab_allowance):
    super().__init__(name, basic_salary)
    self.lab_allowance = lab_allowance
  def calculate_salary(self):
    return self.basic_salary + self.lab_allowance
  
prof = Professor("Dr. Sharma", 70000, 12000)
lab = LabAssistant("Ravi", 30000, 5000)
prof.display()
print("Total Salary: ",prof.calculate_salary())
print()
lab.display()
print("Total Salary: ",lab.calculate_salary())