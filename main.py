import requests
url = "https://restcountries.com/v3.1/name/"
country = input("indtast lande")
params= {"fulltext": "true"}
url = url + country
data = requests.get(url, params).json()


for item in data:
    for key, value in item.items():
        print(key,  value)