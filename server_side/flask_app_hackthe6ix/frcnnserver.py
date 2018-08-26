import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import sys
sys.path.insert(0, '/home/paperspace/dev/caffe/examples')
import fasterRCNNVideo
from flask import send_file
from flask_cors import CORS
import time
from PIL import Image
from flask import send_from_directory


#Setting static path to uploadResults so I can get URLs for the analyzed videos and send it back to react
app = Flask(__name__, static_folder='/home/paperspace/dev/temp', static_url_path='/home/paperspace/dev/temp')


UPLOAD_FOLDER = '/home/paperspace/dev/temp'
ALLOWED_VIDEO_EXTENSIONS = set(['mp4','avi'])

cors = CORS(app, resources={r'/*': {"origins": '*'}})
app.config['CORS_HEADER'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    
def allowed_video_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_VIDEO_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_video_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            uploadPath = UPLOAD_FOLDER+'/'+filename
            resultPath, jsonString = fasterRCNNVideo.runRCNN(uploadPath,os.path.splitext(filename)[0])
            return jsonString
                                  
            
       
    #redirect(url_for('uploadPath',
                                    #filename=filename))  
        
    #TODO: if file uploaded is a video, call the ssd_detect_video script to analyze the video   
    
    
        
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
if __name__ == '__main__':
    app.debug = True
    app.run()