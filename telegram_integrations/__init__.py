from telegram import Updater
from telegram_integrations.telegram_photo import TelegramPhoto
from telegram_integrations.telegram_keys import TelegramKeys

updater = Updater(token='196199210:AAH7GcqsNNUD5-sCHAR6BjgqxUxPwsHFcII')

keys = TelegramKeys()

dispatcher = updater.dispatcher

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

dispatcher.addTelegramCommandHandler('start', start)

def echo(bot, update):
    if TelegramPhoto.is_photo(update):
        keys.add_key(update.message.chat_id, TelegramPhoto.get_file_id(update))
        TelegramPhoto.get_file()
        bot.sendMessage(chat_id=update.message.chat_id, text="Gracias por tu foto")
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="Por favor, envía una foto adjunta")

dispatcher.addTelegramMessageHandler(echo)


updater.start_polling()
