import time
import base64

from aiplat.base import AiPlatBase


class tts(AiPlatBase):

    def aai_tts(self,
                text: str,
                speaker: int = 6,
                format: int = 2,
                volume: int = 0,
                speed: int = 100,
                aht: int = 0,
                apc: int = 58):

        self.url = self.url_prefix + 'aai/aai_tts'
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

    def aai_tta(self, text: str, model_type: int = 0, speed: int = 0):

        self.url = self.url_prefix + 'aai/aai_tta'
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
