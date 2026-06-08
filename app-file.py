import pandas as pd
import numpy as np
import mysql.connector



def connect_to_db():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mysql_operations_dashboard")

db = connect_to_db()
cursor = db.cursor(dictionary=True)

# cursor.execute("SELECT COUNT(*) AS total_suppliers FROM suppliers;")
# result = cursor.fetchone()
# print(result['total_suppliers'])


#Doing Automations for Queries
def get_basic_info(cursor):

    queries = {

        "Total Suppliers": """
        SELECT COUNT(*) AS count
        FROM suppliers
        """,

        "Total Products": """
        SELECT COUNT(*) AS count
        FROM products
        """,

        "Total Categories Dealing": """
        SELECT COUNT(DISTINCT category) AS count
        FROM products
        """,

        "Total Sale Value (Last 3 Months)": """
        SELECT ROUND(
            SUM(ABS(se.change_quantity) * p.price),
            2
        ) AS total_sale
        FROM stock_entries se
        JOIN products p
            ON se.product_id = p.product_id
        WHERE se.change_type = 'Sale'
          AND se.entry_date >= (
                SELECT DATE_SUB(
                    MAX(entry_date),
                    INTERVAL 3 MONTH
                )
                FROM stock_entries
          )
        """,

        "Total Restock Value (Last 3 Months)": """
        SELECT ROUND(
            SUM(se.change_quantity * p.price),
            2
        ) AS total_restock
        FROM stock_entries se
        JOIN products p
            ON se.product_id = p.product_id
        WHERE se.change_type = 'Restock'
          AND se.entry_date >= (
                SELECT DATE_SUB(
                    MAX(entry_date),
                    INTERVAL 3 MONTH
                )
                FROM stock_entries
          )
        """,

        "Below Reorder & No Pending Reorders": """
        SELECT COUNT(*) AS below_reorder
        FROM products p
        WHERE p.stock_quantity < p.reorder_level
          AND p.product_id NOT IN (
                SELECT DISTINCT product_id
                FROM reorders
                WHERE status = 'Pending'
          )
        """
    }

    result = {}

    for label, query in queries.items():
        cursor.execute(query)

        row = cursor.fetchone()

        result[label] = list(row.values())[0]

    return result

#Returns a dictionary with the following keys and their corresponding values:
# - "Total Suppliers": Total number of suppliers in the database.
# result = get_basic_info(cursor)
# print(result)

