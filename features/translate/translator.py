from googletrans import Translator
from typing import Optional
def translate_document(document: str, *, src_lang: Optional[str] = 'auto', dest_lang: Optional[str] ='en'):
  """
  Translate text

  It translates text in one language to another language. It currently supports `fr`ench, ``ko`rean, `ja`panese etc.,
  
  For the languages, refer to [languages.py](translate/languages.py) Dictionary

  Parameters:
  ---
  document: str
    The text to translate.
  src_lang: str (Optional, keyword argument)
    Source language of the document. Defaults to detect the language if not passed a value.
  dest_lang: str ='en'

  Returns:
  ---
  Translated(
    src: str = source language code,
    dest: str = destination language code,
    origin: str = Original Text,
    text: str = Translated Text,
    pronunciation: str = Pronunciation of Translated Text
  )
  """
  translator = Translator()
  return translator.translate(
    document,
    src = src_lang,
    dest = dest_lang
  )
