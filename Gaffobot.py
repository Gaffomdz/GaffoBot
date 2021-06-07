import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hola, soy el gaffo bot, si escribis /price te dire el precio de Bitcoin')



def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def price(update,context):
    """Look ticker and response with the last price"""

    url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD&extraParams=1096939742a514c52eaa08c7072eaaf47bbadf71e03b8657a417566b7e68aee0"
    r = requests.get(url)
    js = r.json()
    last_price = str(round(float(js["RAW"]['BTC']["USD"]["PRICE"]),4))
    update.message.reply_text('Ultimo precio BTC: '+last_price)
    print(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def puteada(update, context):
    """putea."""
    update.message.reply_text('Forro!')


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1551953753:AAGCilsAdxWBs-g-Qc_jhIKvsL6XhnOwvEk", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("cardano", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, price))
    
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
