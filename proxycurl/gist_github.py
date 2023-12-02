import requests

response = requests.get(
    "https://gist.githubusercontent.com/EmiRoberti77/47415962c4c98682b48c2854a4cfbda6/raw/32a9d6ffa8803f68de5a9c5628711ea4622c490c/testjson.json"
)
# response.json()
name = response.json()["full_name"]
print("name", name)
