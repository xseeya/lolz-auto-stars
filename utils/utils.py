import re

def extract_telegram_data(link):
    media_match = re.search(r'\[MEDIA=telegram\]([^/\]]+)/(\d+)\[/MEDIA\]', link)
    if media_match:
        return {
            "username": media_match.group(1),
            "post_id": int(media_match.group(2))
        }
        

