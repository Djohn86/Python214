import requests
from bs4 import BeautifulSoup


def get_html(url):
    sait = requests.get(url)
    return sait.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    p1 = soup.find('body').find('div', id='allEntries').find_all('td')
    for dat in p1:
        el1 = dat.find('div').text
        el2 = dat.find('span', class_='e-author').find('a').text
        el3 = dat.find('span', class_='e-date').find('span', class_='ed-value').text
        print(f'{el1}\nautor - {el2}\ndate - {el3}\n')


def main():
    url = 'http://www.nv43.ru/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()