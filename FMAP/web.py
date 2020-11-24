from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/appointment")
def appointment():
    return render_template("appointment.html")

@app.route("/myprofil")
def myprofil():
    return render_template("myprofil.html")
    
@app.route("/contactus")
def contactus():
    return render_template("contactus.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

if __name__ == "__main__":
    app.run(debug=True)