import sqlite3
import matplotlib.pyplot as plt

# 1. Create/connect to database file
conn = sqlite3.connect('sales_data.db')  # permanent file
cursor = conn.cursor()

#table create
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    quantity INTEGER,
    price REAL
)
''')

sales_data = [
    ('Pen', 10, 5.0),
    ('Notebook', 5, 20.0),
    ('Pencil', 15, 2.0),
    ('Textbook', 20, 30.0),
    ('Water bottles', 45, 20.0),
    ('Shoes', 15, 200.0),
    ('Colour pencil', 10, 10.0),
    ('Scissors', 10, 40.0),
    ('Folders and files', 15, 20.0),
    ('Desk organiser', 10, 50.0),
    ('Sheet protector', 45, 20.0),
    ('Calculator', 15, 70.0),
    ('Diaries', 10, 50.0),
    ('Tape', 52, 20.0),
    ('Envelopes', 15, 5.0),
    ('Markers', 10, 20.0),
    ('Gift Bags', 15, 100.0),
    ('Whiteboard', 15,500.0),
]

# Insert data only if table is empty
cursor.execute('SELECT COUNT(*) FROM sales')
if cursor.fetchone()[0] == 0:
    cursor.executemany('INSERT INTO sales VALUES (?, ?, ?)', sales_data)
    conn.commit()

# 4. Fetch total quantity & revenue
cursor.execute('''
SELECT product, SUM(quantity) as total_qty, SUM(quantity * price) as total_revenue
FROM sales
GROUP BY product
''')
results = cursor.fetchall()

query = """ 
SELECT 
    product, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product 
ORDER BY revenue DESC 
LIMIT 3
"""
print = query

# 5. Print results
print("Product-wise Sales Summary:")
for row in results:
    print(f"➡ {row[0]} - Quantity: {row[1]}, Revenue: ₹{row[2]}")

# 6. Draw bar chart
products = [row[0] for row in results]
revenues = [row[2] for row in results]

plt.bar(products, revenues, color='skyblue')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.show()

# 7. Close connection
conn.close()