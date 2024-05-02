import requests

def transcribe_audio(audio_file_path, api_key):
    url = "https://api.deepgram.com/v1/listen"
    
    headers = {
        "Authorization": f"Token {api_key}"
    }

    # Read audio file as binary data
    with open(audio_file_path, "rb") as file:
        audio_data = file.read()

    # Make a POST request to Deepgram API
    response = requests.post(url, headers=headers, data=audio_data)

    if response.status_code == 200:
        # Extract and return transcription from response
        transcription = response.json()
        return transcription
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Specify your Deepgram API key
api_key = "Your API Key"

# Specify the path to the audio file you want to transcribe
audio_file_path = "H:/Projects/AI Expert tasks/Task 1/e73c005b-f1ab-4484-a724-92a0afd3c9d2.mp3"

# Transcribe the audio
transcription = transcribe_audio(audio_file_path, api_key)

if transcription:
    print("Transcription:", transcription)
else:
    print("Transcription failed.")

