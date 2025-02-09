import json

class LanguageManager:
    def __init__(self):
        self.languages = {}
        self.current_language = 'en'
        self.load_languages()

    def load_languages(self):
        # Load language files
        with open('src/languages/en.json', 'r', encoding='utf-8') as f:
            self.languages['en'] = json.load(f)
        with open('src/languages/zh.json', 'r', encoding='utf-8') as f:
            self.languages['zh'] = json.load(f)

    def switch_language(self, lang_code):
        if lang_code in self.languages:
            self.current_language = lang_code

    def get_text(self, key):
        return self.languages[self.current_language].get(key, key)