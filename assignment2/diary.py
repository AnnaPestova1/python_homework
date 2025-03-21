import traceback
import datetime

def new_line(data):
    return data+"\n"

try:
    count = 0
    answer = str()
    with open("diary.txt", "a") as file:
        # diary struggle to have a data
        today = datetime.datetime.now()
        file.write(new_line(today.strftime("%x")))
        while answer != "done for now":
            if count == 0:
                answer = input("What happened today? ")
                # count help us to ask question "What happened today?" only once
                count += 1
                file.write(new_line(answer))
            # when you finish your description print "done for now" in input
            else:
                answer = input("What else? ")
                """ In the current code, we can omit count += 1 here because 
                 we only need it to prompt "What happened today?" the first time the loop starts."""
                # count += 1
                file.write(new_line(answer))
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