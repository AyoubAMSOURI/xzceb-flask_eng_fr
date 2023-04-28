'''Translate text from english to french and from french to english using IBM-WATSON'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    '''translate from english to french'''
    try:
        translation = language_translator.translate(
       text=english_text,
       model_id='en-fr').get_result()
       #frenchText = json.dumps(translation['translations'][0], indent=2, ensure_ascii=False)
        french_text = translation['translations'][0]['translation']
        return french_text
    except:
        return 'try again'
def french_to_english(french_text):
    '''translate from french to english  '''
    try:
        translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        #englishText = json.dumps(translation['translations'][0], indent=2, ensure_ascii=False)
        english_text = translation['translations'][0]['translation']
        return english_text
    except:
        return 'try again'
    