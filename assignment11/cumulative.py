import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.data as pldata

with sqlite3.connect('../db/lesson.db') as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    query = """
    SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
    """

    df = pd.read_sql_query(query, conn)

    # --- Task 2 ---
    #def cumulative(row):
    #    totals_above = employee_results['total_price'][0:row.name+1]
    #    return totals_above.sum()

    #employee_results['cumulative'] = employee_results.apply(cumulative, axis=1)

    # accomplishes the same result as the above
    df['cumulative'] = df['total_price'].cumsum()

    df.plot(x='cumulative', y='order_id', kind='line', color='green', title='Cumulative Revenue by Order ID')
    plt.show()

    # --- Task 3 ---
    df3 = pldata.wind(return_type='pandas')

    print(df3.head(10))
    print(df3.tail(10))

    df3['strength'] = df3['strength'].replace(r'[-+].*', '', regex=True).astype(float)

    fig = px.scatter(df3, x='strength', y='frequency', color='direction', title='Wind Strength vs Frequency by Direction', hover_data=['strength', 'frequency'])
    fig.write_html('wind.html', auto_open=True)