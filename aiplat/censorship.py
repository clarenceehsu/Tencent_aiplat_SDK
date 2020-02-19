import time
import base64

from aiplat.base import AiPlatBase


class censorship(AiPlatBase):

    def image_terrorism(self,
                        image_path: str = None,
                        image_url: str = None):

        if image_path:
            image_path = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'image/image_terrorism'
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

    def vision_porn(self,
                    image_path: str = None,
                    image_url: str = None):

        if image_path:
            image_path = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'vision/vision_porn'
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

    def aai_evilaudio(self,
                      speech_url: str,
                      speech_id: int = 1234,
                      porn_detect: int = 1,
                      keyword_detect: int = 1):

        self.url = self.url_prefix + 'aai/aai_evilaudio'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'speech_id': speech_id,
            'speech_url': speech_url,
            'porn_detect': porn_detect,
            'keyword_detect': keyword_detect,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']
