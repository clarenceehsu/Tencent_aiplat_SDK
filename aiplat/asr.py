# _*_ coding:utf-8 _*_
import base64
import time
import os

from aiplat.base import AiPlatBase


class asr(AiPlatBase):

    def aai_asr(self, format, filepath, rate=16000):
        res = str(base64.b64encode(open(filepath, "rb").read()), 'utf-8')
        self.url = 'https://api.ai.qq.com/fcgi-bin/aai/aai_asr'
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

    def aai_asrs(self, filepath, speech_id, end, format=2, rate=16000, seq=0):
        self.url = self.url + 'aai/aai_asrs'
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

    def aai_wxasrs(self, filepath, speech_id, end, format=2, rate=16000, bits=16, seq=0, cont_res=0):
        self.url = self.url + 'aai/aai_wxasrs'
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

