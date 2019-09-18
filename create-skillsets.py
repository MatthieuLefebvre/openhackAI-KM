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

skillset_name="websiteskillset4"

skillset_playload = {
  "name": skillset_name,
  "description": 
  "Extract knowledge with cognitive services",
  "skills":
  [
    {
      "@odata.type": "#Microsoft.Skills.Text.KeyPhraseExtractionSkill",
      "context": "/document",
      #"categories": [ "Organization" ],
      "defaultLanguageCode": "en",
      "inputs": [
        {
          "name": "text", "source": "/document/text"
        },
        {
          "name": "languageCode", "source": "/document/languagecode"
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
      "inputs": [
        {
          "name": "text",
          "source": "/document/content"
        }
      ],
      "outputs": [
        {
          "name": "score",
          "targetName": "mySentiment"
        }
      ]
    },
    {
      "@odata.type": "#Microsoft.Skills.Text.EntityRecognitionSkill",
      #"categories": [ "Organization" ], **All Categories
      "defaultLanguageCode": "en",
      "inputs": [
        {
          "name": "text", "source": "/document/content"
        }
      ],
      "outputs": [
        {
          "name": "organizations", "targetName": "organizations"
        },
        {
        "name": "persons",
        "targetName": "people"
      },
      {
        "name": "emails",
        "targetName": "contact"
      },
      {
        "name": "dateTimes",
        "targetName": "dates"
      },
      {
        "name": "locations",
        "targetName": "places"
      },
      {
        "name": "entities",
        "targetName": "MyEntities"
      }
      ]
    }
  ]
}

r = requests.put(endpoint + "/skillsets/" + skillset_name, data=json.dumps(skillset_playload), headers=headers, params=params)
print(r.status_code)


