import requests
import json
import base64
def create_json(img_string):
    request_dict = json.loads(open('request.json').read())
    request_dict['requests'][0]['image']['content'] = img_string
    request_json_str = json.dumps(request_dict)
    with open('request.json', 'w+') as f:
        f.write(request_json_str)
        f.close()
def img_to_text(path):
    print('in the img to text func')
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    create_json(encoded_string)
    data = open('request.json', 'rb').read()
    print('Sending the requrest for text detection')
    response = requests.post(url='https://vision.googleapis.com/v1/images:annotate?key=AIzaSyC6rjZj3EDnLVVljeZ6ZGIXAID_fSe-t-0', data=data, headers={'Content-Type': 'application/json'})
    print('recieved the response for text from google')
    
    with open('response.json', 'w+') as f:
        f.write(response.text)
        f.close()
    print('wrote json file')
    response_dict = json.loads(open('response.json').read())
    print('read json file')
    print(response_dict.keys())
    print('made changes')
    print(response_dict['responses'][0] is None)
    print(response_dict['responses'][0])
    
    text = response_dict['responses'][0]['fullTextAnnotation']['text']
    print(text)
    return text
# img_to_text()
