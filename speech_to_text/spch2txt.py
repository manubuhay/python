from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'API KEY'
url = 'URL'
# Setup Service
authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)
# Perform conversion
with open('Untitled.mp3', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()

text = res['results'][0]['alternatives'][0]['transcript']
print(text)
confidence = res['results'][0]['alternatives'][0]['confidence']
print(confidence)
with open('output.txt', 'w') as out:
    out.writelines(text)
