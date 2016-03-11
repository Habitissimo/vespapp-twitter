import threading

class TelegramKeys:

    lock = threading.Lock()

    def __init__(self):
        self.keys = {}

    def add_key(self, bot, chat_id, file_id):
        self.lock.acquire()
        try:
            if chat_id in self.keys:
                self.keys[chat_id] += [file_id]
            else:
                self.keys[chat_id] = [file_id]
        finally:
            self.lock.release()

    def remove_key(self, chat_id):
        self.lock.acquire()
        try:
            if chat_id in self.keys:
                del self.keys[chat_id]
        finally:
            self.lock.release()