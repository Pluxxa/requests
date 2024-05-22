import requests
import pprint

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 3
}
request = requests.get(url, data=data)

print(request.status_code)
pprint.pprint(request.json())