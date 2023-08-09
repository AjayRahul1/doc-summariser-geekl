from flask import Flask, render_template, request
from doc_summariser_functions import take_input_essay, metrics_of_processed_essay, chatgpt_prompt_summarize_document

app = Flask(__name__)

@app.get("/")
def summarise_page():
  return render_template('index.html')

@app.route("/summarise_txt")
def summarise_the_txt():
  processed_essay = request.args.get('input_for_summarise')
  # print(input_essay)
  processed_essay = take_input_essay(processed_essay)
  
  og_essay_metrics = metrics_of_processed_essay(processed_essay)  # List has items [no_of_words, total_letters, total_digits]
  
  summary_output, summary_metrics = chatgpt_prompt_summarize_document(processed_essay)
  return f"""<p class="fs-4 fw-bold">Summary</p>\n<p class="lh-sm"> {summary_output} </p>"""