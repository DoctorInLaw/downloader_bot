import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env if exists (local dev)

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x]
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", "-100123456789"))

# Optional defaults
DEFAULT_PROGRESS_CAPTION = "⬇️ Downloading..."
DEFAULT_FILE_CAPTION = "✅ Here’s your file!"
