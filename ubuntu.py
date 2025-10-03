import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename or '.' not in filename:
        filename = f"downloaded_image_{hashlib.md5(url.encode()).hexdigest()[:8]}.jpg"
    return filename

def is_duplicate(filepath, content):
    if not os.path.exists(filepath):
        return False
    with open(filepath, 'rb') as f:
        existing_content = f.read()
    return hashlib.md5(existing_content).digest() == hashlib.md5(content).digest()

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = input("Please enter image URLs (comma separated): ").split(',')

    os.makedirs("Fetched_Images", exist_ok=True)
    downloaded = set()

    for url in map(str.strip, urls):
        if not url:
            continue
        try:
            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()

            # Check Content-Type header
            content_type = response.headers.get('Content-Type', '')
            if not content_type.startswith('image/'):
                print(f"✗ Skipped (not an image): {url}")
                continue

            filename = get_filename_from_url(url)
            filepath = os.path.join("Fetched_Images", filename)

            # Prevent duplicate downloads by filename and content
            if filename in downloaded or is_duplicate(filepath, response.content):
                print(f"✗ Duplicate image skipped: {filename}")
                continue

            # Save the image
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

            downloaded.add(filename)
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred for {url}: {e}")

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
