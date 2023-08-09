from flask import Flask, render_template, request
from doc_summariser_functions import take_input_paragraph

app = Flask(__name__)

@app.get("/")
def summarise_page():
  return render_template('index.html')

@app.route("/summarise_txt")
def summarise_the_txt():
  input_essay = request.args.get('input_for_summarise')
  print(input_essay)
  return f"""<p class="fs-3 fw-bold">Summary</p>\n<p class="lh-sm"> {input_essay} </p>"""