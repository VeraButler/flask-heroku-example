"""Flask App Project."""

from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='./templates')


@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.html')


@app.route("/process", methods = ["GET", "POST"] )
def process_form():
    formData = request.values if request.method == "GET" else request.values
    response = "Form Contents <pre>%s</pre>" % "<br/>\n".join(["%s:%s" % item for item in formData.items()] )
    return response


if __name__ == '__main__':
    app.debug = True
    app.run()
