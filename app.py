from flask import Flask,jsonify, request
from dao.models import *
from flask_cors import CORS
from dao.clienteDao import ClienteDao

import os
import boto3
import secrets

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/registroPorRUT",methods=['POST'])
def registerByRUT():
    
    """
    Ruta para subir RUT
    """
    headers=request.headers
    fileName=headers.get('fileName')
    token =headers.get('token')
    print(request.files)
    if 'file' not in request.files:
        error = "Missing data source!"
        return jsonify({'error': error})
    file = request.files['file']
    destination = token+"/"+fileName
    file.save(destination)
    success = "Success!"
    s3 = boto3.resource('s3')
    data={
		'file':destination,
		'bucket':'hackbbva2021colegdaaldrut',
		'path':'users/'+destination
	}
    s3.meta.client.upload_file(data['file'],data['bucket'] , data['path'])
    clienteDao=ClienteDao()

    return jsonify({'file': success,'token':token})

@app.route("/audio",methods=['POST'])
def uploadAudio():
    """
    Ruta para subir audio de seguridad
    """
    headers=request.headers
    fileName=headers.get('fileName')
    token= secrets.token_urlsafe(128)
    print(request.files)
    if 'audio-file' not in request.files:
        error = "Missing data source!"
        return jsonify({'error': error})
    file = request.files['audio-file']
    print("File:",file)
    destination = fileName
    file.save(destination)
    success = "Success!"
    s3 = boto3.resource('s3')
    data={
		'file':destination,
		'bucket':'hackbbva2021colegdaald',
		'path':'users/'+token+'/'+fileName
	}
    s3.meta.client.upload_file(data['file'],data['bucket'] , data['path'])
    clienteDao=ClienteDao()
    cliente=Cliente(token=token,frase='https://hackbbva2021colegdaald.s3.amazonaws.com/'+data['path'])
    clienteDao.crear(cliente)
    return jsonify({'file': success,'token':token})

@app.route("/firma",methods=['POST'])
def uploadSignature():
    """
    Ruta para subir imagen de firma
    """
    headers=request.headers
    fileName=headers.get('fileName')
    token=  token =headers.get('token')
    if 'audio-file' not in request.files:
        error = "Missing data source!"
        return jsonify({'error': error})
    file = request.files['audio-file']
    destination = fileName
    file.save(destination)
    success = "Success!"
    s3 = boto3.resource('s3')
    data={
		'file':destination,
		'bucket':'hackbbva2021colegdaaldfirma',
		'path':'users/'+fileName
	}
    s3.meta.client.upload_file(data['file'],data['bucket'] , data['path'])
    return jsonify({'file': success,'token':token})

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")