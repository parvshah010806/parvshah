from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater
import logging
updater = Updater(token='5227297003:AAEwSnVl-aCGUYGbj92L4m1z6GWTh3ggGa8', use_context=True)

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()