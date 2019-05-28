import hashlib
import urllib.parse
import urllib.request
import urllib.error
import json
import time
import base64

# 接口api
url_prefix = 'https://api.ai.qq.com/fcgi-bin/'


def setParams(array, key, value):
    array[key] = value


def genSignString(parser):
    uri_str = ''
    for key in sorted(parser.keys()):
        if key == 'app_key':
            continue
        uri_str += "%s=%s&" % (key, urllib.parse.quote(str(parser[key]), safe=''))
    sign_str = uri_str + 'app_key=' + parser['app_key']

    hash_md5 = hashlib.md5(sign_str.encode("latin1"))
    return hash_md5.hexdigest().upper()


class AiPlat(object):
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.data = {}

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
    def getNlpTextChat(self, session, question):
        self.data = {}
        self.url = url_prefix + 'nlp/nlp_textchat'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        setParams(self.data, 'session', session)
        setParams(self.data, 'question', question)
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)

        return self.invoke(self.data)["data"]["answer"]

    # 语音识别
    def aai_asr(self, filepath):  # filepath为音频文件的存档位置

        with open(filepath, 'r') as f:
            result = f.read()
            res = base64.b64decode(result)
            f.close()

        self.data = {}
        self.url = url_prefix + 'aai/aai_asr'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        setParams(self.data, 'format', 2)
        setParams(self.data, 'speech', res)
        setParams(self.data, 'rate', 16000)

        return self.invoke(self.data)['data']['text']

    # 语音合成
    def aai_tts(self, sentence, filepath):  # filepath为音频文件的存档位置
        
        self.data = {}
        self.url = url_prefix + 'aai/aai_tts'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        setParams(self.data, 'speaker', 1)
        setParams(self.data, 'format', 2)
        setParams(self.data, 'volume', 0)
        setParams(self.data, 'speed', 100)
        setParams(self.data, 'text', sentence)
        setParams(self.data, 'aht', 0)
        setParams(self.data, 'apc', 58)
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)

        result = self.invoke(self.data)['data']['speech']

        with open(filepath, 'wb') as f:
            res = base64.b64decode(result)
            f.write(res)
            f.close()

    # 文字翻译
    def textTrans(self, sentence):  # filepath为音频文件的存档位置
        self.data = {}
        self.url = url_prefix + 'nlp/nlp_texttrans'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        setParams(self.data, 'type', 0)
        setParams(self.data, 'text', sentence)
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)

        return self.invoke(self.data)['data']['trans_text']

    # 语音翻译
    def speechTrans(self, filepath):  # filepath为音频文件的存档位置
        
        with open(filepath, 'r') as f:
            result = f.read()
            res = base64.b64decode(result)
            f.close()
        
        self.data = {}
        self.url = url_prefix + 'nlp/nlp_speechtranslate'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        setParams(self.data, 'format', 8)  # MP3
        setParams(self.data, 'seq', 0)
        setParams(self.data, 'end', 1)  # Finished or in line
        setParams(self.data, 'seq', 0)
        setParams(self.data, 'session_id', 'test1')  # Name of the sppech sequence if it occur
        setParams(self.data, 'speech_chunk', res)
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        setParams(self.data, 'source', 'zh')  # source language
        setParams(self.data, 'target', 'en')  # target language

        return [self.invoke(self.data)['data']['source_text'], self.invoke(self.data)['data']['target_text']]
