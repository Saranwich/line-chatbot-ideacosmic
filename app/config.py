import os
from dotenv import load_dotenv

load_dotenv()

LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL :
    print("DATABASE_URL NOT FOUND in .env")