import json
import requests
from pprint import pprint

endpoint = 'https://qna8-asf4fhljzhdvf5w.search.windows.net/'
api_version = '?api-version=2019-05-06'
headers = {'Content-Type': 'application/json',
        'api-key': 'DF04684281C985B2D0713E2A653F45F1' }

index_name = 'websiteindex9'

index_schema = {
    "name": index_name,
    "fields": [
      {"name": "id", "type": "Edm.String", "key": "true", "filterable": "true"},
      {"name": "storage_path", "type": "Edm.String", "searchable": "true", "filterable": "true"},
      {"name": "content", "type": "Edm.String", "searchable": "true", "filterable": "true", "sortable": "true", "facetable": "false"},
      {
        "name": "languageCode",
        "type": "Edm.String",
        "searchable": "true",
        "filterable": "false",
        "facetable": "false"
      },
      {
        "name": "keyPhrases",
        "type": "Collection(Edm.String)",
        "searchable": "true",
        "filterable": "false",
        "facetable": "false"
      },
      {
        "name": "reviewers",
        "type": "Collection(Edm.String)",
        "searchable": "true",
        "sortable": "false",
        "filterable": "true",
        "facetable": "true"
      },
      {
        "name": "locations",
        "type": "Collection(Edm.String)",
        "searchable": "true",
        "sortable": "false",
        "filterable": "true",
        "facetable": "true"
      },
      {
        "name": "urls",
        "type": "Collection(Edm.String)",
        "searchable": "true",
        "sortable": "false",
        "filterable": "true",
        "facetable": "true"
      },
      {
        "name": "reviewSentiment",
        "type": "Edm.Double",
        "searchable": "false",
        "filterable": "true",
        "facetable": "false"
      },      
      {
        "name": "enriched",
        "type": "Edm.String",
        "searchable": "false",
        "filterable": "false",
        "facetable": "false"
      }      
   ]
}

url = endpoint + "indexes" + api_version
response  = requests.post(url, headers=headers, json=index_schema)
index = response.json()
pprint(index_name)