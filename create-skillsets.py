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

skillset_name="websiteskillset6"

skillset_playload = {
  "name": skillset_name,
  "description":
  "Detect sentiment, reviewer, location, key-phrases, urls",
  "skills":
  [
    {
      "@odata.type": "#Microsoft.Skills.Text.EntityRecognitionSkill",
      "name": "#1",
      "context": "/document/content",
      "categories": [
        "Person",
        "Quantity",
        "Organization",
        "URL",
        "Email",
        "Location",
        "DateTime"
      ],
      "defaultLanguageCode": "en",
      "inputs": [
        {
          "name": "text", "source": "/document/content"
        }
      ],
      "outputs": [
        {
          "name": "persons",
          "targetName": "reviewers"
        },
        {
          "name": "locations",
          "targetName": "locations"
        },
        {
          "name": "urls",
          "targetName": "urls"
        },
        {
          "name": "entities",
          "targetName": "entities"
        }
      ] 
    },
    {
      "@odata.type": "#Microsoft.Skills.Text.KeyPhraseExtractionSkill",
      "name": "#2",
      "context": "/document/content",
      "defaultLanguageCode": "en",
      "inputs": [
        {
          "name": "text", 
          "source": "/document/content"
        }
      ],
      "outputs": [
        {
          "name": "keyPhrases",
          "targetName": "keyPhrases"
        }
      ]
    },
    {
      "@odata.type": "#Microsoft.Skills.Text.SentimentSkill",
      "name": "#3",
      "context": "/document/content",
      "inputs": [
        {
            "name": "text",
            "source": "/document/content"
        }
      ],
      "outputs": [
        {
            "name": "score",
            "targetName": "reviewSentiment"
        }
      ]
    },
    {
      "@odata.type": "#Microsoft.Skills.Text.LanguageDetectionSkill",
      "name": "#4",
      "context": "/document/content",
      "inputs": [
        {
            "name": "text",
            "source": "/document/content"
        }
      ],
      "outputs": [
        {
            "name": "languageCode",
            "targetName": "Language"
        }
      ]
    }
  ],
  "cognitiveServices": {
        "@odata.type": "#Microsoft.Azure.Search.CognitiveServicesByKey",
        "description": "/subscriptions/1484da54-b9e3-424a-890b-e82ce432fe03/resourceGroups/openhack8/providers/Microsoft.CognitiveServices/accounts/openhackteam8cogsvcs",
        "key": "94625eac7b0d4a1c83a1b93123f3c0ab"
  }
}

r = requests.put(endpoint + "/skillsets/" + skillset_name, data=json.dumps(skillset_playload), headers=headers, params=params)
print(r.status_code)


