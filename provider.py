import asyncio # for googletrans
import googletrans
import deepl

class GoogleProvider:
    def __init__(self):
        self.google_client = googletrans.Translator()
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def translate(self, text, target_lang):
        a = self.google_client.translate(text, dest=target_lang)
        b = self.loop.run_until_complete(a)
        return b.src, b.text

class DeepLProvider:
    def __init__(self, auth_key):
        self.auth_key = auth_key
        self.deepl_client = deepl.Translator(self.auth_key)

    def translate(self, text, target_lang):
        if target_lang.upper() == 'EN':
            target_lang = 'EN-US'
        result = self.deepl_client.translate_text(text, target_lang=target_lang.upper())
        return result.detected_source_lang, result.text
