from flask import Flask, render_template, request
from doc_summariser_functions import preprocess_document, summarize_document
from translate.translator import translate_document
from dotenv import load_dotenv

from translate.languages import LANGUAGES

load_dotenv()

app = Flask(__name__)

@app.get("/")
def summarise_page():
  return render_template('index.html')

@app.get("/summarise_txt")
def summarise_the_txt():
  processed_essay = request.args.get('input_for_summarise')
  processed_essay = preprocess_document(processed_essay)
  
  summary_output, summary_metrics = summarize_document(processed_essay)
  return render_template(
    "htmx_templates/summary_op_with_stats.html",
    summary_output = summary_output,
    languages=LANGUAGES,
    summary_metrics_word = summary_metrics[0], summary_metrics_letters = summary_metrics[1], summary_metrics_digits = summary_metrics[2]
  )

@app.post("/translate_summary")
def translate_summary():
  generated_summary: str = request.form.get("generated-summary")
  dest_lang = request.form.get("translate-dest-lang")
  # print(generated_summary)
  translated_summary = translate_document(generated_summary, dest_lang=dest_lang)
  # print(translated_summary)
  return translated_summary.text