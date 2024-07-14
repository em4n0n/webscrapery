from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def StartSearch():
    search = input("Search for:")
    params = {"q": search}
    dir_name = search.replace(" ", "_".lower())
    r = requests.get("http://www.bing.com/images/search", params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    for item in links:
        img_obj = requests.get(item.attrs["href"])
        print("Getting", item.attrs["href"])
        title = item.attrs["href"].split("/")[-1]
        try:
            img = Image.open(BytesIO(img_obj.content))
            img.save("./scraped_images/" + title, img.format)
        except:
            print("Could not save image.")

    StartSearch()

StartSearch()