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
    formData = request.values if request.method == "GET" else request.values
    user_input = []
    for item in formData.items():
        user_input.append(item[1])
    # response = "Form Contents <pre>%s</pre>" % "<br/>\n".join(["%s:%s" % item for item in formData.items()])
    # return response
    for item in formData.items():
        if item[0] == 'fixed-acidity':
            user_input[0] == item[1]
        if item[0] == 'volatile-acidity':
            user_input[1] == item[1]
        if item[0] == 'citric-acid':
            user_input[2] == item[1]
        if item[0] == 'residual-sugar':
            user_input[3] == item[1]
        if item[0] == 'chlorides':
            user_input[4] == item[1]
        if item[0] == 'free-sulfur-dioxide':
            user_input[5] == item[1]
        if item[0] == 'total-sulfur-dioxide':
            user_input[6] == item[1]
        if item[0] == 'density':
            user_input[7] == item[1]
        if item[0] == 'pH':
            user_input[8] == item[1]
        if item[0] == 'sulphates':
            user_input[9] == item[1]
        if item[0] == 'alcohol':
            user_input[10] == item[1]

    response = get_prediction(user_input)
    print(user_input)
    if response == '2':
        return render_template('rating.html', rating='AVERAGE')
    elif response == '1':
        return render_template('rating.html', rating='POOR')
    elif response == '3':
        return render_template('rating.html', rating='EXCELLENT')
    else:
        return render_template('rating.html', rating='Something went wrong. Please try again.')


if __name__ == '__main__':
    app.debug = True
    app.run()
