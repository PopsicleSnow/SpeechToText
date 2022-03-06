import sqlite3
import speech_recognition as sr
from flask import Flask, render_template
import sqlite3
import json

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect('words.db')
    c = conn.cursor()
    c.execute("SELECT * FROM words ORDER BY count DESC LIMIT 6")
    top = json.dumps(dict(c.fetchall()))
    return render_template("index.html", top = top)
    
if __name__ == "__main__":
    app.run(debug=True) # remove "host='0.0.0.0'" to run server on 127.0.0.1