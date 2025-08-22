from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

from PIL import Image
img = Image.open("WhatsApp Image 2025-05-01 at 09.29.33.jpeg")
