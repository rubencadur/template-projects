from os import getenv
from dotenv import load_dotenv, find_dotenv
from app import create_app

load_dotenv(find_dotenv())
app = create_app("development")

if __name__ == "__main__":
    app.run()