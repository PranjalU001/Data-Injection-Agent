import os
from dotenv import load_dotenv
import snowflake.connector

# ✅ Load .env variables
load_dotenv()

# ✅ Global connection (one-time)
conn = None

def get_connection():
    global conn

    if conn is None:
        conn = snowflake.connector.connect(
            user=os.getenv("SNOW_USER"),
            password=os.getenv("SNOW_PASSWORD"),
            account=os.getenv("SNOW_ACCOUNT"),
            warehouse=os.getenv("SNOW_WAREHOUSE"),
            database=os.getenv("SNOW_DATABASE"),
            schema=os.getenv("SNOW_SCHEMA")
        )

        print("✅ Snowflake connection established (ONLY ONCE)")

    return conn