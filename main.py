from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/keyboard', methods=['GET'])
def hello_world():
    return jsonify(
        type="buttons",
        buttons= [u"선택 1", u"선택 2", u"선택 3"]
    )

if __name__ == '__main__':
    app.debug = True
    app.run()
