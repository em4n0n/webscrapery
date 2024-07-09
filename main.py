from bs4 import BeautifulSoup
import requests

search = input("Search for:")
params = {"q": search} # search variable q to what we want to search for

r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"}) # first instance of an ordered list and the attributes to look for
links = results.findAll("Li", {"class": "b_algo"}) # find all list items with a class b_algo to store them in a list called links

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs("href") # find the attribute href

    if item_text and item_href:
        print(item_text)
        print(item_href)
    
        children = item.children
        for child in children:
            print("Child:", child)