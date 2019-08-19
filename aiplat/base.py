# _*_ coding:utf-8 _*_

import hashlib
import urllib.parse
import urllib.request
import urllib.error
import json

# 接口api

class AiPlatBase(object):

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.data = {}
        self.url_prefix = 'https://api.ai.qq.com/fcgi-bin/'

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