from flask import Flask, request, redirect, url_for
import os
import requests
import subprocess, sys
from google.cloud import texttospeech

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        print (request.get_data())
        if type(request.get_data()) == str:
            print (request.get_data())
            speech = request.get_data()
            # Instantiates a client
            client = texttospeech.TextToSpeechClient()

            # Set the text input to be synthesized
            synthesis_input = texttospeech.types.SynthesisInput(text=speech)

            # Build the voice request, select the language code ("en-US") and the ssml
            # voice gender ("neutral")
            voice = texttospeech.types.VoiceSelectionParams(
                language_code='en-US',
                ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

            # Select the type of audio file you want returned
            audio_config = texttospeech.types.AudioConfig(
                audio_encoding=texttospeech.enums.AudioEncoding.MP3)

            # Perform the text-to-speech request on the text input with the selected
            # voice parameters and audio file type
            response = client.synthesize_speech(synthesis_input, voice, audio_config)

            # The response's audio_content is binary.
            with open('output.mp3', 'wb') as out:
                # Write the response to the output file.
                out.write(response.audio_content)
                print('Audio content written to file "output.mp3"')
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, 'output.mp3'])
            os.remove('output.mp3')
    return 'Playing the audio now'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
