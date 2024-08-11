import requests

api_key = "7ceb12eb0d07394348e79bad0f0e72395feee482"

headers = {
    "Authorization": f"Bearer {api_key}"
}

url = 'https://developer.marvel.com/'
data = requests.get(url, headers=headers)
print(data)

if data.status_code == 200:
    data = data.json()
    print(data)
else:
    print(f"Error: {requests.Response.status_code}")