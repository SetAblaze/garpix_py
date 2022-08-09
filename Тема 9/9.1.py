import requests

def get_req(generic_url):
        response = requests.get(generic_url)
        print(f'По запросу {generic_url} GET вывело следующий код:  {response.status_code}')

get_req('https://www.google.ru/')