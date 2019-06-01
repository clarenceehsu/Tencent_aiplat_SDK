# _*_ coding:utf-8 _*_

import hashlib
import urllib.parse
import urllib.request
import urllib.error
import json
import time
import base64
import os

# 接口api
url_prefix = 'https://api.ai.qq.com/fcgi-bin/'


class AiPlat(object):
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.data = {}
    
    def genSignString(self, parser):
        uri_str = ''
        for key in sorted(parser.keys()):
            if key == 'app_key':
                continue
            uri_str += "%s=%s&" % (key, urllib.parse.quote(str(parser[key]), safe=''))
        sign_str = uri_str + 'app_key=' + self.app_key
        hash_md5 = hashlib.md5(sign_str.encode("latin1"))
        return hash_md5.hexdigest().upper()

    def invoke(self, params):
        self.url_data = urllib.parse.urlencode(params).encode(encoding='utf-8')
        req = urllib.request.Request(self.url, self.url_data)
        try:
            rsp = urllib.request.urlopen(req)
            str_rsp = rsp.read()
            dict_rsp = json.loads(str_rsp.decode('utf-8'))
            return dict_rsp
        except urllib.error.URLError as e:
            dict_error = {}
            if hasattr(e, "code"):
                dict_error = {}
                dict_error['ret'] = -1
                dict_error['httpcode'] = e.code
                dict_error['msg'] = "sdk http post err"
                return dict_error
            if hasattr(e, "reason"):
                dict_error['msg'] = 'sdk http post err'
                dict_error['httpcode'] = -1
                dict_error['ret'] = -1
                return dict_error

    # 智能闲聊
    def getNlpTextChat(self, question):
        self.data = {}
        self.url = url_prefix + 'nlp/nlp_textchat'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'session': 10000,
            'question': question
        }
        self.data['sign'] = self.genSignString(self.data)

        return self.invoke(self.data)["data"]["answer"]

    # 语音识别
    def aai_asr(self, filepath):  # filepath为音频文件的存档位置

        res = str(base64.b64encode(open(filepath, "rb").read()), 'utf-8')

        self.url = 'https://api.ai.qq.com/fcgi-bin/aai/aai_asr'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'format': 2,
            'speech': res,
        }
        self.data['sign'] = self.genSignString(self.data)

        return self.invoke(self.data)['data']['text']

    # 语音合成
    def aai_tts(self, sentence, filepath):  # filepath为音频文件的存档位置

        self.url = url_prefix + 'aai/aai_tts'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'speaker': 6,
            'format': 2,
            'volume': 0,
            'speed': 100,
            'text': sentence,
            'aht': 0,
            'apc': 58,
        }
        self.data['sign'] = self.genSignString(self.data)

        result = self.invoke(self.data)['data']['speech']

        with open(filepath, 'wb') as f:
            res = base64.b64decode(result)
            f.write(res)
            f.close()

    # 文字翻译
    def textTrans(self, sentence):

        self.url = url_prefix + 'nlp/nlp_texttrans'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'type': 0,  # 设置翻译模式，英译中、中译英、英汉互译
            'text': sentence,
        }
        self.data['sign'] = self.genSignString(self.data)

        return self.invoke(self.data)['data']['trans_text']

    # 语音翻译
    def speechTrans(self, filepath):  # filepath为音频文件的存档位置
        
        res = str(base64.b64encode(open(filepath, "rb").read()), 'utf-8')

        self.url = url_prefix + 'nlp/nlp_speechtranslate'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'format': 8,  # MP3
            'seq': 0,
            'end': 1,  # Finished or in line
            'seq': 0,
            'session_id': 'test1',  # Name of the sppech sequence if it occur
            'speech_chunk': res,
            'source': 'zh',  # source language
            'target': 'en',  # target language
        }
        self.data['sign'] = self.genSignString(self.data)

        return [self.invoke(self.data)['data']['source_text'], self.invoke(self.data)['data']['target_text']]

    def getAaiWxAsrs(self, filepath, speech_id, end_flag):
        self.url = url_prefix + 'aai/aai_wxasrs'
        file_len = os.path.getsize(filepath)
        res = str(base64.b64encode(open(filepath, "rb").read()), 'utf-8')

        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'format': 2,
            'rate': 16000,
            'bits': 16,
            'seq': 0,
            'len': file_len,
            'end': end_flag,
            'speech_id': speech_id,
            'speech_chunk': res,
            'cont_res': 1,
        }
        self.data['sign'] = self.genSignString(self.data)

        return self.invoke(self.data)['data']['speech_text']


client = AiPlat('', '')
print(client.textTrans('Hello'))
