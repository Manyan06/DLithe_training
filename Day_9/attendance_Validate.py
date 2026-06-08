import re
def validate_attendance(emp_id, check_in, check_out):
  #Employee ID Validation
  emp_pattern = r"^EMP\d+$"
  if not re.match(emp_pattern, emp_id):
    print("Invalid Employee ID! FORMAT: EMP101")
    return
  
  #Time Validation
  time_pattern = r"^([01]\d|2[0-3]):([0-5]\d)$"
  if not re.match(time_pattern, check_in):
    print("Invalid Check-In Time! Use HH:MM")
    return
  
  #Convert Time into minutes
  in_hour, in_min = map(int, check_in.split(":"))
  out_hour, out_min = map(int, check_out.split(":"))
  in_minutes = in_hour * 60 + in_min
  out_minutes = out_hour * 60 + out_min
  if out_minutes <= in_minutes:
    print("Check-Out time must be greater than Check-In time!")
    return
  working_hours = (out_minutes - in_minutes) / 60
  print("\nAttendance Record Valid")
  print("Employee ID: ",emp_id)
  print("Check-in-Time: ",check_in)
  print("Check-out-Time: ",check_out)
  print("Working Hours: ",working_hours)
  if working_hours < 0:
    print("Status: Half day")
  else:
    print("Status: Full day")

#Input
emp_id = input("Enter Employee ID: ")
check_in = input("Enter Check-In time(HH:MM): ")
check_out = input("Enter Check-Out time(HH:MM): ")
validate_attendance(emp_id, check_in, check_out)