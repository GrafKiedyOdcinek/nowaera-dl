import os
import json
import requests


def load_config(file_path):
    with open(file_path) as config_file:
        return json.load(config_file)


def create_download_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)


def download_images(base_url, number_of_pages, cookies, download_folder):
    image_paths = []

    x_count = base_url.count("X")

    if x_count not in [2, 3]:
        raise ValueError("URL must contain either 'XX' or 'XXX' to indicate page numbering.")

    for number in range(1, number_of_pages + 1):
        if x_count == 3:
            page_number = f"{number:03d}"
        else:
            page_number = f"{number:02d}"

        url = base_url.replace("X" * x_count, page_number)
        response = requests.get(url, cookies=cookies)

        if response.status_code == 200:
            image_path = os.path.join(download_folder, f"{page_number}.jpg")
            with open(image_path, 'wb') as img_file:
                img_file.write(response.content)
            image_paths.append(image_path)
        else:
            print(f"Failed to download image {page_number}: {response.status_code}")

    return image_paths


def main():
    config = load_config('config.json')

    download_folder = config['download_folder']
    number_of_pages = config['number_of_pages']
    cookies = config['cookies']
    base_url = config['url']

    create_download_folder(download_folder)
    download_images(base_url, number_of_pages, cookies, download_folder)

    print(f"Images downloaded successfully to: {download_folder}")


if __name__ == "__main__":
    main()
