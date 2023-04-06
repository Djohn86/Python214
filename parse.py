import requests
from bs4 import BeautifulSoup


class Parser:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        new = self.html.find_all("div", class_='caption')
        for item in new:
            title = item.find('h3')
            href = item.find('a').get('href')
            self.res.append({
                'title': title,
                'href': href
            })
            print(self.res)

    def run(self):
        self.get_html()
        self.parsing()
        self.save()

    def save(self):
        with open(self.path, 'w') as f:
            i = 1
            for item in self.res:
                f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nСсылка: {item["href"]}')
                i += 1



