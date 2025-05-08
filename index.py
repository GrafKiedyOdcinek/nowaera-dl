import os
import json
import requests
from PIL import Image
from fpdf import FPDF
from PyPDF2 import PdfMerger


def load_config(file_path):
    with open(file_path) as config_file:
        return json.load(config_file)


def create_download_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)


def download_images(base_url, number_of_pages, cookies, download_folder):
    image_paths = []
    for number in range(1, number_of_pages + 1):
        page_number = f"{number:03d}"  # Format page number to 3 digits
        url = base_url.replace("XXX", page_number)  # Replace XXX with the formatted page number
        response = requests.get(url, cookies=cookies)

        if response.status_code == 200:
            image_path = os.path.join(download_folder, f"{page_number}.jpg")
            with open(image_path, 'wb') as img_file:
                img_file.write(response.content)
            image_paths.append(image_path)
        else:
            print(f"Failed to download image {page_number}: {response.status_code}")
    return image_paths


def create_temp_pdf(image_paths, temp_pdf_folder):
    os.makedirs(temp_pdf_folder, exist_ok=True)
    for image_path in image_paths:
        with Image.open(image_path) as img:
            width_mm = img.width * 0.264583
            height_mm = img.height * 0.264583

        pdf = FPDF(orientation='P', unit='mm', format=(width_mm, height_mm))
        pdf.add_page()
        pdf.image(image_path, x=0, y=0, w=width_mm, h=height_mm)

        individual_pdf_path = os.path.join(temp_pdf_folder, f"{os.path.basename(image_path).replace('.jpg', '.pdf')}")
        pdf.output(individual_pdf_path)


def merge_pdfs(temp_pdf_folder, output_pdf):
    merger = PdfMerger()
    for pdf_file in os.listdir(temp_pdf_folder):
        if pdf_file.endswith('.pdf'):
            merger.append(os.path.join(temp_pdf_folder, pdf_file))
    merger.write(output_pdf)
    merger.close()


def clean_temp_files(temp_pdf_folder):
    for pdf_file in os.listdir(temp_pdf_folder):
        os.remove(os.path.join(temp_pdf_folder, pdf_file))
    os.rmdir(temp_pdf_folder)


def main():
    config = load_config('config.json')

    download_folder = config['download_folder']
    output_pdf = config['output_pdf']
    number_of_pages = config['number_of_pages']
    cookies = config['cookies']

    create_download_folder(download_folder)

    base_url = config['url']
    image_paths = download_images(base_url, number_of_pages, cookies, download_folder)

    temp_pdf_folder = os.path.join(download_folder, "temp_pdfs")
    create_temp_pdf(image_paths, temp_pdf_folder)

    merge_pdfs(temp_pdf_folder, output_pdf)

    clean_temp_files(temp_pdf_folder)

    print(f"PDF created successfully: {output_pdf}")


if __name__ == "__main__":
    main()
