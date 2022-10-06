import os

from flask import Blueprint, send_from_directory

media = Blueprint('media', __name__)

@media.get('/media/<name>')
def upload(name):
    path = os.path.join(os.getcwd(), "uploads")
    return send_from_directory(path, name)