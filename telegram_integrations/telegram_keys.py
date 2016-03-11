class TelegramKeys:

    def __init__(self):
        self.keys = {}

    def add_key(self, chat_id, file_id):
        if chat_id in self.keys:
            self.keys[chat_id] += [file_id]
        else:
            self.keys[chat_id] = [file_id]
            # create and start thread
            threading.Thread(target=time_out, args=[bot, update.message.chat_id]).start()

    def remove_key(self, chat_id):
        if chat_id in self.keys:
            del self.keys[chat_id]

    # define time out function (threading)
    def time_out(bot, chat_id):
        # config time expiration
        time.sleep(5)
        KEYS.expiration()
        bot.sendMessage(chat_id=chat_id, text="Ha agotado el tiempo de espera")