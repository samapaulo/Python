import bs4 as bs
import requests
import urllib.request
import pandas as pd

source =urllib.request.urlopen('https://www.washingtonpost.com/news-world-sitemap.xml').read()
soup = bs.BeautifulSoup(source, 'xml')

print(soup.find_all('p'))

for url in soup.find_all('loc'):
    print(url.text)
