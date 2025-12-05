from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/convert")
def convert():
    celsius = request.args.get("c", type=float)

    if celsius is None:
        return jsonify({"error": "Please supply ?c=value"}), 400

    fahrenheit = (celsius * 9/5) + 32
    return jsonify({"fahrenheit": fahrenheit})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

