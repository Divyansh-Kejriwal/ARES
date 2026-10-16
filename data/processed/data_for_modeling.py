import os
import mysql.connector
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    database= os.getenv("MYSQL_DATABASE")
)

cursor = connection.cursor()

table = "case_info"

query = f"SELECT * FROM {table}"

df = pd.read_sql(query, connection)

print("Rows and Column: ", df.shape)
print(df.head())
print(df.dtypes)