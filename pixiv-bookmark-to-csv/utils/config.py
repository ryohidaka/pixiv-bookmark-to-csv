import os
from dotenv import load_dotenv

# Load .env file and reflect environment variables.
load_dotenv()

# Get environment variables.
REFRESH_TOKEN = os.environ.get("REFRESH_TOKEN")
USER_ID = os.environ.get("USER_ID")
