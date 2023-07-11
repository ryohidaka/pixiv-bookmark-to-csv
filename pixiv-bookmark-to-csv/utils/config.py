import os
import argparse
from dotenv import load_dotenv

# Load .env file and reflect environment variables.
load_dotenv()

# Get environment variables.
REFRESH_TOKEN = os.environ.get("REFRESH_TOKEN")
USER_ID = os.environ.get("USER_ID")


def get_args():
    """
    Get the type of target to be retrieved from the command-line argument.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--restrict", default="public")
    parser.add_argument("--mode", default="diff")
    args = parser.parse_args()

    return {
        "restrict": args.restrict,
        "mode": args.mode,
    }
