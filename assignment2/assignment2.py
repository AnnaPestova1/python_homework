import csv
import traceback
import os
import custom_module
from datetime import datetime

def read_employees():
    employeesDict = {}
    employeeList = []
    try:
        with open("../csv/employees.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            count = 1
            for row in reader:
                if count == 1:
                    employeesDict["fields"] = row
                    count += 1
                else:
                    employeeList.append(row)
            employeesDict["rows"] = employeeList
        return employeesDict
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")


employees = read_employees()
print("employees", employees)

def column_index(field_name):
    return employees["fields"].index(field_name)

employee_id_column = column_index("employee_id")
print("employee_id_column", employee_id_column)

def first_name(row_number):
    index = column_index("first_name")
    # index vs number ambiguity: task says number (row) (index-1), test expects index
    # row_index = row_number-1
    # row = employees["rows"][row_index]
    row = employees["rows"][row_number]
    print("row", row)
    return row[index]

print("employees", employees)
print("first_name", first_name(2))

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

print("employee_find", employee_find(3))

def employee_find_2(employee_id):
    matches=list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

print("employee_find_2", employee_find_2(3))

def sort_by_last_name():
    employees["rows"].sort(key = lambda row: row[column_index("last_name")])
    return employees["rows"]
sort_by_last_name()
print(sort_by_last_name())
print("employees", employees)
print("first_name", first_name(2))

def employee_dict(row):
    new_dict={}
    for field in employees["fields"]:
        if(field == "employee_id"):
            continue
        else:
            new_dict[field] = row[column_index(field)]
    return new_dict

print(employee_dict(employees["rows"][0]))

def all_employees_dict():
    new_dict = {}
    for row in employees["rows"]:
        new_dict[row[column_index("employee_id")]] = employee_dict(row)
    return new_dict

print(all_employees_dict())

# do not forget print 'export THISVALUE=ABC' in the terminal where you are running tests
def get_this_value():
    return os.environ.get("THISVALUE")

print(get_this_value())

def set_that_secret(new_secret):
    return custom_module.set_secret(new_secret)

print("custom_module before run set_that_secret()", custom_module.secret)
set_that_secret("watermelon")
print("custom_module after run set_that_secret()", custom_module.secret)

def read_minutes():
    def convert_to_dict(name):
        min_dict = {}
        minutes_list=[]
        try:
            basepath = "../csv"
            file_name = name + ".csv"
            path = os.path.join(basepath, file_name)
            with open(path, "r") as csv_file:
                reader = csv.reader(csv_file)
                count = 1
                for row in reader:
                    if count == 1:
                        min_dict["fields"] = row
                        count += 1
                    else:
                        minutes_list.append(tuple(row))
                min_dict["rows"] = minutes_list
            return min_dict
        except Exception as e:
            trace_back = traceback.extract_tb(e.__traceback__)
            stack_trace = list()
            for trace in trace_back:
                stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")
    
    minutes1 = convert_to_dict("minutes1")
    minutes2 = convert_to_dict("minutes2")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1, minutes2)


def create_minutes_set():
    return set(minutes1["rows"]).union(set(minutes2["rows"]))


minutes_set = create_minutes_set()  
print("minutes_set", minutes_set)  


def create_minutes_list():
    minutes_list = list(minutes_set)
    result = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")) ,minutes_list))
    return result

minutes_list = create_minutes_list()
print("minutes_list", minutes_list)

def write_sorted_list():
    minutes_list.sort(key = lambda row: row[1])
    result = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")) ,minutes_list))
    try:
        with open("./minutes.csv", "w") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(minutes1["fields"])
            writer.writerows(result)
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    print("result", result)
    return result


write_sorted_list()