# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from aiplat.base import AiPlatBase
from aiplat.ocr import ocr
from aiplat.face import face
from aiplat.piceffect import piceffect
from aiplat.picrecog import picrecog
from aiplat.censorship import censorship
from aiplat.chat import chat
from aiplat.translate import translate
from aiplat.textanalysis import textanalysis
from aiplat.semantic import semantic
from aiplat.asr import asr
from aiplat.tts import tts


class Aiplat(AiPlatBase):

    def ocr_idcardocr(self, image_path, card_type):
        # 身份证 OCR
        return ocr.ocr_idcardocr(self, image_path, card_type)

    def ocr_driverlicenseocr(self, image_path, card_type):
        # 行驶证驾驶证 OCR
        return ocr.ocr_driverlicenseocr(self, image_path, card_type)

    def ocr_generalocr(self, image_path):
        # 通用 OCR
        return ocr.ocr_generalocr(self, image_path)

    def ocr_bizlicenseocr(self, image_path):
        # 营业执照 OCR
        return ocr.ocr_bizlicenseocr(self, image_path)

    def ocr_creditcardocr(self, image_path):
        # 银行卡 OCR
        return ocr.ocr_creditcardocr(self, image_path)

    def ocr_handwritingocr(self, image_path='', image_url=''):
        # 手写体 OCR
        return ocr.ocr_handwritingocr(self, image_path, image_url)

    def ocr_plateocr(self, image_path='', image_url=''):
        # 车牌 OCR
        return ocr.ocr_plateocr(self, image_path, image_url)

    def ocr_bcocr(self, image_path):
        # 名片 OCR
        return ocr_bcocr(self, image_path)

    def face_detectface(self, image_path, mode=1):
        # 人脸检测与分析
        return face.face_detectface(self, image_path, mode)

    def face_detectmultiface(self, image_path):
        # 多人脸检测
        return face.face_detectmultiface(self, image_path)

    def face_detectcrossageface(self, source_image, target_image):
        # 跨年龄人脸识别
        return face.face_detectcrossageface(self, source_image, target_image)

    def face_faceshape(self, image_path, mode=1):
        # 五官定位
        return face.face_faceshape(self, image_path, mode)

    def face_facecompare(self, image_a, image_b):
        # 人脸对比
        return face.face_facecompare(self, image_a, image_b)

    def face_faceidentify(self, image_path, group_id, topn):
        # 人脸搜索 - 人脸搜索
        return face.face_faceidentify(self, image_path, group_id, topn)

    def face_newperson(self, group_ids, person_id, image_path, person_name, tag):
        # 人脸搜索 - 个体创建
        return face.face_newperson(self, group_ids, person_id, image_path, person_name, tag)

    def face_delperson(self, person_id):
        # 人脸搜索 - 删除个体
        return face.face_delperson(self, person_id)

    def face_addface(self, person_id, image_path, tag):
        # 人脸搜索 - 增加人脸
        return face.face_addface(self, person_id, image_path, tag)

    def face_delface(self, person_id, face_ids):
        # 人脸搜索 - 删除人脸
        return face.face_delface(self, person_id, face_ids)

    def face_faceverify(self, image_path, person_id):
        # 人脸验证
        return face.face_faceverify(self, image_path, person_id)

    def ptu_imgfilter(self, image_path, filter=1):
        # 图片滤镜（天天P图）
        return piceffect.ptu_imgfilter(self, image_path, filter)

    def vision_imgfilter(self, image_path, filter=1, session_id=1234):
        # 图片滤镜（AI Lab）
        return piceffect.vision_imgfilter(self, image_path, filter, session_id)

    def ptu_facecosmetic(self, image_path, cosmetic=1):
        # 人脸美妆
        return piceffect.ptu_facecosmetic(self, image_path, cosmetic)

    def ptu_facedecoration(self, image_path, decoration=1):
        # 人脸变妆
        return piceffect.ptu_facedecoration(self, image_path, decoration)

    def ptu_facesticker(self, image_path, sticker=1):
        # 大头贴
        return piceffect.ptu_facesticker(self, image_path, sticker)

    def ptu_faceage(self, image_path):
        # 颜龄检测
        return piceffect.ptu_faceage(self, image_path)

    def vision_imgtotext(self, image_path, session_id=1234):
        # 看图说话
        return picrecog.vision_imgtotext(self, image_path, session_id)

    def image_tag(self, image_path):
        # 多标签识别
        return picrecog.image_tag(self, image_path)

    def image_fuzzy(self, image_path):
        # 模糊图片检测
        return picrecog.image_fuzzy(self, image_path)

    def image_food(self, image_path):
        # 美食图片识别
        return picrecog.image_food(self, image_path)

    def vision_scener(self, image_path, topk=1):
        # 场景识别
        return picrecog.vision_scener(self, image_path, topk)

    def vision_objectr(self, image_path, topk=1, format=1):
        # 物体识别
        return picrecog.vision_objectr(self, image_path, topk, format)

    def image_terrorism(self, image_path='', image_url=''):
        # 暴恐识别
        return censorship.image_terrorism(self, image_path, image_url)

    def vision_porn(self, image_path='', image_url=''):
        # 图片鉴黄
        return censorship.vision_porn(self, image_path, image_url)

    def aai_evilaudio(self, speech_url, speech_id=1234, porn_detect=1, keyword_detect=1):
        # 音频鉴黄/音频敏感词检测
        return censorship.aai_evilaudio(self, speech_url, speech_id, porn_detect, keyword_detect)

    def nlp_textchat(self, text, session=10000):
        # 智能闲聊
        return chat.nlp_textchat(self, text, session)

    def nlp_texttrans(self, text, type=0):
        # 文本翻译（AI Lab）
        return translate.nlp_texttrans(self, text, type)

    def nlp_texttranslate(self, text, source='zh', target='en'):
        # 文本翻译（翻译君）
        return translate.nlp_texttranslate(self, text, source, target)

    def nlp_speechtranslate(self, session_id, filepath, format=8, seq=0, end=1, source='zh', target='en'):
        # 语音翻译
        return translate.nlp_speechtranslate(self, session_id, filepath, format, seq, end, source, target)

    def nlp_imagetranslate(self, image_path, session_id=1234, scene='doc', source='zh', target='en'):
        # 图片翻译
        return translate.nlp_imagetranslate(self, image_path, session_id, scene, source, target)

    def nlp_textdetect(self, text, candidate_langs='', force=0):
        # 语种识别
        return nlp_textdetect(self, text, candidate_langs, force)

    def nlp_wordseg(self, text):
        # 分词
        return textanalysis.nlp_wordseg(self, text)

    def nlp_wordpos(self, text):
        # 词性
        return textanalysis.nlp_wordpos(self, text)

    def nlp_wordner(self, text):
        # 专有名词
        return textanalysis.nlp_wordner(self, text)

    def nlp_wordsyn(self, text):
        # 同义词
        return textanalysis.nlp_wordsyn(self, text)

    def nlp_textpolar(self, text):
        # 情感分析
        return semantic.nlp_textpolar(self, text)

    def aai_asr(self, format, filepath, rate=16000):
        # 语音识别 - echo版
        return asr.aai_asr(self, format, filepath, rate)

    def aai_asrs(self, filepath, speech_id, end, format=2, rate=16000, seq=0):
        # 语音识别 - 流式版（AI Lab）
        return asr.aai_asrs(self, filepath, speech_id, end, format, rate, seq)

    def aai_wxasrs(self, filepath, speech_id, end, format=2, rate=16000, bits=16, seq=0, cont_res=0):
        # 语音识别 - 流式版(WeChat AI)
        return asr.aai_wxasrs(self, filepath, speech_id, end, format, rate, bits, seq, cont_res)

    def aai_tts(self, text, speaker=6, format=2, volume=0, speed=100, aht=0, apc=58):
        # 语音合成 - AI Lab
        return tts.aai_tts(self, text, speaker, format, volume, speed, aht, apc)

    def aai_tta(self, text, model_type=0, speed=0):
        # 语音合成（优图）
        return tts.aai_tta(self, text, model_type, speed)
