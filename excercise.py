import requests
import json

every_politician_res = requests.get('https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json')
body = json.loads(every_politician_res.content)

# print(body)
print(body[15])

print('----------')

gov_url = body[15]['legislatures'][0]['popolo_url']
print(gov_url)

print('----------')

azerb_res = requests.get('https://cdn.rawgit.com/everypolitician/everypolitician-data/ef0b4748c61b629e9885b968dc10d583db8c822e/data/Azerbaijan/National_Assembly/ep-popolo-v1.0.json')
azerb_body = json.loads(azerb_res.content)

# print(azerb_body)

print(azerb_body['persons'][2]['name'])

poli_name = azerb_body['persons'][2]['name']