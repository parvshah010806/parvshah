import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
# Best practice would be to replace context with an underscore,
# since context is an unused local variable.
# This being an example and not having context present confusing beginners,
# we decided to have it present as context.
def start(update: Update, context: CallbackContext) -> None:
    """Sends explanation on how to use the bot."""
    
    update.message.reply_text('Hi! Use /set <seconds> to set a timer')
 
updater = Updater("5227297003:AAEwSnVl-aCGUYGbj92L4m1z6GWTh3ggGa8")

dispatcher = updater.dispatcher


updater.start_polling()
updater.idle()


if __name__ == '__main__':
    main()
