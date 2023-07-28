from flask import Flask
from flask_restful import reqparse, Api, Resource
from dotenv import load_dotenv
import logging
import os

# load_dotenv()
# api_key = os.environ['AUDD_API_KEY']

app = Flask(__name__)
api = Api(app)
# app.logger.setLevel(logging.INFO)

parser = reqparse.RequestParser()
parser.add_argument('task')

class Message(Resource):
    def get(self):
        return {"message": 'Hello World'}
api.add_resource(Message, '/api/hello')

@app.route("/api/healthchecker", methods=["GET"])
def healthchecker():
    return {"status": "success", "message": "Integrate Flask Framework with Next.js"}

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/')
# def home():
#     app.logger.info(f'API_KEY: {api_key}')
#     return 'Hello, World!'



