import requests
import pprint

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "userId" : "1"
}
request = requests.get(url, params=data)

print(request.status_code)
pprint.pprint(request.json())