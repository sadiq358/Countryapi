import requests
url = "https://restcountries.com/v3.1/name/"
country = input("indtast land:")
# Man skal indtaste et land for at forsætte.

params= {"fulltext": "true"}
url = url + country

#Her laver jeg et API-kald:
response = requests.get(url, params=params)

if response.status_code ==200:
    data = response.json()
    country_data = data[0]
    #Her henter koden oplysninger om de forskellige informationer.
    Hovedstad = country_data.get("capital", "")
    Befolkning = country_data.get("population", "")
    Areal = country_data.get("area", "")
    Valuta = country_data.get("currencies", "")
    Sprog = country_data.get("languages","")
    Nabolande = country_data.get("borders", "")

    #Nu skal den så kunne vise de oplysninger den har om det angivende land.
    print("Information om landet:")
    print("Hovedstad:", Hovedstad[0])
    print("Areal:", "km^2")
    print("Valuta:")
    print("Sprog:")
    print("Nabolande")
else: 
    print("Fejl! Landet findes ikke.")