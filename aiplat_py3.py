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

    # 身份证 OCR
    def ocr_idcardocr(self, image_path, card_type):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = url_prefix + 'ocr/ocr_idcardocr'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'image': res,
            'card_type': card_type,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        if result['data']['frontimage']:
            with open('frontimage.jpg', 'wb') as f:
                res = base64.b64decode(result['data']['frontimage'])
                f.write(res)
                f.close()
        if result['data']['backimage']:
            with open('backimage.jpg', 'wb') as f:
                res = base64.b64decode(result['data']['backimage'])
                f.write(res)
                f.close()

        return result['data']

    # 行驶证驾驶证 OCR
    def ocr_driverlicenseocr(self, image_path, card_type):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = url_prefix + 'ocr/ocr_driverlicenseocr'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'image': res,
            'card_type': card_type,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 通用 OCR
    def ocr_generalocr(self, image_path):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = url_prefix + 'ocr/ocr_generalocr'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'image': res,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 营业执照OCR
    def ocr_bizlicenseocr(self, image_path):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = url_prefix + 'ocr/ocr_bizlicenseocr'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'image': res,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 银行卡 OCR
    def ocr_creditcardocr(self, image_path):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = url_prefix + 'ocr/ocr_creditcardocr'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'image': res,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 手写体 OCR
    def ocr_handwritingocr(self, image_path='', image_url=''):

        if image_path:
            image_path = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = url_prefix + 'ocr/ocr_handwritingocr'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'image': image_path,
            'image_url': image_url,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 车牌 OCR
    def ocr_plateocr(self, image_path='', image_url=''):

        if image_path:
            image_path = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = url_prefix + 'ocr/ocr_plateocr'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'image': image_path,
            'image_url': image_url,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 名片 OCR
    def ocr_bcocr(self, image_path):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = url_prefix + 'ocr/ocr_bcocr'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'image': res,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 人脸检测与分析
    def face_detectface(self, image_path, mode=1):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = url_prefix + 'face/face_detectface'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'image': res,
            'mode': mode,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 多人脸检测
    def face_detectmultiface(self, image_path):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = url_prefix + 'face/face_detectmultiface'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'image': res,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 跨年龄人脸识别
    def face_detectcrossageface(self, source_image, target_image):

        source_image_res = str(base64.b64encode(open(source_image, "rb").read()), 'utf-8')
        target_image_res = str(base64.b64encode(open(target_image, "rb").read()), 'utf-8')
        self.url = url_prefix + 'face/face_detectcrossageface'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'source_image': source_image_res,
            'target_image': target_image_res,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 五官定位
    def face_faceshape(self, image_path, mode=1):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = url_prefix + 'face/face_faceshape'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'image': res,
            'mode': mode,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 人脸对比
    def face_facecompare(self, image_a, image_b):

        image_a_res = str(base64.b64encode(open(image_a, "rb").read()), 'utf-8')
        image_b_res = str(base64.b64encode(open(image_b, "rb").read()), 'utf-8')
        self.url = url_prefix + 'face/face_facecompare'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'source_image': image_a_res,
            'target_image': image_b_res,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 人脸搜索 - 人脸搜索
    def face_faceidentify(self, image_path, group_id, topn):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = url_prefix + 'face/face_faceidentify'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'image': res,
            'group_id': group_id,
            'topn': topn,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 人脸搜索 - 个体创建
    def face_newperson(self, group_ids, person_id, image_path, person_name, tag):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = url_prefix + 'face/face_newperson'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'group_ids': group_ids,
            'person_id': person_id,
            'image': res,
            'person_name': person_name,
            'tag': tag,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 人脸搜索 - 删除个体
    def face_delperson(self, person_id):

        self.url = url_prefix + 'face/face_delperson'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'person_id': person_id,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 人脸搜索 - 增加人脸
    def face_addface(self, person_id, image_path, tag):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = url_prefix + 'face/face_addface'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'person_id': person_id,
            'image': res,
            'tag': tag,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 人脸搜索 - 删除人脸
    def face_delface(self, person_id, face_ids):

        self.url = url_prefix + 'face/face_delface'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'person_id': person_id,
            'face_ids': face_ids,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 人脸验证
    def face_faceverify(self, image_path, person_id):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = url_prefix + 'face/face_faceverify'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'person_id': person_id,
            'image': res,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 智能闲聊
    def nlp_textchat(self, question):

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
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 语音识别 - echo版
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

    # 文本翻译 - AI Lab
    def textTrans(self, text, type=0):

        self.url = url_prefix + 'nlp/nlp_texttrans'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'type': type,
            'text': text,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 语音翻译
    def nlp_speechtranslate(self, session_id, filepath, format=8, seq=0, end=1, source='zh', target='en'):

        res = str(base64.b64encode(open(filepath, "rb").read()), 'utf-8')

        self.url = url_prefix + 'nlp/nlp_speechtranslate'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'format': format,
            'seq': seq,
            'end': end,
            'session_id': session_id,
            'speech_chunk': res,
            'source': source,
            'target': target,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    # 语音识别 - 流式版（WeChat AI）
    def aai_wxasrs(self, filepath, speech_id, end, format=2, rate=16000, bits=16, seq=0, cont_res=0):

        self.url = url_prefix + 'aai/aai_wxasrs'
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

    # 语音合成 - AI Lab
    def aai_tts(self, text, speaker=6, format=2, volume=0, speed=100, aht=0, apc=58):

        self.url = url_prefix + 'aai/aai_tts'
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


if __name__ == '__main__':
    client = AiPlat('', '')
    print(client.nlp_textchat('你好'))
