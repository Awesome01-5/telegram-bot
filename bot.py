import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

signals = [
    {
        "pair": "EUR/USD",
        "signal": "BUY",
        "entry": "1.0850",
        "sl": "1.0810",
        "tp": "1.0900",
        "risk": "Medium"
    }
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running. Use /signal")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    s = random.choice(signals)
    text = f"""
PAIR: {s['pair']}
SIGNAL: {s['signal']}
ENTRY: {s['entry']}
SL: {s['sl']}
TP: {s['tp']}
RISK: {s['risk']}
"""
    await update.message.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

app.run_polling()
