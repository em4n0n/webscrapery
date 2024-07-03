from bs4 import BeautifulSoup
import requests

search = input("Search for:")
params = {"q": search} # search variable q to what we wan to search for

r = requests.get("https://www.bing.com/search?q=pizza", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("Li", {"class": "b_algo"})