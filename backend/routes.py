from flask import Blueprint, request, jsonify
from .controllers import generate_playlist

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Welcome to Playlist Generator!"

@main.route('/generate_playlist', methods=['POST'])
def generate_playlist_route():
    data = request.json
    playlist = generate_playlist(data)
    return jsonify(playlist)
