import requests
r = requests.get('https://api.github.com/events')
print("Status code:", r.status_code)
print("Response text:")
print(r.text)