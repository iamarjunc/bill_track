from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

# Load .env file
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Encode password (VERY IMPORTANT if it has @ or #)
PASSWORD = quote_plus(PASSWORD)

# Build connection string
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

print("Connecting to:", HOST)  # debug

# Create engine
engine = create_engine(DATABASE_URL)

# Test connection
try:
    with engine.connect() as connection:
        print("✅ Connection successful!")
except Exception as e:
        print("❌ Failed to connect:", e)