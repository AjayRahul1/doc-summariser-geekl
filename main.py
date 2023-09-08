from flask import Flask, render_template, request
from doc_summariser_functions import take_input_essay, metrics_of_processed_essay, chatgpt_prompt_summarize_document
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.get("/")
def summarise_page():
  return render_template('index.html')

@app.get('/input_essay_metrics')
def input_essay_metrics():
  processed_essay = request.args.get('input_for_summarise')
  processed_essay = take_input_essay(processed_essay)
  og_essay_metrics = metrics_of_processed_essay(processed_essay)  # List has items [no_of_words, total_letters, total_digits]
  return f"""{og_essay_metrics[0]} Words | {og_essay_metrics[1]} Letters | {og_essay_metrics[2]} Digits"""

@app.route("/summarise_txt")
def summarise_the_txt():
  processed_essay = request.args.get('input_for_summarise')
  processed_essay = take_input_essay(processed_essay)
  
  summary_output, summary_metrics = chatgpt_prompt_summarize_document(processed_essay)
  return render_template("htmx_templates/summary_op_with_stats.html", summary_output=summary_output, summary_metrics_word = summary_metrics[0],
                         summary_metrics_letters = summary_metrics[1], summary_metrics_digits = summary_metrics[2])