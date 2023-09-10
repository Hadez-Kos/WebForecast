import os
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("secret_key")
