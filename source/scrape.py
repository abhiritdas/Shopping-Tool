from bs4 import BeautifulSoup
import requests

#send request to website
def scrape(result_from_main):

    product_listings = []
    url = "https://www.newegg.com/p/pl?d="
    search = result_from_main
    result = requests.get(url + search)

    #create Beautiful Soup Object
    doc = BeautifulSoup(result.text, "html.parser")

    #returns first tag in the product title
    item = []
    items = doc.find_all("div", class_="item-container")
    for item in items:
        item_name = item.find("a", class_ = "item-title")
        product_listings.append("Product: " + item_name.string)

        #finding price of product
        prices = item.find_all(text = "$")
        parent = prices[0].parent
        strong = parent.find("strong")
        sup = parent.find("sup")
        product_listings.append("Price: $" + strong.string + sup.string)

    return product_listings