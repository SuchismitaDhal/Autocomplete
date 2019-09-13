from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

WORDS = []
with open("large.txt", "r") as file:
    for line in file.readlines():
        WORDS.append(line.rstrip())


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    words = [word for word in WORDS if word.startswith(request.args.get("q"))]
    # more memory efficient than return render_template("search.html", words=words)
    # would return an object as 0:word0 1:word1 ...
    return jsonify(words)
