import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

""" Module for translating between french and english """

def create_translator_instance():
    """
    Use environment variables to instantiate Watson Language Translator service
    """
    load_dotenv()

    apikey = os.environ['apikey']
    url = os.environ['url']

    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2021-02-10',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)
    return language_translator


# Create Language Translator instance
language_translator = create_translator_instance()


def english_to_french(english_text):
    """
    Transtlate englishText to french using Watson Language Translator
    :param: englishText: String of well-formed english to translate.
    :return: String of french text translated from english.
    """
    if not english_text:
        return ''
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return translation['translations'][0]['translation']


def french_to_english(french_text):
    """
    Transtlate englishText to french using Watson Language Translator
    :param: englishText: String of well-formed english to translate.
    :return: String of french text translated from english.
    """
    if not french_text:
        return ''

    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return translation['translations'][0]['translation']


def get_languages():
    """
    Get json of all available languages in Watson Language Translator
    """
    languages = language_translator.list_languages().get_result()
    return languages
