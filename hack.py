import requests
import json
import os

url = "https://ssyoutube.com/api/convert"
data = {"url": "https://www.youtube.com/watch?v=DPBRGWUgQsA&list=RDcrtQSTYWtqE&index=2"}
headers = {
    "referer": "https://ssyoutube.com/en53/youtube-video-downloader"
}

array = []

x = requests.post(url, data, headers)
print(x.text)
# jsobj = json.loads(x.text)

# checkexist = os.path.isfile('./hack.json')

# if checkexist == False:
#     f = open('./hack.json', 'r')
#     array = f.read()
#     print(array)

#     with open('hack.json', 'r') as newfile:
#         print("hi")
# else:
#     f = open('./hack.json', 'r')
#     array = f.read()
#     jsonload = json.loads(array)
#     jsonarr = json.dumps(jsonload)
#     with open('hack.json', 'r') as newfile:
#         jsonarr.
