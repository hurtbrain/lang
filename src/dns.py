import requests
def recurl(url):
    globals()[theurl] = url
# Define the raw GitHub URL and the local filename you want to save it as
local_filename = "index.json"

# Send a GET request to the URL
response = requests.get(theurl)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Write the content to a local file in binary mode
    with open(local_filename, "wb") as file:
        file.write(response.content)
    print(f"File downloaded successfully as {local_filename}")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
