# _*_ coding:utf-8 _*_
import base64
import time
import os

from aiplat.base import AiPlatBase


class tts(AiPlatBase):

    def aai_tts(self, text, speaker=6, format=2, volume=0, speed=100, aht=0, apc=58):
        self.url = self.url + 'aai/aai_tts'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'speaker': speaker,
            'format': format,
            'volume': volume,
            'speed': speed,
            'text': text,
            'aht': aht,
            'apc': apc,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        _data = result['data']['speech']

        with open('tts.wav', 'wb') as f:
            res = base64.b64decode(_data)
            f.write(res)
            f.close()

        return result['data']

    def aai_tta(self, text, model_type=0, speed=0):
        self.url = self.url + 'aai/aai_tta'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'text': text,
            'model_type': model_type,
            'speed': speed,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        _data = result['data']['voice']

        with open('tts.mp3', 'wb') as f:
            res = base64.b64decode(_data)
            f.write(res)
            f.close()

        return result['data']
