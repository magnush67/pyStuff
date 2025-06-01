from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/greet/<name>")
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == "__main__":
    app.run(debug=True)

# Open browser http://127.0.0.1:5000/api/greet/Magnus