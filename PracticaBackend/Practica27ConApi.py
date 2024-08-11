import requests

api_key = ""

headers = {
    "Authorization": f"Bearer {api_key}"
}

url = 'https://pokeapi.co/api/v2/pokemon/ditto'
data = requests.get(url, headers=headers)
print(data)

if data.status_code == 200:
    data = data.json()
    print(data)
else:
    print(f"Error: {requests.Response.status_code}")