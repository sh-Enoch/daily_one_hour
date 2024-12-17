from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def welcome():
    return render_template("index.html")

@app.route("/book")
def display():
    return render_template("index.html")

@app.route("/<name>")
def hello(name):
    return render_template("hello.html", name=name)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/category")
def category():
    return render_template("category.html")

@app.route("/about")
def about():
    sites = ['twitter', 'Discord', 'instagram', 'Github']
    return render_template("about.html", sites=sites)

@app.route("/contact/<role>")
def contact(role):
    return render_template("contact.html", person=role)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)

