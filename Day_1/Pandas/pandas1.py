import pandas as pd
employees = pd.DataFrame({
  'EmpID':[1,2,3,4],
  'Name' :['Alice','Bob', 'Charlie','David'],
  'DeptID' : [101,102,101,103]
})

#Departments dataset
departments = pd.DataFrame({
  'DeptID' : [101,102,103],
  'Department' :['HR', 'Finance','IT']
})

#merged on DeptID
merged_df = pd.merge(employees,departments,on = 'DeptID')
print("Merged DataFrame: \n", merged_df)