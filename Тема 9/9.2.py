import requests

def req_func(generic_url, args_arr):
    response = ''
    if(generic_url[len(generic_url) - 1] == '?'):
        response = requests.get(generic_url, params=args_arr)
        return response.url
    else:
        for


payload = {'key1': 'value1', 'key2': 'value2'}
print(req_func('https://www.ozon.ru/search/?from_global=@&sorting=@&text=@', payload))