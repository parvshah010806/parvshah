import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

    update.message.reply_text('Hi! Use /set <seconds> to set a timer')
    def main() -> None:
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5227297003:AAEwSnVl-aCGUYGbj92L4m1z6GWTh3ggGa8")

    dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))

 updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
