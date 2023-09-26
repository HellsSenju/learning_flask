from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    number = int(request.args.get('number'))
    return render_template("webService.html", result = str(number) + '^3 = ' + str(number**3))


if __name__ == '__main__':
    app.run(debug=True, threaded=True)