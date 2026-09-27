import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8633944838:AAEcatdgpON3vLBs60qOPoVgAPrAnEGu3NA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🎲 Son tashlash", callback_data='roll')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "1 dan 5 gacha bo'lgan tasodifiy sonni olish uchun tugmani bosing:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    son = random.randint(1, 5)
    
    keyboard = [[InlineKeyboardButton("🎲 Yana tashlash", callback_data='roll')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text=f"Tushgan son: {son}",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button, pattern="^roll$"))
    app.run_polling()

if __name__ == "__main__":
    main()
