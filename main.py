from bs4 import BeautifulSoup
import requests

search = input("Search for:")
params = {"q": search} # search variable q to what we wan to search for

r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("Li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs("href")

    if item_text and item_href:
        print(item_text)
        print(item_href)