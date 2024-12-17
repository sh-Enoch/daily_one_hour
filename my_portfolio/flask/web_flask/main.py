from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def show():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/category")
def category():
    return render_template("category.html")

if __name__ == "__main__":
    app.run(debug=True,port=5000)
