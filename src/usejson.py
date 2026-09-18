import json
from dns import recurl
# Open the file in read mode ('r')
with open("data.json", "r") as file:
    data = json.load(file)

username = data["dns"]["hurtbrain"]
recurl(username)