import threading


class TelegramKeys:

    lock = threading.Lock()

    def __init__(self):
        self.keys = {}

    def add_photo(self, chat_id, file_id):
        #self.lock.acquire()
        #try:
        if chat_id in self.keys:
            self.keys[chat_id].update({'photos': file_id})
            return True
        else:
            self.keys[chat_id] = {
                'photos': [file_id]}
            return False
        #finally:
        #    self.lock.release()
        #    return None

    def add_location(self, chat_id, latitude, longitude):
        #self.lock.acquire()
        #try:
        if chat_id in self.keys:
            # update value
            self.keys[chat_id] = {
                'location': [latitude, longitude]}
            return True
        else:
            # new value
            self.keys[chat_id] = {
                'location': [latitude, longitude]}
            return False
        #finally:
        #    self.lock.release()
        #    return None

    def add_type(self, chat_id, type):
        if chat_id in self.keys:
            # update value
            self.keys[chat_id] = {
                'type': type}
            return True
        else:
            # new value
            self.keys[chat_id] = {
                'type': type}
            return False

    def remove_key(self, chat_id):
        self.lock.acquire()
        try:
            if chat_id in self.keys:
                del self.keys[chat_id]
        finally:
            self.lock.release()

    @classmethod
    def send_request(cls, chat_id):
        
