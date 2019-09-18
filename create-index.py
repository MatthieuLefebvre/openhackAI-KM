import json
import requests
from pprint import pprint

endpoint = 'https://qna8-asf4fhljzhdvf5w.search.windows.net/'
api_version = '?api-version=2019-05-06'
headers = {'Content-Type': 'application/json',
        'api-key': 'DF04684281C985B2D0713E2A653F45F1' }

index_schema = {
  "name": "websiteindex7",
  "fields": [
    {
      "name": "id",
      "type": "Edm.String",
      "facetable": "false",
      "filterable": "false",
      "key": "true",
      "retrievable": "true",
      "searchable": "false",
      "sortable": "false"
      #"analyzer": "null",
      #"indexAnalyzer": "null",
      #"searchAnalyzer": "null",
      #"synonymMaps": [],
      #"fields": []
    },
    {
      "name": "url",
      "type": "Edm.String",
      "facetable": "false",
      "filterable": "true",
      "key": "false",
      "retrievable": "true",
      "searchable": "true",
      "sortable": "false",
      "analyzer": "standard.lucene"
      #"indexAnalyzer": "null",
      #"searchAnalyzer": "null",
      #"synonymMaps": [],
      #"fields": []
    },
    {
      "name": "file_name",
      "type": "Edm.String",
      "facetable": "false",
      "filterable": "false",
      "key": "false",
      "retrievable": "true",
      "searchable": "true",
      "sortable": "true",
      "analyzer": "standard.lucene"
      #"indexAnalyzer": "null",
      #"searchAnalyzer": "null",
      #"synonymMaps": [],
      #"fields": []
    },
    {
      "name": "content",
      "type": "Edm.String",
      "facetable": "false",
      "filterable": "false",
      "key": "false",
      "retrievable": "true",
      "searchable": "true",
      "sortable": "false",
      "analyzer": "standard.lucene"
      #"indexAnalyzer": "null",
      #"searchAnalyzer": "null",
      #"synonymMaps": [],
      #"fields": []
    },
    {
      "name": "size",
      "type": "Edm.Double",
      "facetable": "false",
      "filterable": "false",
      "retrievable": "true",
      "sortable": "true"
      #"analyzer": "null",
      #"indexAnalyzer": "null",
      #"searchAnalyzer": "null",
      #"synonymMaps": [],
      #"fields": []
    },
    {
      "name": "last_modified",
      "type": "Edm.DateTimeOffset",
      "facetable": "false",
      "filterable": "false",
      "retrievable": "true",
      "sortable": "true"
      #"analyzer": "null",
      #"indexAnalyzer": "null",
      #"searchAnalyzer": "null",
      #"synonymMaps": [],
      #"fields": []
    },
    {
      "name": "keyPhrases",
      "type": "Collection(Edm.String)",
      "facetable": "false",
      "filterable": "true",
      "retrievable": "true",
      "sortable": "false"
    },
    {
      "name": "mySentiment",
      "type": "Edm.Int32",
      "facetable": "false",
      "filterable": "true",
      "retrievable": "true",
      "sortable": "true"
    },
    {
      "name": "organizations",
      "type": "Edm.String",
      "facetable": "false",
      "filterable": "true",
      "retrievable": "true",
      "sortable": "true"
    },
    {
      "name": "people",
      "type": "Collection(Edm.String)",
      "facetable": "false",
      "filterable": "true",
      "retrievable": "true",
      "sortable": "false"
    },
    {
      "name": "contact",
      "type": "Collection(Edm.String)",
      "facetable": "false",
      "filterable": "true",
      "retrievable": "true",
      "sortable": "false"
    },
    {
      "name": "dates",
      "type": "Edm.DateTimeOffset",
      "facetable": "false",
      "filterable": "true",
      "retrievable": "true",
      "sortable": "true"
    },
    {
      "name": "places",
      "type": "Collection(Edm.String)",
      "facetable": "false",
      "filterable": "true",
      "retrievable": "true",
      "sortable": "false"
    },
    {
      "name": "MyEntities",
      "type": "Collection(Edm.String)",
      "facetable": "false",
      "filterable": "true",
      "retrievable": "true",
      "sortable": "false"
    }
]
  #,
  #"suggesters": [],
  #"scoringProfiles": [],
  #"defaultScoringProfile": "",
  #"corsOptions": "null",
  #"analyzers": [],
  #"charFilters": [],
  #"tokenFilters": [],
  #"tokenizers": [],
  #"@odata.etag": "\"0x8D73BBACA07BB5D\""
}

url = endpoint + "indexes" + api_version
response  = requests.post(url, headers=headers, json=index_schema)
index = response.json()
pprint(index)