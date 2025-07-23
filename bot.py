import asyncio
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
from downloader import download_video
from database import db
import keepalive
import json
import os

if not os.path.exists("downloads"):
    os.makedirs("downloads")

with open("config.json") as f:
    config = json.load(f)

BOT_TOKEN = config['bot_token']
ADMIN_IDS = config['admin_ids']
LOG_CHANNEL_ID = config['log_channel_id']

queue = asyncio.Queue()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is online.\nSend a video link!")

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    allow_all = db.get_setting("allow_all") == "true"
    if user_id not in db.get_users() and not allow_all:
        return await update.message.reply_text("❌ You are not approved.")
    url = update.message.text.strip()
    await update.message.reply_text(f"📎 Got link: {url}\n(This is a placeholder handler)")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))

    # Keepalive Flask for Replit/Render
    import threading
    threading.Thread(target=keepalive.run).start()

    app.run_polling()

if __name__ == "__main__":
    main()
