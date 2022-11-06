import bs4
import requests


url = 'https://habr.com/ru/'
HEADERS = {
    'Accept': '*/*', 'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 OPR/54.0.2952.64'}

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'android', 'sitemap', ]


def get_data(site_address, head):
    response = requests.get(site_address, headers=head)
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article')
    return articles


def get_news(data, search_words):

    link_list = []

    for article in data:
        article_titles = article.find_all(class_="tm-article-snippet__title tm-article-snippet__title_h2")
        article_titles = [title.text.strip().lower() for title in article_titles]
        article_tags = article.find_all(class_="tm-article-snippet__hubs-item")
        article_tags = [tag.text.strip().lower() for tag in article_tags]
        article_bodies = article.find_all(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
        article_bodies = [body.text.strip().lower() for body in article_bodies]
        article_text = (*article_titles, *article_tags, *article_bodies)
        for line in article_text:
            line = line.split()
            for element in line:
                if element in search_words:
                    date = article.find(class_='tm-article-snippet__datetime-published').contents[0]['title']
                    title = article.find(class_="tm-article-snippet__title-link").text
                    href = article.find(class_='tm-article-snippet__title-link').attrs['href']
                    link = f'{"https://habr.com"}{href}'
                    if title not in link_list:
                        link_list.append(title)
                        print(f'{date} -> {title} ==> {link}')


if __name__ == '__main__':
    get_news(get_data(url, HEADERS), KEYWORDS)
