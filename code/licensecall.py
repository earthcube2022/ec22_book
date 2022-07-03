import requests

response = requests.get('/api/licenses/')
print(response.json())



