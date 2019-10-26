from bs4 import BeautifulSoup
import requests

# html_doc = """
# <html>
# <head>
# <title>My Super Puper Title</title>
# </head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """

url = "https://meteo.ua/ua/34/kiev/month"
response = requests.get(url)
html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')
# tempr = soup.find_all(class_ = 'wwt_cont')

tempr = soup.find_all(class_ = 'wthr30_itm')

for i in tempr:
    # print(i)

    print(i.find_all(class_ = 'wi_num')[0].text)
    print(i.find_all(class_ = 'wi_mon')[0].text)
    if i.find('img'):
        print(i.find('img').get('title'))
        print("Мин." + i.find_all(class_ = '')[2].text)
        #print("Макс." + i.find_all(class_ = '')[3].text)
    else:
        pass

    print("==================")



# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.title.string)
#
# for link in soup.find_all('a'):
#     print(link.get('href'))
