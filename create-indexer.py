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

indexer_name = 'websiteindexer8'
datasource_name = 'openhackteam8'
index_name = 'websiteindex7'
skillset_name = 'websiteskillset4'


indexer_payload = {
    "name": indexer_name,
    "dataSourceName": datasource_name,
    "targetIndexName": index_name,
     "fieldMappings" : [
    {
      "sourceFieldName" : "metadata_storage_path",
      "targetFieldName" : "id",
      "mappingFunction" :
        { "name" : "base64Encode" }
    },
    {
      "sourceFieldName" : "metadata_storage_size",
      "targetFieldName" : "size"
    },
    {
      "sourceFieldName" : "metadata_storage_path",
      "targetFieldName" : "url"
    },
    {
      "sourceFieldName" : "metadata_storage_last_modified",
      "targetFieldName" : "last_modified"
    },
     {
      "sourceFieldName" : "metadata_storage_name",
      "targetFieldName" : "file_name"
    }
  ],
   "outputFieldMappings" :
  [
        {
          "sourceFieldName" : "/document/pages/*/keyPhrases/*",
          "targetFieldName" : "keyPhrases"
        },  
        {
            "sourceFieldName": "/document/sentiment",
            "targetFieldName": "MySentiment"
        },     
        {
          "sourceFieldName" : "/document/organizations",
          "targetFieldName" : "organizations"
        },
        {
          "sourceFieldName" : "/document/people",
          "targetFieldName" : "people"
        },
        {
          "sourceFieldName" : "/document/contact",
          "targetFieldName" : "contact"
        },
         {
          "sourceFieldName" : "/document/dates",
          "targetFieldName" : "dates"
        },
         {
          "sourceFieldName" : "/document/places",
          "targetFieldName" : "places"
        }
        ,
         {
          "sourceFieldName" : "/document/MyEntities",
          "targetFieldName" : "MyEntities"
        }


  ],
}

r = requests.put(endpoint + "/indexers/" + indexer_name, data=json.dumps(indexer_payload), headers=headers, params=params)
print(r.status_code)

#Indexer status
#r = requests.get(endpoint + "/indexers/" + indexer_name + "/status", headers=headers,params=params)
#pprint(json.dumps(r.json(), indent=1))