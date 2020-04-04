#install BeautifulSoup  and requests library
#Import Them
import requests
from bs4 import BeautifulSoup

class WebScrapper():
   wikiDoc = requests.get("https://en.wikipedia.org/wiki/Deep_learning");
   parsedDoc = BeautifulSoup(wikiDoc.content, "html.parser")

    #function to get the title of the page
   def getTitle(self):
     title = self.parsedDoc.title.string
     return title

   # function to get all the links available
   def getWikiLinks(self):
       list =[]
       for link in self.parsedDoc.find_all('a'):
           # print(list)
           list.append(link.get('href'))
       return list
webs = WebScrapper()
print(webs.getTitle())
print(webs.getWikiLinks())