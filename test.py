import requests
import json
from docx import Document
from docx.shared import Pt
import docx
from bs4 import BeautifulSoup
from pprint import pprint
from docx.enum.text import WD_ALIGN_PARAGRAPH
import re


def save_and_download_image(picture_url,photo_path):
        response = requests.get(picture_url)
        with open(photo_path, "wb") as file:
            file.write(response.content)
        return response

user_choise = input("Write link to your wiki page: ")
response = requests.get(user_choise)
response.raise_for_status() 
soup = BeautifulSoup(response.text, features="html.parser")
url = f'https:{soup.find("img")["src"]}'

print(save_and_download_image(picture_url=url,photo_path="./image_papka.jpg"))