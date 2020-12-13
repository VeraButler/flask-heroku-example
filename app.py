"""Flask App Project."""

from flask import Flask, jsonify, render_template, request

from model import get_prediction

app = Flask(__name__, template_folder='./templates')


@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.html')


@app.route("/process", methods=["GET", "POST"])
def process_form():
    user_input = []
    formData = request.values if request.method == "GET" else request.values
    for item in formData.items():
        user_input.append(item)
    response = get_prediction(user_input)
    return response


if __name__ == '__main__':
    app.debug = True
    app.run()
