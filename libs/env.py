from dotenv import load_dotenv
import os

load_dotenv()

def load(key):
    return os.environ.get(key)