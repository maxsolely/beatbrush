from flask import Flask, jsonify, request
from flask_restful import reqparse, Api, Resource
from dotenv import load_dotenv
import logging
import os
import requests

load_dotenv()
AUDD_API_KEY = os.environ['AUDD_API_KEY']

# This is one way to do it
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('task')

class Message(Resource):
    def get(self):
        return {"message": 'Hello World'}
api.add_resource(Message, '/api/hello')

# This is another way to handle routes
@app.route("/api/healthchecker", methods=["GET"])
def healthchecker():
    return {"status": "success", "message": "Integrate Flask Framework with Next.js"}

@app.route("/api/identify_track", methods=[ "POST"])
def identify_track():
  # get data from the POST request
  audio_file = request.files['audio']
  audio_file.save("audio.webm")

  url = "https://api.audd.io/"
  payload = {
    'api_token': AUDD_API_KEY,
    'return': 'spotify',
    'method': 'recognize'
  }

  files = {
    'file': open('audio.webm', 'rb')
  }

  response = requests.post(url, data=payload, files=files)
  # Check if the request was successful
  if response.status_code == 200:
    return jsonify(response.json()), 200  # Return response from API
  else:
    return jsonify({'message': 'Failed to post data to API'}), 500


if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/')
# def home():
#     app.logger.info(f'API_KEY: {api_key}')
#     return 'Hello, World!'



