# Import Beautiful Soup
# and urllib modules
import bs4 as bs
import urllib.request

#assign variable to specimen url
source =urllib.request.urlopen('https://www.washingtonpost.com/news-world-sitemap.xml').read()

#read url using xml format
soup = bs.BeautifulSoup(source, 'xml')

#find the links
for url in soup.find_all('loc'):
    print(url.text)
