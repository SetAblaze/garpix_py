import requests

def get_req(generic_url):
    response = f'По запросу {generic_url} get вывело следующий код: {requests.get(generic_url)}'
    return response

print(get_req('https://www.google.ru/'))