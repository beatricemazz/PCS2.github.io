# downloader.py
import os
import requests
import uuid

def html_downloader(i, u_url, original_directory):
    response = requests.get(u_url)
    response.raise_for_status()  # Raise an error for bad responses
    unique_filename = f"{uuid.uuid4()}.html"
    filepath = os.path.join(original_directory, "data", str(i), unique_filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)  # Create folder if it doesn't exist
    with open(filepath, "w", encoding="utf-8") as file:
         file.write(response.text)
    print(f"Downloaded: {u_url}")

