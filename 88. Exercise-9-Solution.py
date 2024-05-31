import requests
import json

query = input("What type news are you ineterested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-04-30&sortBy=publishedAt&apiKey=3d8deac6d166436dba7ab018aee2e30f"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-------------------------------------------------------------------------------------------------------------")