import configparser
from telegram.ext import Updater, CommandHandler

def hello(bot, update):
    update.message.reply_text(
        'hello, {}'.format(update.message.from_user.first_name))


config = configparser.ConfigParser()
config.read('config.ini')

updater = Updater(config['TELEGRAM']['ACCESS_TOKEN'], use_context=True)

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()