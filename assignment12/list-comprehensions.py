import pandas as pd

df = pd.read_csv('../csv/employees.csv')
print('\ndf\n', df)

employee_names=[f"{row["first_name"]} {row["last_name"]}" for _, row in df.iterrows() ]
# row = next(df.iterrows())[1]

print('\nemployee_names\n', employee_names, len(employee_names))

employee_names_with_e = [name for name in employee_names if "e" in name.lower()]
print('\nemployee_names_with_e\n', employee_names_with_e, len(employee_names_with_e))
