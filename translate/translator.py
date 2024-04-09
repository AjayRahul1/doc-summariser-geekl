from googletrans import Translator

def translate_document(document: str, *, src_lang: str = 'auto', dest_lang: str ='fr'):
  """
  It translates text in one language to another language. It currently supports `fr`ench, ``ko`rean, `ja`panese etc., Refer to the Languages Dict below.
  :return: Translator(src = source language code, dest = destination language code, origin = Original Text, text = Translated Text, pronunciation)
  """
  translator = Translator()
  return translator.translate(
    document,
    src = src_lang,
    dest = dest_lang
  )
