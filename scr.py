from bs4 import BeautifulSoup
import requests
import csv
f = csv.writer(open('books.csv','w',encoding="utf-8"))
f.writerow(["Name","Price","Category"])
URL = 'http://books.toscrape.com/index.html'
baseURL = 'http://books.toscrape.com/'
page = requests.get(URL)
indexSoup = BeautifulSoup(page.text,'html.parser')
indexSoup = indexSoup.find(class_="side_categories")
indexSoup = indexSoup.find('ul')
linksSoup = indexSoup.find_all('a')
links = []
categorySoups = []
for linkSoup in linksSoup:
    links.append(baseURL + linkSoup['href'])

for link in links:
    #print(link)
    category = requests.get(link)
    categoryLink = link.replace("index.html","")
    categorySoups.append({'theSoup':BeautifulSoup(category.text,'html.parser'),'lnk':categoryLink})
categorySoups = categorySoups[1:]
for category in categorySoups:
    tempSoup = category['theSoup']
    title = tempSoup.find(class_="page-header action")
    title = title.find('h1')
    categoryTitle = title.string
    print('-------------------' + categoryTitle + '---------------')
    while True:
        next = tempSoup.find(class_="next")
      
        articles = tempSoup.find_all('article')
        for article in articles:
            bookname = article.find('h3')
            bookname = bookname.find('a')
            bookNameString = bookname['title']
            bookPrice = article.find(class_='product_price')
            bookPrice = article.find(class_='price_color')
            bookPriceString = bookPrice.string
            bookPriceString = bookPriceString[2:]
            print(bookNameString + "   PRICE:  " + bookPriceString)
            f.writerow([bookNameString,bookPriceString,categoryTitle])
        if next:
            next = next.find('a')
            tempPage = requests.get(category['lnk'] + next['href'])
            tempSoup = BeautifulSoup(tempPage.text,'html.parser')
        else:
            break