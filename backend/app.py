from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend():
    # Buraya öneri algoritmasını ekleyin
    return jsonify({"message": "Öneri sistemi çalışıyor!"})

if __name__ == '__main__':
    app.run(debug=True)

