from flask import Flask, jsonify, request

app = Flask(__name__)
heart_record = [

        {
            "heart_id": "",
            "date": "",
            "heart_rate": ""
        },
]

@app.route('/heart_record', methods=['GET'])
def getRecord():
    return jsonify(heart_record)

@app.route('/heart_record', methods=['POST'])
def addRecord():
    record = request.get_json()
    heart_record.append(record)
    return {'id': len(heart_record)},200

@app.route('/heart_record', methods=['POST'])
def getSpecific():
    specific = request.get_json()
    return jsonify(heart_record['heart_id' == specific]),300



if __name__ == '__main__':
    app.run()







    