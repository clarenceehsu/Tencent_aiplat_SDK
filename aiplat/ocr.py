import time
import base64

from aiplat.base import AiPlatBase


class ocr(AiPlatBase):

    def ocr_idcardocr(self, image_path: str, card_type: int):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'ocr/ocr_idcardocr'
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

    def ocr_driverlicenseocr(self, image_path: str, card_type: int):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'ocr/ocr_driverlicenseocr'
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

    def ocr_generalocr(self, image_path: str):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'ocr/ocr_generalocr'
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

    def ocr_bizlicenseocr(self, image_path: str):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'ocr/ocr_bizlicenseocr'
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

    def ocr_creditcardocr(self, image_path: str):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'ocr/ocr_creditcardocr'
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

    def ocr_handwritingocr(self, image_path: str = None, image_url: str = None):

        if image_path:
            image_path = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'ocr/ocr_handwritingocr'
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

    def ocr_plateocr(self, image_path: str = None, image_url: str = None):

        if image_path:
            image_path = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'ocr/ocr_plateocr'
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

    def ocr_bcocr(self, image_path: str):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'ocr/ocr_bcocr'
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
