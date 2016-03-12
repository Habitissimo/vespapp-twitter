import threading


class TelegramKeys:

    lock = threading.Lock()

    def __init__(self):
        self.keys = {}
        self.url = 'http://web-1.avispamientoweb.d28e17c3.cont.dockerapp.io/api'

    def add_photo(self, chat_id, file_id):
        self.lock.acquire()
        try:
            if chat_id in self.keys:
                self.keys[chat_id].update({'photos': file_id})
                self.lock.release()
                return True
            else:
                self.keys[chat_id] = {'photos': [file_id]}
                self.lock.release()
                return False
        finally:
            self.lock.release()
            return None

    def add_location(self, chat_id, latitude, longitude):
        self.lock.acquire()
        try:
            if chat_id in self.keys:
                self.keys[chat_id] = {'location': [latitude, longitude]}
                self.lock.release()
                return True
            else:
                self.keys[chat_id] = {'location': [latitude, longitude]}
                self.lock.release()
                return False
        finally:
            self.lock.release()
            return None

    def add_type(self, chat_id, type):
        self.lock.acquire()
        try:
            if chat_id in self.keys:
                self.keys[chat_id].update({'type': type})
                self.lock.release()
                return True
            else:
                self.keys[chat_id].update({'type': type})
                self.lock.release()
            return False
        finally:
            self.lock.release()
            return None

    def get_key_by_id(self, chat_id):
        self.lock.acquire()
        try:
            if chat_id in self.keys:
                key = self.keys[chat_id]
                self.lock.release()
                return key
            return None
        finally:
            self.lock.release()
            return None

    def remove_key(self, chat_id):
        self.lock.acquire()
        try:
            if chat_id in self.keys:
                del self.keys[chat_id]
                self.lock.release()
                return True
            return None
        finally:
            self.lock.release()
            return None