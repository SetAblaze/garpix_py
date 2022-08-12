import requests

def some_func(language_list):
    output_arr = []
    for i in language_list:
        response = requests.get(
            'https://api.github.com/search/repositories',
            params={'q': f'requests+language:{i}'},
        )
        jsn = response.json()
        output_arr.append([i,jsn['total_count']])
    return output_arr

print(some_func(['python', 'c++', 'java', 'javascript', 'ruby', 'c#']))