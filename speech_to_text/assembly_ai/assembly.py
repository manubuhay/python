import requests
import time
import os
import json
import pandas as pd

__version__='v1.1'
__author__='Jie Jenn'

class AssemblyAI:
    BASE_URL= "https://api.assemblyai.com/v2/"

    def __init__(self,api_key):
        self.api_key=api_key

    @property
    def headers(self):
        return {'authorization': self.api_key}

    def upload_audio_by_url(self,url_link,remove_filler_word=True,format_text=True, **kwarg):
        request_body={
            'audio_url': url_link,
            'disfluencies': remove_filler_word,
            'format_text': format_text
        }

        for key,val in kwarg.items():
            request_body[key]=val

        response=requests.post(self.BASE_URL+'transcript',headers=self.headers,json=request_body)
        return response

    def retrieve_transcript(self,transcript_id):
        response=requests.get(self.BASE_URL+'transcript/'+transcript_id,headers=self.headers)
        return response.json()