import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

with sqlite3.connect('../db/lesson.db') as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # --- Task 1 ---
    query = """
    SELECT last_name, SUM(price * quantity) AS revenue 
    FROM employees e 
    JOIN orders o ON e.employee_id = o.employee_id 
    JOIN line_items l ON o.order_id = l.order_id 
    JOIN products p ON l.product_id = p.product_id 
    GROUP BY e.employee_id;
    """

    employee_results = pd.read_sql_query(query, conn)

    employee_results.plot(x='last_name', y='revenue', kind='bar', color='skyblue', title='Revenue by Employee')
    plt.show()