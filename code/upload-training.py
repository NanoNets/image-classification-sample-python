import os, requests

#mkdir images
#for i in $(cat labels); do mkdir images/$i ; done
#cat labels.csv | awk -F',' '{system("cp ./train/" $1 ".jpg ./images/" $2 "/")}'
model_id = os.environ.get('NANONETS_MODEL_ID')
api_key = os.environ.get('NANONETS_API_KEY')

url = 'https://app.nanonets.com/api/v2/ImageCategorization/UploadFile/'
images_dict = {}

with open('./labels.csv') as f:
        lines = f.readlines()
        for line in lines:
                data = line.strip('\n').split(",")
                file_name = data[0]
                label = data[1]
                if label not in images_dict:
                        images_dict[label] = []
                images_dict[label].append('./train/' + file_name + '.jpg')
        for label in images_dict:
                files = []
                for images in images_dict[label]:
                        data = ('file',open(images, 'rb'))
                        files.append(data)
                files.append(('category',('', label)))
                files.append(('modelId',('', model_id)))
                response = requests.post(url, auth= requests.auth.HTTPBasicAuth(api_key, ''), files=files)
                print(response.text)


print("\n\n\nNEXT RUN: python ./code/train-model.py")