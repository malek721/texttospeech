import playsound
from albumentations import Affine
from google.cloud import texttospeech
from pyttsx3.voice import Voice
from tensorboard.plugins.audio.summary import audio
from torch.utils.benchmark import Language
from transformers.agents.translation import LANGUAGE_CODES

client = texttospeech.TextToSpeechClient.from_service_account_file(r"C:\Users\admin\PycharmProjects\text_to_speech_project\api_service_key.json")


input_text = texttospeech.SynthesisInput(text="merhaba,arkadaşlar bugün dersimiz saat dokuzda olacak bilginiz olsun")

voice = texttospeech.VoiceSelectionParams(
    language_code="tr_TR",
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    name="tr-TR-Wavenet-E"
)

audio_config =texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    effects_profile_id=['small-bluetooth-speaker-class-device'],
    speaking_rate=1,
    pitch=1
)

response = client.synthesize_speech(input=input_text,voice=voice,audio_config=audio_config)

with open("output.mp3","wb") as output:
    output.write(response.audio_content)
    print("Audio content written to file 'output.mp3'")

# playsound.playsound(output.mp3)
