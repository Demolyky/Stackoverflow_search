import requests
import json
import datetime


class Stackoverflow:

    def __init__(self):
        self.host = 'https://api.stackexchange.com/'
        self.url = '/2.3/search'

    def search_in_file(self, tag):
        __requests_url = self.host + self.url
        __params = {'fromdate': datetime.date.today()-datetime.timedelta(days=1), 'todate': datetime.date.today(),
                    'order': 'desc', 'sort': 'creation', 'tagged': tag, 'site': 'stackoverflow'}
        __responce = requests.get(__requests_url, params=__params)

        with open('all_result', 'w+') as f:
            json.dump(__responce.json(), f, ensure_ascii=False, indent=2)
        with open('result', 'w+') as f:
            _questions = [{'title': title['title'], 'link': title['link']} for title in __responce.json()['items']]
            number=0
            for question in _questions:
                number+=1
                f.write(f'{number}. Название статьи: "{question["title"]}", ссылка: {question["link"]}')
                print(f'{number}. Название статьи: "{question["title"]}", ссылка: {question["link"]}')


search_stack = Stackoverflow()
search_stack.search_in_file('Python')
