import os

DB_USERNAME = "your_username"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_NAME = "employee_db"

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
