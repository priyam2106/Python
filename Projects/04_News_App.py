import requests

query = input("what type of news are you interested in today?")
api ="05c2d9389bb74537a6033f1a9d2dac4e" 

url=f"https://newsapi.org/v2/everything?q={query}&from=2025-06-10&sortBy=publishedAt&apiKey={api}"

print(url)

r = requests.get(url)
data = r.json()

articles = data["articles"]

for index,article in enumerate(articles):
    print(index+1, article["title"] , article["url"])
    
    print("\n********************************\n")