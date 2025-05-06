import sqlite3
import pandas as pd

def fetch_data_from_sqlite(db_path, query): 
    # Create connection
    conn = sqlite3.connect(db_path)
    # Store query result in score 
    score = pd.read_sql_query(query, conn)
    # Close the connection
    conn.close()
    return score