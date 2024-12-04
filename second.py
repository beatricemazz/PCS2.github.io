# url_extractor.py
import requests
import re

def get_restaurant_urls(i):
    current_url = f"https://guide.michelin.com/en/it/restaurants/page/{i}"
    page_text = requests.get(current_url).text
    address_pattern = r'href="/en/.+?/.+?/restaurant/.+?"'
    matches = re.findall(address_pattern, page_text)
    page_urls = {"https://guide.michelin.com" + match[6:-1] for match in matches}
    return i, page_urls