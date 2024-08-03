from .services import get_spotify_data, get_apple_music_data
from .ai import generate_playlist_from_data

def generate_playlist(data):
    # Example data handling
    service = data.get('service')
    user_data = data.get('user_data')
    
    if service == 'spotify':
        data = get_spotify_data(user_data)
    elif service == 'apple_music':
        data = get_apple_music_data(user_data)
    else:
        return {"error": "Unsupported service"}
    
    playlist = generate_playlist_from_data(data)
    return playlist
