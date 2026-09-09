from flask import Flask, jsonify, render_template

app = Flask(__name__)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# API endpoint
@app.route("/api/users")
def users():
    return jsonify([
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ])


# Start Flask server
if __name__ == "__main__":
    app.run(debug=True)


