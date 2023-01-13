from flask import Flask, render_template, request, jsonify
from flask_assets import Bundle, Environment
import random
app = Flask(__name__)

assets = Environment(app)
css = Bundle("src/style.css", output="dist/main.css")

assets.register("css", css)
css.build()


@app.route("/")
def homepage():
    return render_template("index.html", text="bye")


if __name__ == "__main__":
    app.run(debug=True)