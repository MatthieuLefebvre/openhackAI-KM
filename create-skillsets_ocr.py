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

skillset_name="websiteskillset_ocr"

skillset_payload = {
  "name": skillset_name,
  "description":
  "Detect sentiment, reviewer, location, key-phrases, urls",
  "skills":
  [
    {
      "description": "Extract text (plain and structured) from image.",
      "name": "#1",
      "@odata.type": "#Microsoft.Skills.Vision.OcrSkill",
      "context": "/document/normalized_images/*",
      "defaultLanguageCode": "en",
      "detectOrientation": "true",
      "inputs": [
        {
          "name": "image",
          "source": "/document/normalized_images/*"
        }
      ],
      "outputs": [
        {
          "name": "text", "targetName": "ocrText"
        }
      ]
    },
    {
      "@odata.type": "#Microsoft.Skills.Text.MergeSkill",
      "description": "Create merged_text, which includes all the textual representation of each image inserted at the right location in the content field.",
      "name": "#2",
      "context": "/document",
      "insertPreTag": " ",
      "insertPostTag": " ",
      "inputs": [
        {
          "name":"text", "source": "/document/content"
        },
        {
          "name": "itemsToInsert", "source": "/document/normalized_images/*/ocrText"
        },
        {
          "name":"offsets", "source": "/document/normalized_images/*/contentOffset" 
        }
      ],
      "outputs": [
        {
          "name": "mergedText", "targetName" : "merged_text"
        }
      ]
    },
    {
      "@odata.type": "#Microsoft.Skills.Text.EntityRecognitionSkill",
      "name": "#3",
      "context": "/document/merged_text",
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
          "name": "text", "source": "/document/merged_text"
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
      "name": "#4",
      "context": "/document/merged_text",
      "defaultLanguageCode": "en",
      "inputs": [
        {
          "name": "text", 
          "source": "/document/merged_text"
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
      "name": "#5",
      "context": "/document/merged_text",
      "inputs": [
        {
            "name": "text",
            "source": "/document/merged_text"
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
      "name": "#6",
      "context": "/document/merged_text",
      "inputs": [
        {
            "name": "text",
            "source": "/document/merged_text"
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

skillset_url = endpoint + "skillsets/" + skillset_name

r = requests.put(endpoint + "/skillsets/" + skillset_name, data=json.dumps(skillset_payload), headers=headers, params=params)

pprint(skillset_url)
print(r.status_code)
