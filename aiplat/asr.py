import os
import time
import base64

from aiplat.base import AiPlatBase


class asr(AiPlatBase):

    def aai_asr(self,
                format: str,
                filepath: str,
                rate: int = 16000):

        res = str(base64.b64encode(open(filepath, "rb").read()), 'utf-8')
        self.url = self.url_prefix = 'aai/aai_asr'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'format': format,
            'speech': res,
            'rate': rate,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    def aai_asrs(self,
                 filepath: str,
                 speech_id: int,
                 end: int,
                 format: int = 2,
                 rate: int = 16000,
                 seq: int = 0):

        self.url = self.url_prefix + 'aai/aai_asrs'
        file_len = os.path.getsize(filepath)
        res = str(base64.b64encode(open(filepath, "rb").read()), 'utf-8')
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'format': format,
            'rate': rate,
            'seq': seq,
            'len': file_len,
            'end': end,
            'speech_id': speech_id,
            'speech_chunk': res,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    def aai_wxasrs(self,
                   filepath: str,
                   speech_id: int,
                   end: int,
                   format: int = 2,
                   rate: int = 16000,
                   bits: int = 16,
                   seq: int = 0,
                   cont_res: int = 0):

        self.url = self.url_prefix + 'aai/aai_wxasrs'
        file_len = os.path.getsize(filepath)
        res = str(base64.b64encode(open(filepath, "rb").read()), 'utf-8')
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'format': format,
            'rate': rate,
            'bits': bits,
            'seq': seq,
            'len': file_len,
            'end': end,
            'speech_id': speech_id,
            'speech_chunk': res,
            'cont_res': cont_res,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']
