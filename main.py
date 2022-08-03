KEYWORDS = ['искусственный интеллект', 'образование', 'Как']

import requests
# pip install BeautifulSoup4
from bs4 import BeautifulSoup

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,bg;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_ym_uid=1620378523565045443; hl=ru; fl=ru; _ga=GA1.2.1094103539.1649505661; _ym_d=1650362059; '
              'habr_web_home_feed=/all/; _ym_isad=2; _gid=GA1.2.642503540.1659431761; '
              'visited_articles=551994:531472:488054:483400:63539:103257:186608:552212; _gat_gtag_UA_726094_1=1',
    'Host': 'habr.com',
    'Referer': 'https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': "s'ame-origin'",
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                  'Safari/537.36 '
}

url = 'https://habr.com/ru/all/'
ret = requests.get(url, timeout=5, headers=HEADERS)

soup = BeautifulSoup(ret.text, 'html.parser')

articles = soup.findAll('div', class_="tm-article-snippet")

data = []
for article in articles:
    article_date = article.find('span', class_='tm-article-snippet__datetime-published')
    article = article.find('a', class_='tm-article-snippet__title-link')
    article_link = 'https://habr.com' + article.get('href')
    data.append([article_date.text, article.text, article_link])

data_new = []
for i in data:
    for j in KEYWORDS:
        if j in i[1]:
            data_new.append(i)

for i in data_new:
    print(*i)