import threading


class TelegramKeys:

    def __init__(self):
        self.keys = {}
        self.lock = threading.Lock()

    def add_photo(self, update, file_id):
        self.lock.acquire()
        try:
            if update.message.chat_id in self.keys:
                self.keys[update.message.chat_id].update({'photos': [file_id]})
                return True
            else:
                self.keys[update.message.chat_id] = {'photos': [file_id],
                                                     'user': [update.message.chat.username]}
                return False
        finally:
            self.lock.release()

    def add_location(self, update, latitude, longitude):
        self.lock.acquire()
        try:
            if update.message.chat_id in self.keys:
                self.keys[update.message.chat_id].update({'location': [latitude, longitude]})
                return True
            else:
                self.keys[update.message.chat_id] = {'location': [latitude, longitude],
                                                     'user': [update.message.chat.username]}
                return False
        finally:
            self.lock.release()

    def add_type(self, update, t_avispamiento):
        self.lock.acquire()
        try:
            if update.message.chat_id in self.keys:
                self.keys[update.message.chat_id].update({'type': t_avispamiento})
                return True
            else:
                self.keys[update.message.chat_id] = {'type': t_avispamiento,
                                                     'user': [update.message.chat.username]}
            return False
        finally:
            self.lock.release()

    def get_key_by_id(self, chat_id):
        self.lock.acquire()
        try:
            if chat_id in self.keys:
                return self.keys[chat_id]
            return None
        finally:
            self.lock.release()

    def remove_key(self, chat_id):
        self.lock.acquire()
        try:
            if chat_id in self.keys:
                del self.keys[chat_id]
                return True
            return None
        finally:
            self.lock.release()
