from flask import Flask, request, jsonify, make_response
import hashlib

app = Flask(__name__)

input_text = ""

def generate_hash_func(text):
    sha256 = hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    return sha256.hexdigest()

@app.route('/set-text', methods=['POST'])
def set_text():
    global input_text
    data = request.get_json()
    new_text = data.get('input_text')
    input_text = new_text
    return jsonify({"message": "Text defined successfully!"})

@app.route('/generate-hash', methods=['GET'])
def generate_hash():
    global input_text
    if input_text:
        hash_result = generate_hash_func(input_text)
        return jsonify({"hash": hash_result})
    else:
        response = make_response(jsonify({"message": "Text not defined. Use the /set-text route first."}), 400)
        return response

@app.route('/verify-hash', methods=['POST'])
def verify_hash():
    global input_text
    data = request.get_json()
    input_hash = data.get('input_hash')
    if input_text:
        calculate_hash = generate_hash_func(input_text)
        if calculate_hash == input_hash:
            response = make_response(jsonify({"message": "The hash matches the text."}), 200)
            return response
        else:
            response = make_response(jsonify({"message": "The hash does not match the text."}), 400)
            return response
    else:
        response = make_response(jsonify({"message": "Text not defined. Use the /set-text route first."}), 400)
        return response

if __name__ == '__main__':
    app.run(debug=True)
