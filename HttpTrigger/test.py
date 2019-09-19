import logging
#import azure.functions as func
import json
#import pandas as pd
from string import punctuation
from collections import Counter

#with open("json_playload_test.json", "r") as read_file:
#    json_playload = json.load(read_file)

'''
json_playload = {
    "values": [
        {
            "recordId": "a1",
            "data":
            {
               "text":  "Tiger, tiger burning bright in the darkness of the night.",
               "language": "en"
            }
        },
        {
            "recordId": "a2",
            "data":
            {
               "text":  "The rain in spain stays mainly in the plains! That's where you'll find the rain!",
               "language": "en"
            }
        }
   ]
}
'''
json_playload = '{"values": [ {"recordId": "a1","data":{"text":  "Tiger, tiger burning bright in the darkness of the night.","language": "en"}},{"recordId": "a2","data":{"text":  "The rain in spain stays mainly in the plains! That\'s where you\'ll find the rain!","language": "en"}}]}'


def run(json_data):

   # Array of stop words to be ignored
    stopwords = ['', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 
    "youre", "youve", "youll", "youd", 'your', 'yours', 'yourself', 
    'yourselves', 'he', 'him', 'his', 'himself', 'she', "shes", 'her', 
    'hers', 'herself', 'it', "its", 'itself', 'they', 'them', 
    'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 
    'this', 'that', "thatll", 'these', 'those', 'am', 'is', 'are', 'was',
    'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 
    'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 
    'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 
    'about', 'against', 'between', 'into', 'through', 'during', 'before', 
    'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 
    'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 
    'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 
    'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 
    'only', 'own', 'same', 'so', 'than', 'too', 'very', 'can', 'will',
    'just', "dont", 'should', "shouldve", 'now', "arent", "couldnt", 
    "didnt", "doesnt", "hadnt", "hasnt", "havent", "isnt", "mightnt", "mustnt",
    "neednt", "shant", "shouldnt", "wasnt", "werent", "wont", "wouldnt", "shall"]

 # Get the values from input json
    toBeCleanedValues = json.loads(json_data)['values']

 # Prepare the output
    results = {}
    results["values"] = []

    # Empty JSON structure in which to return the results
    result_json = {"words":[]}

# Clean each value - Assuming there will be more key phrases / Entities than terms
    for value in toBeCleanedValues:
        recordId = value['recordId']
        text = value['data']['text']
        # Count the words and get the most common 10
        wordcount = Counter(text.split()).most_common(10)
        words = [w[0] for w in wordcount]

        # Add the top 10 words to the output for this text record
        result_json["words"] = words

        try:
            results["values"].append(
            {
            "recordId": recordId,
            "word": result_json,
            "data": {
                "text": text
                    },
                "errors": None,
                "warnings": None
            })
        except:
            results["values"].append(
            {
            "recordId": recordId,
            "word":result_json,
            "data": {
                "text": ""
                    },
                "errors": "Error while appending the cleaned term to the output",
                "warnings": None
            })
            
    return str(results)

test_result = run(json_playload)

print(json.dumps(test_result))

