import bs4
import requests
import datetime

url = 'https://habr.com/ru/'
HEADERS = {
    'Accept': '*/*', 'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 OPR/54.0.2952.64'}

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'Android', 'sitemap']

response = requests.get(url, headers=HEADERS)
print(response.status_code)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')
for article in articles:
    article_titles = article.find_all(class_="tm-article-snippet__title tm-article-snippet__title_h2")
    article_titles = [title.text.strip() for title in article_titles]
    article_tags = article.find_all(class_="tm-article-snippet__hubs-item")
    article_tags = [tag.text.strip() for tag in article_tags]
    article_bodies = article.find_all(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
    article_bodies = [body.text.strip() for body in article_bodies]
    article_text = [*article_titles, *article_tags, *article_bodies]
    for line in article_text:
        line = line.split()
        for element in line:
            if element in KEYWORDS:
                date = article.find(class_='tm-article-snippet__datetime-published').contents[0]['title']
                title = article.find(class_="tm-article-snippet__title-link").text
                href = article.find(class_='tm-article-snippet__title-link').attrs['href']
                link = f'{"https://habr.com"}{href}'
                print(title)

