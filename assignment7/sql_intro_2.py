import pandas as pd
import sqlite3
# **Task 5: Read Data into a DataFrame**
with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = "SELECT l.line_item_id, l.quantity, p.product_id, p.product_name, p.price FROM line_items l JOIN products p ON l.product_id = p.product_id"
    df = pd.read_sql_query(sql_statement, conn)
    print("\ndf first 5 lines\n", df.head())
    
    df['total'] = df['quantity'] * df['price']
    print("\ndf first 5 lines\n", df.head())

    resulting_df = df.groupby("product_id").agg({"line_item_id":'count',"total":'sum', "product_name":'first'}).reset_index()
    print("\nresulting_df first 5 lines\n", resulting_df.head())

    sorted = resulting_df.sort_values(by='product_name', ignore_index=True)
    print("\nsorted first 5 lines\n", sorted.head())

    sorted.to_csv("order_summary.csv", index=False)
    print("DataFrame saved to order_summary.csv")






