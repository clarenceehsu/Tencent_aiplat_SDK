import time
import base64

from aiplat.base import AiPlatBase


class translate(AiPlatBase):

    def nlp_texttrans(self, text: str, type: int = 0):

        self.url = self.url_prefix + 'nlp/nlp_texttrans'
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

    def nlp_texttranslate(self, text: str, source: str = 'zh', target: str = 'en'):

        self.url = self.url_prefix + 'nlp/nlp_texttranslate'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'text': text,
            'source': source,
            'target': target,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    def nlp_speechtranslate(self,
                            session_id: str,
                            filepath: str,
                            format: int = 8,
                            seq: int = 0,
                            end: int = 1,
                            source: str = 'zh',
                            target: str = 'en'):

        res = str(base64.b64encode(open(filepath, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'nlp/nlp_speechtranslate'
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

    def nlp_imagetranslate(self,
                           image_path: str,
                           session_id: str,
                           scene: str = 'doc',
                           source: str = 'zh',
                           target: str = 'en'):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'nlp/nlp_imagetranslate'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'image': res,
            'session_id': session_id,
            'scene': scene,
            'source': source,
            'target': target,
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']

    def nlp_textdetect(self, text: str, candidate_langs: str = None, force: int = 0):

        self.url = self.url_prefix + 'nlp/nlp_textdetect'
        self.data = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'text': text,
            'candidate_langs': candidate_langs,
            'force': force
        }
        self.data['sign'] = self.genSignString(self.data)
        result = self.invoke(self.data)
        if result['ret']:
            return result['msg']

        return result['data']
