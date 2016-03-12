import threading, time

from telegram import Updater
from telegram_integration.telegram_keys import TelegramKeys
from telegram_integration.telegram_photo import TelegramPhoto
from telegram_integration.telegram_location import TelegramLocation
from telegram_integration.telegram_requester import TelegramRequester

# global variables
keys = TelegramKeys()

# create bot
updater = Updater(token='175120475:AAGxpJ4TC-24XTF6Jvub9-eWYEqQFJ0AUZo')
dispatcher = updater.dispatcher


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

# add /start dispatcher
dispatcher.addTelegramCommandHandler('start', start)


def echo(bot, update):
    if TelegramPhoto.is_photo(update):
        # add photo in keys
        file_id = TelegramPhoto.get_file_id(update)
        result = keys.add_photo(chat_id=update.message.chat_id, file_id=file_id)
        if result is not None and not result:
            # create thread
            # TODO start()
            thr = threading.Thread(target=time_out, args=[bot, update.message.chat_id])

        # image received
        bot.sendMessage(chat_id=update.message.chat_id, text="Imagen recibida! Gracias por tu colaboración!")
        # TODO send custom keyboard

    elif TelegramLocation.is_location(update):
        # get latitude and longitude
        latitude, longitude = TelegramLocation.get_location(update)
        # add location in keys
        result = keys.add_location(chat_id=update.message.chat_id, latitude=latitude, longitude=longitude)
        if result is not None and not result:
            # create thread
            # TODO start()
            thr = threading.Thread(target=time_out, args=[bot, update.message.chat_id])

        # location received
        bot.sendMessage(chat_id=update.message.chat_id, text="Localización recibida! Gracias por tu colaboración!")
        # TODO send custom keyboard

    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="No podemos procesar el mensaje")

# add @msg to dispatcher
dispatcher.addTelegramMessageHandler(echo)


def stop(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hemos registrado su avispamiento!")
    bot.sendMessage(chat_id=update.message.chat_id, text="Gracias por la colaboración!")
    keys.add_type(chat_id=update.message.chat_id, type=1)
    TelegramRequester.send_request(bot=bot, key=keys.get_key_by_id(chat_id=update.message.chat_id))
    keys.remove_key(chat_id=update.message.chat_id)

# add /stop dispatcher
dispatcher.addTelegramCommandHandler('stop', stop)

# start bot
updater.start_polling()


# define time out function (threading)
def time_out(bot, chat_id):
    # config time expiration
    time.sleep(2)
    bot.sendMessage(chat_id=chat_id, text="Ha agotado el tiempo de espera")
