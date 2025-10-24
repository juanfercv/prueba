from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    x, y = 5, 3
    suma = x + y
    resta = x - y
    return f"Suma: {suma}, Resta: {resta}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
