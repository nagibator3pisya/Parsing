from  bs4 import BeautifulSoup
import requests
import os
# Директория для сохранения фотографий
output_dir = 'photos'

# Создаем директорию, если она не существует
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Заголовки, чтобы замаскироваться под браузер
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
def urls(urls):
    request = requests.get(urls, headers=headers)
    soups = BeautifulSoup(request.text,'html.parser')
    return soups



def cheak_photo(soups):
    """
    находим все фотки
    :param soups: в него передаем запрос который идет на сайт
    image - находит все совпадение с классом image
    далее по списку идем по ссылкам
    :return:
    """
    image = soups.find_all('img')
    list_photo = []
    for i in image:
        if i.get('src'):
            list_photo.append(i['src'])
    return list_photo


def download_photo(photo_url,base_url):
    for i,url in enumerate(photo_url):
        if not url.startswith('http'):
            url = base_url + url
        response = requests.get(url,headers=headers)
        with open(os.path.join(output_dir,f'image_{i}.jpg'),'wb') as f:
            f.write(response.content)


if __name__ == '__main__':
    url = 'https://koteiki.com/'
    soup = urls(url)
    img = cheak_photo(soup)
    # print(img)
    download_photo(img,url)

