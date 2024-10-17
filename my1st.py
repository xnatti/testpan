import requests
import json

apiuser = 'thisuser'
apikey = 'masdhf-85nf-ansdf75-sadfbja43'

url = 'https://totallysecure.domain.tld/thisapi'

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
  'X-AUTH-API': 'sadfmdn-8dhbbafsdg-8n56ha67df'
}

username = 'admin'
password = 'mypasso'

response = requests.get(url, headers=headers, verify=False)
print(response)

