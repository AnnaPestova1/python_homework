import pandas as pd
data = [{'Employee': 'Jones', 'Product': 'Widget', 'Region': 'West', 'Revenue': 9000}, \
{'Employee': 'Jones', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 4000}, \
{'Employee': 'Jones', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 11000}, \
{'Employee': 'Jones', 'Product': 'Widget', 'Region': 'East', 'Revenue': 4000}, \
{'Employee': 'Jones', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 5500}, \
{'Employee': 'Jones', 'Product': 'Doohickey', 'Region': 'East', 'Revenue': 2345}, \
{'Employee': 'Smith', 'Product': 'Widget', 'Region': 'West', 'Revenue': 9007}, \
{'Employee': 'Smith', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 40003}, \
{'Employee': 'Smith', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 110012}, \
{'Employee': 'Smith', 'Product': 'Widget', 'Region': 'East', 'Revenue': 9002}, \
{'Employee': 'Smith', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 15500}, \
{'Employee': 'Garcia', 'Product': 'Widget', 'Region': 'West', 'Revenue': 6007}, \
{'Employee': 'Garcia', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 42003}, \
{'Employee': 'Garcia', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 160012}, \
{'Employee': 'Garcia', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 16500}, \
{'Employee': 'Garcia', 'Product': 'Doohickey', 'Region': 'East', 'Revenue': 2458}]
sales = pd.DataFrame(data)
print("\nsales\n", sales)

# Pivot Tables

sales_pivot1 = pd.pivot_table(sales,index=['Product','Region'],values=['Revenue'],aggfunc='sum',fill_value=0)
print("\nsales_pivot1\n", sales_pivot1)

# This creates a two level index to show sales by product and region. The revenue values are summed for each product and region.
sales_pivot2 = pd.pivot_table(sales,index='Product',values='Revenue',columns='Region', aggfunc='sum',fill_value=0)
print("\nsales_pivot2\n", sales_pivot2)

# The result here is similar, but instead of a two level index, you have columns to give sales by region.
sales_pivot3 = pd.pivot_table(sales,index='Product',values='Revenue',columns=['Region','Employee'], aggfunc='sum',fill_value=0)
print("/nsales_pivot3/n", sales_pivot3)
# By adding the employee column, you get these revenue numbers broken down by employee.  The fill value is used when there is no corresponding entry.

# Using apply()

sales_pivot2['Total'] = sales_pivot2['East'] + sales_pivot2['West'] # adding two columns to make a new one
print("\nsales_pivot2\n", sales_pivot2)

per_employee_sales=sales.groupby('Employee').agg({'Revenue':'sum'})
per_employee_sales['Commission Percentage'] = [0.12, 0.09, 0.1]
per_employee_sales['Commission'] = per_employee_sales['Revenue'] * per_employee_sales['Commission Percentage']
print("\nper_employee_sales\n", per_employee_sales)

per_employee_sales=sales.groupby('Employee').agg({'Revenue':'sum'})
per_employee_sales['Commission Plan'] = ['A', 'A', 'B']

def calculate_commission(row):
    if row['Revenue'] < 10000:
        return 0
    if row['Commission Plan'] == 'A':
        return 1000 + 0.05 * (row['Revenue'] - 10000)
    else:
        return 1400 + 0.04 * (row['Revenue'] - 10000)

per_employee_sales['Commission'] = per_employee_sales.apply(calculate_commission, axis=1)
print("\nper_employee_sales\n", per_employee_sales)

# Using isnull(), dropna() and fillna()

# Sample DataFrame with missing values
data2 = {'Name': ['Alice', 'Bob', None, 'David'],
        'Age': [24, 27, 22, None],
        'Score': [85, None, 88, 76]}
df2 = pd.DataFrame(data2)

# Find rows with missing data
# The axis=1 is needed to specify rows.
df_missing = df2[df2.isnull().any(axis=1)]
print("\ndf_missing\n", df_missing)

# Remove rows with missing data
df_dropped = df2.dropna()
print("\ndf_dropped\n", df_dropped)

# Replace missing data with default values
df_filled = df2.fillna({'Age': 0, 'Score': df2['Score'].mean()})
print("\ndf_filled\n", df_filled)

# Data Transformation

# Sample DataFrame with mixed data types
data3 = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': ['24', '27', '22'],
        'JoinDate': ['2023-01-15', '2022-12-20', '2023-03-01']}
df3 = pd.DataFrame(data3)

# Convert 'Age' column to integers
df3['Age'] = df3['Age'].astype(int)

# Convert 'JoinDate' column to datetime
df3['JoinDate'] = pd.to_datetime(df3['JoinDate'])

print("\ndf3.dtypes\n", df3.dtypes)  # Verify data types
print("\ndf3\n", df3)

# In addition you can use the Series map() method to change items in a column.
data4 = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Location': ['LA', 'LA', 'NY'],
        'JoinDate': ['2023-01-15', '2022-12-20', '2023-03-01']}
df4 = pd.DataFrame(data4)

# Convert 'Location' abbreviations into full names

df4['Location'] = df4['Location'].map({'LA': 'Los Angeles', 'NY': "New York"})
print("\ndf4\n", df4)

# The problem with the code above is that if the value in the 'Location' column is not either 'LA' or 'NY', it is converted to NaN.  Suppose you want to preserve the existing value in this case. You'd use the replace() method instead:

df4['Location'] = df4['Location'].replace({'LA': 'Los Angeles', 'NY': "New York"})
print("\ndf4\n", df4)

data5 = {'Name': ['Tom', 'Dick', 'Harry', 'Mary'], 'Phone': [3212347890, '(212)555-8888', '752-9103','8659134568']}
df5 = pd.DataFrame(data5)
df5['Correct Phone'] = df5['Phone'].astype(str)

def fix_phone(phone):
    if phone.isnumeric():
        out_string = phone
    else:
        out_string = ''
        for c in phone:
            if c in '0123456789':
                out_string += c
    if len(out_string) == 10:
        return out_string
    return None
    
df5['Correct Phone'] = df5['Correct Phone'].map(fix_phone)
print("\ndf5\n", df5)

# Finally we can use built in numpy functions in order to change all of the data in a data frame by following a function
data6 = {'Name': ['Alice', 'Bob', 'Charlie'],
	'Age': [20, 22, 43]}

df6 = pd.DataFrame(data6)

# Increase the age by 1 as a new year has passed
df6['Age'] += 1
print("\ndf6\n", df6)

# For Data Discretization we have to use the more complicated pandas.cut() function. This will allow us to automatically split data into a series of equal sized bins.
data7 = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Location': ['LA', 'LA', 'NY'],
        'Grade': [78, 40, 85]}
df7 = pd.DataFrame(data7)

# Convert grade into three catagories, "bad", "okay", "great"

df7['Grade'] = pd.cut(df7['Grade'], 3, labels = ["bad", "okay", "great"])
print("\ndf7\n", df7)