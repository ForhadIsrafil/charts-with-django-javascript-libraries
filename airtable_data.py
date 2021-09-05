import requests

'''
Base ID: ....
Table name: FRONT Image, BACK Image
API Key: ...
'''

api_key = '....'
base_id = "..."
table_name = "....a"

url = "https://api.airtable.com/v0/" + base_id + "/" + table_name
headers = {"Authorization": "Bearer " + api_key}

response = requests.get(url, headers=headers)
airtable_response = response.json()
print(airtable_response['records'][0]['fields']['FRONT Image'][0]['url'])  # [3]['fields']['Attachments'][0]['url']
records = airtable_response['records']
for data in records:
    image_url = data['fields']['FRONT Image'][0]['url']
    image_name = data['fields']['FRONT Image'][0]['filename']

# image_url = airtable_response['records'][0]['fields']['FRONT Image'][0]['url']
# image_name = airtable_response['records'][0]['fields']['FRONT Image'][0]['filename']

# image_response = requests.get(url=airtable_response['records'][3]['fields']['Attachments'][0]['url'])
    image_response = requests.get(url=image_url)
    file = open("airtable/" + image_name, "wb")
    file.write(image_response.content)
    file.close()
