import requests
import os,json

model_id = os.environ.get('NANONETS_MODEL_ID')
api_key = os.environ.get('NANONETS_API_KEY')

url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'

#data = {'file': open('REPLACE_IMAGE_PATH.jpg', 'rb'), 'modelId': ('', model_id)}

#response = requests.post(url, auth= requests.auth.HTTPBasicAuth(api_key, ''), files=data)

a = os.listdir("./test")
f = open("sub","a")
count = 0
files = []
for image in a:
        count += 1
        data = ('file',open('./test/' + image, 'rb'))
        files.append(data)
        if count % 20 == 0:
            print count
            files.append(('modelId',('', model_id)))
            response = requests.post(url, auth= requests.auth.HTTPBasicAuth(api_key, ''), files=files)
            resp = json.loads(response.text)
            for result in resp['result']:
                file_name = result['file']
                probability_arr = []
                print result['prediction']
                for p in result['prediction']:
                    probability_arr.append({"p": str(p['probability']), "l" : p['label']})
                probability_arr = sorted(probability_arr, key=lambda x: x["l"])
                line = file_name.split(".jpg")[0] + ',' + ','.join(x["p"] for x in probability_arr)
                f.write(line + "\n")
            files = []