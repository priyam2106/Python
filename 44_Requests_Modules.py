import requests

r = requests.get('https://api.github.com/users/codewithharry')

with open("harry.txt","w") as f:
    f.write(r.text)