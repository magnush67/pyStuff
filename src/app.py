from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/greet/<name>")
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == "__main__":
    app.run(debug=True)

# To see the app running http://localhost:5000/api/greet/Alice