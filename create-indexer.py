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

indexer_name = 'websiteindexer9'
datasource_name = 'openhackteam8'
index_name = 'websiteindex9'
skillset_name = 'websiteskillset6'


indexer_payload = {
    "name": indexer_name,
    "dataSourceName": datasource_name,
    "targetIndexName": index_name,
    "skillsetName" : skillset_name,
     "fieldMappings" : [
        {
        "sourceFieldName" : "metadata_storage_path",
        "targetFieldName" : "id",
        "mappingFunction" : { "name" : "base64Encode" }
      },
      {
        "sourceFieldName" : "metadata_storage_path",
        "targetFieldName" : "storage_path"
      },
      {
        "sourceFieldName" : "content",
        "targetFieldName" : "content"
      }
    ],
    "outputFieldMappings" : [
      {
        "sourceFieldName" : "/document/content/reviewers",
        "targetFieldName" : "reviewers"
      },
      {
        "sourceFieldName" : "/document/content/locations",
        "targetFieldName" : "locations"
      },
      {
        "sourceFieldName" : "/document/content/urls",
        "targetFieldName" : "urls"
      },
      {
        "sourceFieldName" : "/document/content/keyPhrases",
        "targetFieldName" : "keyPhrases"
      },
      {
        "sourceFieldName" : "/document/content/reviewSentiment",
        "targetFieldName" : "reviewSentiment"
      }
    ],
    "parameters": {
        "maxFailedItems":-1,
        "maxFailedItemsPerBatch":-1,
        "configuration": {
            "dataToExtract": "contentAndMetadata",
            "imageAction": "generateNormalizedImages"
        }
    }
}

r = requests.put(endpoint + "/indexers/" + indexer_name, data=json.dumps(indexer_payload), headers=headers, params=params)
#index = response.json()
print(r.status_code)
#pprint(index)

#r = requests.put(endpoint + "/indexers/" + indexer_name, data=json.dumps(indexer_payload), headers=headers, params=params)
#print(r.status_code)

#Indexer status
#r = requests.get(endpoint + "/indexers/" + indexer_name + "/status", headers=headers,params=params)
#pprint(json.dumps(r.json(), indent=1))