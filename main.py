from telegram.ext import Updater
from telegram.ext import CommandHandler

updater = Updater(token='5227297003:AAEwSnVl-aCGUYGbj92L4m1z6GWTh3ggGa8', use_context=True)

dispatcher = updater.dispatcher

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

from telegram import Update
from telegram.ext import CallbackContext


from telegram.ext import MessageHandler, Filters

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

from telegram.ext import CommandHandler

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
