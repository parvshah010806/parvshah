import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
 
updater = Updater("5227297003:AAEwSnVl-aCGUYGbj92L4m1z6GWTh3ggGa8")

dispatcher = updater.dispatcher


updater.start_polling()
