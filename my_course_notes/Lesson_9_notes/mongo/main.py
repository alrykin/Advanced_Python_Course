from flask import Flask, request, jsonify
#import json

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    print(request.headers)
    #print(request.headers['priv_token'])
    if request.headers['priv_token'] == '34#$^QG3asgsadRSBV4W24W':
        data  = {"value": 2}
        # return json.dumps(data)
        return jsonify(data)# используя flask jsonify
    else:
        # return json.dumps({"error_code": "wrong_auth"})
        return jsonify({"error_code": "wrong_auth"})# используя flask jsonify

@app.route('/get_json', methods = ['GET','POST'])
def get_var_from_json():
    data = {"value": 2}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
