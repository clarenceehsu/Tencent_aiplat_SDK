import time
import base64

from aiplat.base import AiPlatBase


class piceffect(AiPlatBase):

    def ptu_imgfilter(self, image_path: str, filter: int = 1):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'ptu/ptu_imgfilter'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'filter': filter,
            'image': res,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']
        elif result['data']['image']:
            with open('image.jpg', 'wb') as f:
                res = base64.b64decode(result['data']['image'])
                f.write(res)
                f.close()

        return result['data']

    def vision_imgfilter(self, image_path: str, filter: int = 1, session_id: int = 1234):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'vision/vision_imgfilter'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'filter': filter,
            'image': res,
            'session_id': session_id,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']
        elif result['data']['image']:
            with open('image.jpg', 'wb') as f:
                res = base64.b64decode(result['data']['image'])
                f.write(res)
                f.close()

        return result['data']

    def ptu_facecosmetic(self, image_path: str, cosmetic: int = 1):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'ptu/ptu_facecosmetic'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'filter': filter,
            'cosmetic': cosmetic,
            'image': res,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']
        elif result['data']['image']:
            with open('image.jpg', 'wb') as f:
                res = base64.b64decode(result['data']['image'])
                f.write(res)
                f.close()

        return result['data']

    def ptu_facedecoration(self, image_path: str, decoration: int = 1):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'ptu/ptu_facedecoration'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'filter': filter,
            'decoration': decoration,
            'image': res,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']
        elif result['data']['image']:
            with open('image.jpg', 'wb') as f:
                res = base64.b64decode(result['data']['image'])
                f.write(res)
                f.close()

        return result['data']

    def ptu_facesticker(self, image_path: str, sticker: int = 1):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'ptu/ptu_facesticker'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'filter': filter,
            'sticker': sticker,
            'image': res,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']
        elif result['data']['image']:
            with open('image.jpg', 'wb') as f:
                res = base64.b64decode(result['data']['image'])
                f.write(res)
                f.close()

        return result['data']

    def ptu_faceage(self, image_path: str):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'ptu/ptu_faceage'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'filter': filter,
            'image': res,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']
        elif result['data']['image']:
            with open('image.jpg', 'wb') as f:
                res = base64.b64decode(result['data']['image'])
                f.write(res)
                f.close()

        return result['data']
