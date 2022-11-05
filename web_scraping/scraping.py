import bs4
import requests


url = 'https://habr.com'

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get(url)
print(response.status_code)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_="tm-article-snippet__title-link")
    hubs = [hub.text.strip() for hub in hubs]
    print(hubs)
