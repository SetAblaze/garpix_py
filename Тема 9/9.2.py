import requests

def req_func(generic_url, args_arr):
    if(generic_url[len(generic_url) - 1] == '?'):
        response = requests.get(generic_url, params=args_arr)
        return response.url
    else:
        output_url = ''
        buff_url = generic_url
        for i in args_arr:
            index = buff_url.find('=') + 1
            output_url += buff_url[:index] + args_arr[i]
            buff_url = buff_url[index+1:]
        response = requests.get(output_url)
        return output_url, response.status_code

payload = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(req_func('https://www.ozon.ru/search/?from_global=@&sorting=@&text=@', payload))