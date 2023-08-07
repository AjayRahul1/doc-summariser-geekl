from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def summarise_page():
  return render_template('index.html')