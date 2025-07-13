
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7552446301:AAHxd1xhNfjfZzhZ_BG_L6CmFXHSGXE4e4g"

def start(update: Update, context: CallbackContext):
    message = """👋 أهلاً بك في كورس المهارات الحياتية!

📄 للتسجيل، يرجى ملء هذا النموذج:
https://docs.google.com/forms/d/e/1FAIpQLSff_KgV9lkoWGl9aQHVvfgx3673hY_RG5mO84aymiVtpqY7tQ/viewform?usp=dialog

📌 بعد إرسال النموذج، سيتم التواصل معك وإرسال الكورس خلال 24 ساعة.
"""
    update.message.reply_text(message)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
