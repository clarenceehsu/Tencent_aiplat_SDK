# _*_ coding:utf-8 _*_
import base64
import time
import os

from aiplat.base import AiPlatBase


class picrecog(AiPlatBase):

    def vision_imgtotext(self, image_path, session_id=1234):
        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url + 'vision/vision_imgtotext'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'image': res,
            'session_id': session_id,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    def image_tag(self, image_path):
        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url + 'image/image_tag'
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

    def image_fuzzy(self, image_path):
        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url + 'image/image_fuzzy'
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

    def image_food(self, image_path):
        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url + 'image/image_food'
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

    def vision_scener(self, image_path, topk=1):
        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url + 'vision/vision_scener'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'topk': topk,
            'image': res,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    def vision_objectr(self, image_path, topk=1, format=1):
        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url + 'vision/vision_objectr'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'format': format,
            'topk': topk,
            'image': res,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']
