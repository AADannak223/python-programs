from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'Hello, World'


@app.route("/sum/<int:n>")
def square(n):
    if n % 2 == 0:
        result = {
            "number": n,
            "Even": True,
            "server-IP": "122.234.323.234.44"
        }
    else:
        result = {
            "number": n,
            "Even": False,
            "server-IP": "122.234.323.234.44"
        }
    return jsonify(result)


if __name__=="__main__":
    app.run(debug=True)




