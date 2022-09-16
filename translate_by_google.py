import googletrans
from googletrans import Translator
import langid





def translate(text):
    lang = langid.classify(text)[0]
    if lang == 'ru':
        result = translate_ru_to_en(text)
        return result
    elif lang == 'en':
        result = translate_en_to_ru(text)
        return result
    else:
        return "Ошибка. Язык не найден."


def translate_ru_to_en(text):
    translator = Translator()
    translated = translator.translate(text, src='ru', dest='en').text
    return translated


def translate_en_to_ru(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='ru').text
    return translated
