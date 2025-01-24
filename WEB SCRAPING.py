import os
os.chdir(r"C:\Users\Appala nithin\OneDrive\Pictures\Documents\NARESH-IT\AI-PART\JAN 8th - webscrapping\xml_single articles")

import  xml.etree.ElementTree as ET


tree = ET.parse("769952.xml")
root = tree.getroot()



import re, string , unicodedata
import nltk

from bs4 import BeautifulSoup

def strip_html(text):
    soup=BeautifulSoup(text,'html.parser')
    return soup.get_text()

def remove_between_square_brackets(text):
    return re.sub(r'\[[^]]*\]','',text)


def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

root=ET.tostring(root,encoding='utf8').decode('utf8')
sample = denoise_text(root)

print(sample)