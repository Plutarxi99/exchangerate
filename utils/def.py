import requests

url = 'https://api.github.com/search/repositories'
params = {'q': 'python', 'sort': 'stars'}
response = requests.get(url, params=params)

print(response.content)
# b'{"total_count":3204986,"incomplete_results":false,"items":[{"id":83222441, ...

print(response.text)
# {"total_count":3204990,"incomplete_results":false,"items":[{"id":83222441 ...

print(response.json())
# {'total_count': 3204992, 'incomplete_results': False, 'items': [{'id': 83222441, ...

print(response.ok)
# True