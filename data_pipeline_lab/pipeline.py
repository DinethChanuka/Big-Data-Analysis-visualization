# This is the main pipeline file
import requests
import pandas as pd

API_URL = "https://jsonplaceholder.typicode.com/posts"

#send a request to the API and get the response

response = requests.get(API_URL, timeout=30)

#raise an error if the http was unsuccessful
response.raise_for_status()

#Convert the json response to a pandas DataFrame
data =response.json()

# Convert the records into a Pandas DataFrame
df=pd.DataFrame(data)

print(df.head())
print("Total number of records:", len(df))