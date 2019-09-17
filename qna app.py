import http.client, urllib.parse, json, time, sys



  # Represents the various elements used to create HTTP request URIs
  # for QnA Maker operations.
  # From Publish Page
  # Example: YOUR-RESOURCE-NAME.azurewebsites.net
  # CAUTION: This is not the exact value of HOST field
  # HOST trimmed to work with http library
host = "qna-8.azurewebsites.net";

  # Authorization endpoint key
  # From Publish Page
endpoint_key = "f16f0a4a-5920-4e3e-8bd3-804dd54bfdd4";

  # Management APIs postpend the version to the route
  # From Publish Page
  # Example: /knowledgebases/ZZZ15f8c-d01b-4698-a2de-85b0dbf3358c/generateAnswer
  # CAUTION: This is not the exact value after POST
  # Part of HOST is prepended to route to work with http library
route = "/qnamaker/knowledgebases/c7122a89-9c78-493d-9564-37a22dff0f23/generateAnswer";

  # JSON format for passing question to service
question = "{'question': 'How can I cancel my hotel reservation?','top': 1}";

headers = {
  'Authorization': 'EndpointKey ' + endpoint_key,
  'Content-Type': 'application/json'
}

try:
  conn = http.client.HTTPSConnection(host,port=443)

  conn.request ("POST", route,  question, headers)

  response = conn.getresponse ()

  answer = response.read ()

  print(json.dumps(json.loads(answer), indent=4))

except :
    print ("Unexpected error:", sys.exc_info()[0])
    print ("Unexpected error:", sys.exc_info()[1])