import requests
url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=971c0d9026bd4952b3258c2665adcec7')
response = requests.get(url)
print(response.json())