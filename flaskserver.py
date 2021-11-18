from flask import Flask
from bert import preproces
from flask import request
from flask_cors import CORS, cross_origin

app  = Flask(__name__)
CORS(app)

@app.route("/data")
def serve():
    text = request.args.get('text')
    # print(text)
    res = preproces(' '+text)
    k = res.call()
    k["text"]= ' '+text
    return k

if __name__ == "__main__":
    app.run()