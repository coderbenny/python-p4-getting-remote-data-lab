import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content
        
    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)
    
    
resource = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
print(resource.get_response_body())
# print(resource.load_json())
