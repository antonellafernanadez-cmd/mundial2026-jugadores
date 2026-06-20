from dotenv import load_dotenv
import os
load_dotenv()

password=os.getenv("DB_PASSWORD")
user= os.getenv("DB_USER")
database= os.getenv("DB_NAME")
port= os.getenv("DB_PORT")
host= os.getenv("DB_HOST")

DATABASE_CONNECTION_URI= f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"