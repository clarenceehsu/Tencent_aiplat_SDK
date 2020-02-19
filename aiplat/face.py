import time
import base64

from aiplat.base import AiPlatBase


class face(AiPlatBase):

    def face_detectface(self, image_path: str, mode: int = 1):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'face/face_detectface'
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

    def face_detectmultiface(self, image_path: str):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'face/face_detectmultiface'
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

    def face_detectcrossageface(self, source_image: str, target_image: str):

        source_image_res = str(base64.b64encode(open(source_image, "rb").read()), 'utf-8')
        target_image_res = str(base64.b64encode(open(target_image, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'face/face_detectcrossageface'
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

    def face_faceshape(self, image_path: str, mode: int = 1):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'face/face_faceshape'
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

    def face_facecompare(self, image_a: str, image_b: str):

        image_a_res = str(base64.b64encode(open(image_a, "rb").read()), 'utf-8')
        image_b_res = str(base64.b64encode(open(image_b, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'face/face_facecompare'
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

    def face_faceidentify(self, image_path: str, group_id: str, topn: int):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'face/face_faceidentify'
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

    def face_newperson(self,
                       group_ids: str,
                       person_id: str,
                       image_path: str,
                       person_name: str,
                       tag: str):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'face/face_newperson'
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

    def face_delperson(self, person_id: str):

        self.url = self.url_prefix + 'face/face_delperson'
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

    def face_addface(self, person_id: str, image_path: str, tag: str):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'face/face_addface'
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

    def face_delface(self, person_id: str, face_ids: str):

        self.url = self.url_prefix + 'face/face_delface'
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

    def face_faceverify(self, image_path: str, person_id: str):

        res = str(base64.b64encode(open(image_path, "rb").read()), 'utf-8')
        self.url = self.url_prefix + 'face/face_faceverify'
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
