import requests

url = "https://api.github.com"
data = {
    "q" : ""
}
request = requests.get(url, params=data)

print(request.status_code)
print(request.json())