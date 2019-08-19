# _*_ coding:utf-8 _*_
import base64
import time
import os

from aiplat.base import AiPlatBase


class chat(AiPlatBase):

    def nlp_textchat(self, text, session=10000):
        self.url = self.url_prefix + 'nlp/nlp_textchat'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'session': session,
            'question': text,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']