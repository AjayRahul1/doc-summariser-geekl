from flask import Flask, render_template, request, jsonify, send_file
from doc_summariser_functions import preprocess_document, summarize_document
from features.translate.translator import translate_document
from features.removebg import removebg_image
from dotenv import load_dotenv
from werkzeug.utils import secure_filename # create a secure_filename for no overwrites
import os

from features.translate.languages import LANGUAGES

load_dotenv()

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['REMOVE_BG_IMGS_DIR'] = 'no_bg_imgs'

@app.route("/", methods=["GET"])
def summarise_page():
  return render_template('index.html')

@app.route("/removebg", methods=["GET"])
def home_removebg():
  return render_template("removebg-home.html")

@app.get("/summarise_txt")
def summarise_the_txt():
  print("Summarising the text...")
  processed_essay = request.args.get('input_for_summarise')
  processed_essay = preprocess_document(processed_essay)
  
  summary_output, summary_metrics = summarize_document(processed_essay)
  return render_template(
    "htmx_templates/summary_op_with_stats.html",
    summary_output = summary_output,
    languages=LANGUAGES,
    summary_metrics_word = summary_metrics[0], summary_metrics_letters = summary_metrics[1], summary_metrics_digits = summary_metrics[2]
  )

# @app.post("/summarise_document")
# def summarise_document():
#   processed_essay = request.json['input_for_summarise']
#   processed_essay = preprocess_document(processed_essay)
  
#   summary_output, summary_metrics = summarize_document(processed_essay)
#   return jsonify({
#     "summary_output": summary_output,
#     "summary_metrics_word" : summary_metrics[0],
#     "summary_metrics_letters": summary_metrics[1],
#     "summary_metrics_digits": summary_metrics[2]
#   })

@app.post("/translate_summary")
def translate_summary():
  generated_summary: str = request.form.get("generated-summary")
  dest_lang = request.form.get("translate-dest-lang")
  # print(generated_summary)
  translated_summary = translate_document(generated_summary, dest_lang=dest_lang)
  # print(translated_summary)
  return translated_summary.text

@app.route('/remove_bg_process', methods=['POST'])
def remove_bg_img_process():
  if 'file' not in request.files: return jsonify({'error': 'No file part'})

  file = request.files['file']

  if file.filename == '':
    return jsonify({'error': 'No selected file'})

  # Generate a unique filename to prevent overwriting
  filename = secure_filename(file.filename)
  filename = file.filename
  upload_img_fp = os.path.join(app.config['UPLOAD_FOLDER'], filename)
  file.save(upload_img_fp)

  # Removing Background of the image
  try:
    import PIL
    rmbg_img = removebg_image(upload_img_fp)

    # Save the file to the response_images folder
    response_image_path = os.path.join(app.config['REMOVE_BG_IMGS_DIR'], (filename.split('.')[0] + "_NoBG.png"))
    rmbg_img.save(response_image_path)

    print(response_image_path)
    print(str(response_image_path))

  except PIL.UnidentifiedImageError:
    print("Unable to open the image due to unsupported type.")
  finally:
    os.remove(upload_img_fp)
    print("Removed the uploaded image!")
  # Return the path of the saved image
  return jsonify({'image_path': response_image_path})

@app.get("/image_path/<path:image_path>")
def get_image_with_path(image_path):
  return send_file(image_path, mimetype = 'image/png')
