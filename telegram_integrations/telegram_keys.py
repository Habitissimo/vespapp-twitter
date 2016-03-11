class TelegramKeys:

    def __init__(self):
        self.keys = {}

    def add_key(self, chat_id, file_id):
        if chat_id in self.keys:
            self.keys[chat_id] += [file_id]
        else:
            self.keys[chat_id] = [file_id]
            # TODO lanzar un thread

    def remove_key(self, chat_id):
        if chat_id in self.keys:
            del self.keys[chat_id]