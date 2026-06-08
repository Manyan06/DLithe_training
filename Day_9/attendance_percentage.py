import re
class Solution:
  def evaluate_Employee(self, emp_id, name, attendance, project_completion):
    if not re.match(r"^EMP\d{3,5}$",emp_id):
      return "Invalid Employee ID"
    if not re.match(r"^[A-Za-z ]+$", name):
      return "Invalid Employee Name"
    if attendance < 0 or attendance > 100:
      return "Invalid Ateendace Percaentage"
    if project_completion < 0 or project_completion > 100:
      return "Invalid Project Completion Percentage"
    score = (attendance * 0.4) + (project_completion * 0.6)
    if score >= 90:
      return "Excellent"
    elif score >= 75:
      return "Good"
    elif score >= 60:
      return "Average"
    else:
      return "Needs Improvement"
    
#Input
emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
attendance = float(input("Attendance percentage: "))
project_completion = float(input("Project completion percentage: "))

obj = Solution()
result = obj.evaluate_Employee(
  emp_id, 
  name, 
  attendance, 
  project_completion
)
print("\nEmployee rating: ", result)