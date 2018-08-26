import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import sys
from flask import send_file
from flask_cors import CORS
import time
from PIL import Image
from flask import send_from_directory
import json
import cv2
import datetime
import time
import _init_paths
from main import func_to_call
import requests
import image_to_txt


app = Flask(__name__, static_folder='/home/paperspace/flask_app_hackthe6ix/', static_url_path='/home/paperspace/flask_app_hackthe6ix/uploaded_images')
IMAGE_FOLDER = '/home/paperspace/flask_app_hackthe6ix/uploaded_images'

cors = CORS(app, resources={r'/*': {"origins": '*'}})
app.config['CORS_HEADER'] = 'Content-Type'
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER


@app.route('/', methods=['POST'])
def googlePiHandler():
    itemsArr = []
    if request.method == 'POST':
        size = 0
        if str(request.get_data()) == 'mode:0':
            print ('this is mode 0')
            
            
            ts = time.time()
            st = str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H_%M_%S'))
            
            cap = cv2.VideoCapture('rtsp://localhost:2222')
            print('Captured image')
            path = '/home/paperspace/flask_app_hackthe6ix/uploaded_images/'+st+'.jpg'
            there = False
            
            while size < 70000:
                if there == True:
                    os.remove('/home/paperspace/flask_app_hackthe6ix/uploaded_images/'+st+'.jpg')
                print 'here again'
                rval, frame = cap.read()
                cv2.imwrite('/home/paperspace/flask_app_hackthe6ix/uploaded_images/'+st+'.jpg', frame)
                size = os.stat('/home/paperspace/flask_app_hackthe6ix/uploaded_images/'+st+'.jpg').st_size
                there = True
            print('About to call the func')
            result = str(func_to_call(path))
            requests.post("http://localhost:5555", data=result) 
            
            
        elif str(request.get_data()) == 'mode:1':
            print ('this is mode 1')
            
            ts = time.time()
            st = str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H_%M_%S'))
            
            cap = cv2.VideoCapture('rtsp://localhost:2222')
            path = '/home/paperspace/flask_app_hackthe6ix/uploaded_images/'+st+'.jpg'
            there = False
            
            while size < 70000:
                if there == True:
                    os.remove('/home/paperspace/flask_app_hackthe6ix/uploaded_images/'+st+'.jpg')
                print 'here again'
                rval, frame = cap.read()
                cv2.imwrite('/home/paperspace/flask_app_hackthe6ix/uploaded_images/'+st+'.jpg', frame)
                size = os.stat('/home/paperspace/flask_app_hackthe6ix/uploaded_images/'+st+'.jpg').st_size
                there = True
            result = str(image_to_txt.img_to_text(path))
            requests.post("http://localhost:5555", data=result) 

            
        
    return '''
    '''


if __name__ == '__main__':
    app.debug = True
    app.run()