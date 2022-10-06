import os

from flask import send_from_directory

class MediasController:
    def upload(self, name):
        path = os.path.join(os.getcwd(), "uploads")
        return send_from_directory(path, name)