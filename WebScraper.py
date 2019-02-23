import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        hfile = open("headlines.txt", "w+")
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url and "html" in url:
                hfile.write(url + "\n")
                print("\n" + url)




news = "https://news.google.com/"
Scraper(news).scrape()



