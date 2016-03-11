from telegram import Updater
from telegram_integration.telegram_keys import TelegramKeys
from telegram_integration.telegram_photo import TelegramPhoto

# global variables
keys = TelegramKeys

# create bot
updater = Updater(token='175120475:AAGxpJ4TC-24XTF6Jvub9-eWYEqQFJ0AUZo')
dispatcher = updater.dispatcher

def start (bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

# add /start dispatcher
dispatcher.addTelegramCommandHandler('start', start)

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)
    if TelegramPhoto.is_photo(update):
        keys.add_key(chat_id=update.message.chat_id, file_id= TelegramPhoto.get_file_id(update))
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="No podemos procesar el siguiente archivo")



# add @msg to dispatcher
dispatcher.addTelegramMessageHandler(echo)

# start bot
updater.start_polling()
