import requests
from bs4 import BeautifulSoup

def request_start(url:str):
    url = url
    page = requests.get(url)
    soup = BeautifulSoup(page.text,  "html.parser")
    return soup






if __name__ == '__main__':
    url = 'https://ru.pinterest.com/ideas/мемы-с-котиками-без-мата/905677035414/'
    soup = request_start(url)
    # result = Chear_point(soup)

