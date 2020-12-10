"""Flask App Project."""

from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder='./templates')


@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
