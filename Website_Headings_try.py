from bs4 import BeautifulSoup
import urllib.request
import lxml

source = urllib.request.urlopen('https://www.nytimes.com/')
soup = BeautifulSoup(source,'lxml')
print(soup.title)

