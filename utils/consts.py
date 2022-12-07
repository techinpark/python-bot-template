import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = ""
APP_LOGO_IMAGE_URL = ""
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
