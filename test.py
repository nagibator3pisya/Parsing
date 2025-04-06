from bs4 import BeautifulSoup
import requests
import re

def request_start(url:str):
    url = url
    page = requests.get(url)
    soup = BeautifulSoup(page.text,  "html.parser")
    return soup


def Chear_point(soup):
    lists = []
    all_content = soup.find_all(class_='post__message')
    for i in all_content:
        lists.append(i.text)
    return lists


def links(result):
    # (http|https):(\/\/)(\w+)(.)(\w+)(\/)(\w+)(\/)(\w+\W)(\w+)(\/)(\w+)(\/)(\w+)
    all_links = []
    for text in result:
        found_links = re.finditer(r'(http|https):(\/\/)(\w+)(.)(\w+)(.*)', text)
        all_links.extend(found_links)
    return all_links


def file_text(links):
    try:
        with open('open_files/ss.txt', 'w', encoding='utf8') as f:
            for link in links:
                f.write(link + '\n')
        print("Файл успешно записан.")
    except Exception as e:
        print(f"Ошибка при записи файла: {e}")


def main():
    lin = []
    ursl = 'https://2ch.hk/hc/res/604286.html'
    soup = request_start(ursl)
    result = Chear_point(soup)
    linss = links(result)

    for match in linss:
        lin.append(match.group())

    print("Найденные ссылки:", lin)  # Отладочное сообщение

    if lin:
        file_text(lin)
    else:
        print("Нет данных для записи в файл.")





if __name__ == '__main__':
    main()





