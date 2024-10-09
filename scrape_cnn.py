from bs4 import BeautifulSoup
import requests

url = 'https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html'
def fetch_html(url):
    respond = requests.get(url)
    return respond.text if respond.status_code == 200 else print('error')


def parsing_content(respond):
    soup = BeautifulSoup(respond, 'html.parser')
    title = soup.find('h1')
    content = ' '.join([p.text for p in soup.find_all('p')])
    f = open('text.txt', 'w')
    f.write("Title: "+ title.text +content)
    f.close()
    return print(title.text, content)

respond = fetch_html(url)
parsing_content(respond)
