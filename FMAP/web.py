from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/90538/Desktop/Project/FMAP/database.db'
db=SQLAlchemy(app)


@app.route("/")
@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/appointment")
def appointment():
    areas = FootballArea.query.all()
    return render_template("appointment.html",areas=areas)

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

@app.route("/addFootballArea")
def addFootballArea():
    return render_template("addFootballArea.html")


@app.route("/addArea",methods = ["POST"])
def addArea():
    OwnerName = request.form.get("owner_name")
    AreaName = request.form.get("area_name")
    City = request.form.get("city")
    adress = request.form.get("adress")
    OwnerNumber = request.form.get("owner_number")
    newArea = FootballArea(OwnerName = OwnerName,AreaName = AreaName,OwnerNumber=OwnerNumber,
                            City = City,adress=adress)

    db.session.add(newArea)
    db.session.commit()
    return redirect(url_for("addFootballArea"))

@app.route("/bookAppointment/<string:id>")
def bookAppointment(id):
    area = FootballArea.query.filter_by(id = id).first()

    return render_template("book_Appointment.html",area=area)
    
@app.route("/signup_user",methods = ["POST"])
def signup_user():
    name = request.form.get("name")
    surname = request.form.get("surname")
    username = request.form.get("user_name")
    email = request.form.get("email")
    password = request.form.get("password")
    newUser = Users(name = name,surname = surname,username=username,email = email,password = password)#, user_type = "user")

    db.session.add(newUser)
    db.session.commit()
    return redirect(url_for("signin"))

@app.route("/signup_owner",methods = ["POST"])
def signup_owner():
    name = request.form.get("name")
    surname = request.form.get("surname")
    username = request.form.get("user_name")
    email = request.form.get("email")
    password = request.form.get("password")
    newUser = Users(name = name,surname = surname,username=username,email = email,password = password)#,user_type = "owner")

    db.session.add(newOwner)
    db.session.commit()
    return redirect(url_for("signin"))

@app.route("/signin_user", methods=["POST", "GET"])
def signin_user():
    if request.method == "POST":
        username = request.form["nm"]
        password = request.form["psw"]
        user_check = Users.query.filter_by(username=username).first()
        if user_check:
            if user_check.password == password:
                return render_template("myprofil.html")
        return '<h1>Invalid username or password</h1>'
    else:
        return render_template("signin.html")

class Users(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    username = db.Column(db.String(80))
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
    #user_type = db.Column(db.String(80))

    def __init__(self, name, surname, username, email, password):#, user_type):
        self.name = name
        self.surname = surname
        self.username = username
        self.email = email
        self.password = password
        #self.user_type = user_type

class FootballArea(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    OwnerName = db.Column(db.String(80))
    OwnerNumber = db.Column(db.String(80))
    AreaName = db.Column(db.String(80))
    City = db.Column(db.String(80))
    adress = db.Column(db.Text)
    
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)