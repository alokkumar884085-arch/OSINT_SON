import logging
import os
import requests
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Bot Token
BOT_TOKEN = "8804077517:AAGY_T6eit4xVG3ozlCuqsaQlpXNMuhRBhk"

# --- Flask Server (Render Sleep Mode Rokne ke liye) ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive and running!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()
# -----------------------------------------------------


# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "👋 **OSINT Pro Bot**\n\n"
        "Commands:\n"
        "🔍 /leak <number>\n"
        "🎮 /ff <uid>\n"
        "📱 /tg <query>\n"
    )
    await update.message.reply_text(welcome_message, parse_mode="Markdown")


# /leak command
async def leak_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Usage: /leak 918887882236")
        return

    query = context.args[0]
    api_url = f"http://sahilxalone.xyz/api/leak?key=LOVEABLE&number={query}"

    try:
        response = requests.get(api_url, timeout=15)
        data = response.json()
        await update.message.reply_text(f"🔍 **Leak Result**\n\n```json\n{data}\n```", parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")


# /ff command
async def ff_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Usage: /ff 1645613050")
        return

    uid = context.args[0]
    api_url = f"http://187.127.175.208:5000/Bmw?uid={uid}"

    try:
        response = requests.get(api_url, timeout=15)
        data = response.json()
        await update.message.reply_text(f"🎮 **FF Result**\n\n```json\n{data}\n```", parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")


# /tg command
async def tg_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Usage: /tg 7515862733")
        return

    query = context.args[0]
    api_url = f"https://r-bots-tg-2-number-api.co08.art/tg?key=R-BOTS82ns&q={query}"

    try:
        response = requests.get(api_url, timeout=15)
        data = response.json()
        await update.message.reply_text(f"📱 **Telegram Result**\n\n```json\n{data}\n```", parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")


def main():
    # Flask ko background me chalu karein
    keep_alive()

    # Telegram Bot Start
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("leak", leak_command))
    application.add_handler(CommandHandler("ff", ff_command))
    application.add_handler(CommandHandler("tg", tg_command))

    logger.info("Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
