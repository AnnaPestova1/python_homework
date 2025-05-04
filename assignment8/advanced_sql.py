import sqlite3
# Task 1: Complex JOINs with Aggregation
# I know it is better to use:
# with sqlite3.connect("../db/lesson.db") as conn:
# but assignment says Within the assignment8 folder, create advanced_sql.py. 
# This should open the database, issue the SQL statement, print out the result, and close the database.

# so I am opening and close db instead

conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()
'''
Find the total price of each of the first 5 orders.  
There are several steps.  You need to join the orders 
table with the line_items table and the products table.  
You need to GROUP_BY the order_id.  
You need to select the order_id and the 
SUM of the product price times the line_item quantity.  
Then, you ORDER BY order_id and LIMIT 5.  
You don't need a subquery.
Print out the order_id and the total price
for each of the rows returned.
'''

cursor.execute("""
SELECT o.order_id,
    SUM(p.price*l.quantity) AS total_price
FROM Orders AS o
JOIN Line_items AS l ON l.order_id = o.order_id
JOIN Products AS p ON p.product_id = l.product_id
GROUP BY o.order_id
ORDER BY o.order_id 
LIMIT 5
""")

print("task1", cursor.fetchall())

# Task 2: Understanding Subqueries
'''For each customer, find the average price of their orders.  
This can be done with a subquery. 
You compute the price of each order as in part 1, but you return 
the customer_id and the total_price.  That's the subquery. 
You need to return the total price using AS total_price, 
and you need to return the customer_id with AS customer_id_b, 
for reasons that will be clear in a moment.  In your main statement, 
you left join the customer table with the results of the subquery, 
using ON customer_id = customer_id_b.  You aliased the customer_id 
column in the subquery so that the column names wouldn't collide.  
Then group by customer_id -- this GROUP BY comes after the subquery -- and 
get the average of the total price of the customer orders.  
Return the customer name and the average_total_price.'''

cursor.execute("""
SELECT c.customer_id, c.customer_name, 
AVG(total_price) AS average_total_price
FROM Customers AS c
JOIN (
    SELECT o.customer_id AS customer_id_b, 
        SUM(p.price*l.quantity) AS total_price
    FROM Orders AS o
    JOIN Line_items AS l ON l.order_id = o.order_id
    JOIN Products AS p ON p.product_id = l.product_id
    GROUP BY o.order_id
) AS total_price ON c.customer_id = customer_id_b 
GROUP BY c.customer_id
""")

print("task2", cursor.fetchall())

# Task 3: An Insert Transaction Based on Data
'''You want to create a new order for the customer named Perez and Sons.  
The employee creating the order is Miranda Harris.  
The customer wants 10 of each of the 5 least expensive products.  
You first need to do a SELECT statement to retrieve the customer_id, another to retrieve 
the product_ids of the 5 least expensive products, and another to retrieve the employee_id.  
Then, you create the order record and the 5 line_item records comprising the order.  
You have to use the customer_id, employee_id, and product_id values you obtained from the 
SELECT statements. You have to use the order_id for the order record you created in the line_items 
records. The inserts must occur within the scope of one transaction. 
Then, using a SELECT with a JOIN, print out the list of line_item_ids for 
the order along with the quantity and product name for each.'''

customer_id = cursor.execute("SELECT customer_id FROM Customers WHERE customer_name='Perez and Sons'").fetchone()[0]
print("task3",customer_id)
product_ids = cursor.execute("SELECT product_id FROM Products ORDER BY price ASC LIMIT 5").fetchall()
print("task3",product_ids)
employee_id = cursor.execute("SELECT employee_id FROM Employees WHERE first_name='Miranda' AND last_name='Harris'").fetchone()[0]
print("task3",employee_id)

try:
    order_id = cursor.execute("INSERT INTO Orders (customer_id, employee_id) VALUES (?,?) RETURNING order_id", (customer_id,employee_id)).fetchone()[0]
    print("task3 order_id",order_id)
    for product_id in product_ids:
        cursor.execute("INSERT INTO Line_items (order_id, product_id, quantity) VALUES (?,?,?)",(order_id,product_id[0],10))
except Exception as e:
    conn.rollback()  # Rollback transaction if there's an error
    print("Error:", e)
    
cursor.execute("""
SELECT l.line_item_id, p.product_name, l.quantity
FROM Line_items AS l
JOIN Products AS p ON p.product_id = l.product_id
WHERE l.order_id=?;
""",(order_id,))
print("task3 new orders", cursor.fetchall())

# Task 4: Aggregation with HAVING
'''Find all employees associated with more than 5 orders.  
You want the first_name, the last_name, and the count of orders.  
You need to do a JOIN on the employees and orders tables, and then use 
GROUP BY, COUNT, and HAVING.'''

cursor.execute("""
SELECT e.first_name, e.last_name, COUNT(o.order_id)
FROM Employees AS e
JOIN Orders AS o ON o.employee_id = e.employee_id
GROUP BY e.employee_id
HAVING COUNT(o.order_id);
""")
print("task4", cursor.fetchall())
conn.close()