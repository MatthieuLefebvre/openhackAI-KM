import json
import requests
from pprint import pprint

endpoint = 'https://qna8-asf4fhljzhdvf5w.search.windows.net/'
api_version = '/docs?api-version=2019-05-06'
headers = {'Content-Type': 'application/json',
        'api-key': 'DF04684281C985B2D0713E2A653F45F1' }

index = '/azureblob-index'
query = '&top = 5'
#https://qna8-asf4fhljzhdvf5w.search.windows.net/indexes/azureblob-index/docs?api-version=2019-05-06&search=*


url = endpoint + 'indexes' + index + api_version + query
#pprint(url)
response  = requests.get(url, headers=headers)
index_list = response.json()
pprint(index_list)
