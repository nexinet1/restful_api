#

import requests

# define the API endpoint URL
url = "https://jsonplaceholder.typicode.com/posts"

# make an HTTP GET request to the API endpoint
response = requests.get(url)

# check if the request was successful (status code 200)
if response.status_code == 200:
    # print the response to the console
    print(response.json())
else:
    # print an error message
    print("Error: could not retrieve data from API")
