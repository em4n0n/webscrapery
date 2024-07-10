from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

search = input("Search for:")
params = {"q": search}