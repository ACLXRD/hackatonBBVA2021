from flask import Flask,jsonify, request
from dao.models import *
from flask_cors import CORS

import os
import boto3

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

bucketname=''
@app.route("/registroPorRUT",methods=['POST'])
def registerByRUT():
    
    """
    Ruta para subir imágenes de productos
    """
    headers=request.headers
    fileName=headers.get('fileName')
    print(request.files)
    if 'file' not in request.files:
        error = "Missing data source!"
        return jsonify({'error': error})
    file = request.files['file']
    destination = '/tmp/'+fileName
    file.save(destination)
    success = "Success!"
    s3 = boto3.resource('s3')
    data={
		'file':destination,
		'bucket':bucketname,
		'path':'users/'+fileName
	}
    s3.meta.client.upload_file(data['file'],data['bucket'] , data['path'])
    return jsonify({'file': success})


if __name__=="__main__":
    app.run(debug=True)