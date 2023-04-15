import requests
from bs4 import BeautifulSoup


class Parser:
    html = ''
    data = []

    def __init__(self, url, fail):
        self.url = url
        self.fail = fail

    def get_html(self):
        ind = requests.get(self.url).text
        self.html = BeautifulSoup(ind, 'lxml')

    def parsing(self):
        el1 = self.html.find('body').find('div', id='allEntries').find_all('td')
        for d in el1:
            try:
                info1 = d.find('div').text
                info2 = d.find('span', class_='e-author').find('a').text
                info3 = d.find('span', class_='e-date').find('span', class_='ed-value').text
                self.data.append({
                    'title': info1,
                    'autor': info2,
                    'date': info3
                })
            finally:
                continue

    def save_data(self):
        with open(self.fail, 'w') as f:
            i = 1
            for token in self.data:
                # f.write(f'Новость № {i}\nНазвание: {token["title"]}')
                # i += 1
                f.write(f'Новость № {i}\nНазвание: {token["title"]}\nАвтор: {token["autor"]}\nДата: {token["date"]}'
                        f'\n\n')
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save_data()


def main():
    for i in range(12, 25):
        pars = Parser(f'http://www.nv43.ru/news/?page{i}', 'nw.txt')
        pars.run()


if __name__ == '__main__':
    main()
