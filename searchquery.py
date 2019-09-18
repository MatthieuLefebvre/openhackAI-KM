import json
import requests
from pprint import pprint


#Setup the endpoint
endpoint = 'https://qna8-asf4fhljzhdvf5w.search.windows.net/'
headers = {'Content-Type': 'application/json',
        'api-key': 'DF04684281C985B2D0713E2A653F45F1' }
params = {
    'api-version': '2019-05-06'
}


index_name = 'websiteindex4'

#searchstring = "/docs&search=New York&$count=true&$select=file_name, url, size, last_modified"
searchstring = "/docs&search=New York&$count=true&$select=*"

#Query the index for all fields
#r = requests.get(endpoint + "/indexes/" + index_name, headers=headers,params=params)
#print(json.dumps(r.json(), indent=1))

#New York Query
#r = requests.get(endpoint + "/indexes/" + index_name + "/docs?&search=" + "New York" + "&$count=true&$select=file_name, url, size, last_modified", headers=headers, params=params)
#pprint(r.json())

#London Query
#r = requests.get(endpoint + "/indexes/" + index_name + "/docs?&search=" + "London" + "Buckingham Palace"+ "&$count=true&$select=file_name, url, size, last_modified", headers=headers, params=params)
#pprint(r.json())

#Las Vegas Query match with url = reviews
#r = requests.get(endpoint + "/indexes/" + index_name + "/docs?&search=Las Vegas"+ "&$count=true&$select=file_name, url, size, last_modified&$filter=search.ismatch(" + "'reviews','url')", headers=headers, params=params)
#pprint(r.json())


#Las Vegas Query do not match with url = reviews
r = requests.get(endpoint + "/indexes/" + index_name + "/docs?&search=Las Vegas"+ "&$count=true&$select=file_name, url, size, last_modified&$filter=not search.ismatch(" + "'reviews','url')", headers=headers, params=params)
pprint(r.json())

#r = requests.get(endpoint + "/indexes/" + index_name + searchstring, headers=headers, params=params)
#pprint(r.json())