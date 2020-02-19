from __future__ import absolute_import, unicode_literals

from aiplat.asr import asr
from aiplat.ocr import ocr
from aiplat.tts import tts
from aiplat.chat import chat
from aiplat.face import face
from aiplat.picrecog import picrecog
from aiplat.semantic import semantic
from aiplat.piceffect import piceffect
from aiplat.translate import translate
from aiplat.censorship import censorship
from aiplat.textanalysis import textanalysis


class Aiplat(ocr, face, piceffect, picrecog, censorship, chat, translate, textanalysis, semantic, asr, tts):
    pass
