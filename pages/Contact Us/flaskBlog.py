from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
	return render_template("contact-us.html")


@app.route("/about")
def about():
	return "<h1>Home Page2</h1>"

if __name__ == '__main__':
	app.run(debug = True)	