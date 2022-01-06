import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

#loading the .env file
load_dotenv()

#extracting the api key and url from the .env file
apikey = os.environ['apikey']
URL = str(os.environ['url'])
VERSION = '2018-05-01'
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_default_headers({'x-watson-learning-opt-out': "true"})

language_translator.set_service_url(URL)

languages = language_translator.list_languages().get_result()

def languages_supported():
    print(json.dumps(languages, indent=2))


def english_to_french(english_text):
    if english_text is None or not english_text.strip():
        return "Please enter text to translate"
    french_text = language_translator.translate(
    text = english_text,
    model_id='en-fr').get_result()['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    if french_text is None or not french_text.strip():
        return "Please enter text to translate"
    english_text = language_translator.translate(
    text = french_text,
    model_id='fr-en').get_result()['translations'][0]['translation']
    return english_text