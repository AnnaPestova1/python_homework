import pandas as pd

"""Task 1"""
# Create a DataFrame from a dictionary:
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data)
print("\ntask1_data_frame\n", task1_data_frame)

# Add a new column
task1_with_salary = task1_data_frame.copy()

task1_with_salary["Salary"] = [70000, 80000, 90000]
print("\ntask1_with_salary\n", task1_with_salary)

# Modify an existing column
task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"]+1
print("\ntask1_older\n", task1_older)

# Save the DataFrame as a CSV file
task1_older.to_csv("employees.csv", index=False)

"""Task 2"""
# Read data from a CSV file
task2_employees = pd.read_csv("employees.csv")
print("\ntask2_employees\n", task2_employees)

# Read data from a JSON file
json_employees = pd.read_json("additional_employees.json")
print("\njson_employees\n", json_employees)

# Combine DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\nmore_employees\n", more_employees)

"""Task 3"""
# Use the head() method
first_three = more_employees.head(3)
print("\nfirst_three\n", first_three)

# Use the tail() method
last_two = more_employees.tail(2)
print("\nlast_two\n", last_two)

# Get the shape of a DataFrame
employee_shape = more_employees.shape
print("\nemployee_shape\n", employee_shape)

# Use the info() method
print('\nmore_employees.info\n', more_employees.info())


"""Task 4"""
# Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data
dirty_data = pd.read_csv("dirty_data.csv")
print("\ndirty_data\n", dirty_data)

clean_data = dirty_data.copy()
print("\nclean_data\n", clean_data)

# Remove any duplicate rows from the DataFrame
clean_data = clean_data.drop_duplicates()
print("\nclean_data drop_duplicates\n", clean_data)

# Convert Age to numeric and handle missing values
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print("\nclean_data Convert Age to numeric\n", clean_data)

# Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print("\nclean_data Salary to numeric\n", clean_data)

clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], pd.NA)
print("\nclean_data replace known placeholders (unknown, n/a) with NaN\n", clean_data)

# Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the 
mean_age = clean_data["Age"].mean()
clean_data["Age"] = clean_data["Age"].fillna(mean_age)
median_salary = clean_data["Salary"].median()
clean_data["Salary"] = clean_data["Salary"].fillna(median_salary)
print("\nclean_data Fill missing numeric values \n", clean_data)

# Convert Hire Date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
print("\nclean_data onvert Hire Date to datetime\n", clean_data)

# Strip extra whitespace and standardize Name and Department as uppercase
clean_data["Department"] = clean_data["Department"].str.strip()
clean_data["Department"] = clean_data["Department"].str.upper()
clean_data["Name"] = clean_data["Name"].str.strip()
clean_data["Name"] = clean_data["Name"].str.upper()
print("\nclean_data Strip extra whitespace and uppercase\n", clean_data)
