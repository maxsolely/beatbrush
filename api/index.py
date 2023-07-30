from flask import Flask, jsonify, request
from flask_restful import reqparse, Api, Resource
from dotenv import load_dotenv
from promp_templates import music_taxonomy_user_prompt, music_taxonomy_system_prompt
import logging
import os
import requests
import openai

load_dotenv()
stability_engine_id = "stable-diffusion-xl-1024-v1-0"
stability_api_host = "https://api.stability.ai"
AUDD_API_KEY = os.environ['AUDD_API_KEY']
STABILITY_KEY = os.environ['STABILITY_KEY']
openai.api_key = os.environ['OPEN_AI_KEY']

# This is one way to do it
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('task')

# OpenAi stuff
def call_chat_gpt_taxonomy(artist_name, song_title):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": music_taxonomy_system_prompt},
      {"role": "user", "content": music_taxonomy_user_prompt.format(trackTitle=song_title, artistName=artist_name)}
    ],
    max_tokens=1000,
    temperature=0
  )
  return completion


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
  json_data = response.json()
  print(json_data)
  artist_name=""
  song_title=""
  if json_data["result"] is not None:
    artist_name = json_data["result"]["artist"]
    song_title= json_data["result"]["title"]
    print(artist_name)
    print(song_title)
  # Check if the request was successful
  if response.status_code == 200:
    chat_gpt_response = call_chat_gpt_taxonomy(artist_name, song_title)
    response_string = chat_gpt_response["choices"][0]["message"]["content"]
    # remove new lines and leading/trailing spaces
    cleaned_string = " ".join(line.strip() for line in response_string.split("\n"))
    # remove the comma at the end, if any
    if cleaned_string[-1] == ',':
      cleaned_string = cleaned_string[:-1]
    print(cleaned_string)
    return jsonify(cleaned_string), 200  # Return response from API
    # return jsonify(response.json()), 200  # Return response from API
  else:
    return jsonify({'message': 'Failed to post data to API'}), 500

@app.route("/api/generate_image", methods=["GET"])
def generateImage():
  response = requests.post(
    f"{stability_api_host}/v1/generation/{stability_engine_id}/text-to-image",
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {STABILITY_KEY}"
    },
    json={
        "text_prompts": [
            {
                "text": "A lighthouse on a cliff"
            }
        ],
        "cfg_scale": 7,
        "height": 1024,
        "width": 1024,
        "samples": 1,
        "steps": 30,
    },
  )

  if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

  return response.json(), 200

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/')
# def home():
#     app.logger.info(f'API_KEY: {api_key}')
#     return 'Hello, World!'



