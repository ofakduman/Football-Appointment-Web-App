from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
#from flask_wtf.file import FileField, FileAllowed #to restrict upload file types -> to only upload png and jpeg files for pp
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Berk/Documents/GitHub/Project/FMAP/database.db'
db=SQLAlchemy(app)


currentUser = 0         #global variable
user_DataBase_size = 25

def setCurrentUser(id):
    global currentUser
    currentUser = id

def getUser():
    global currentUser
    return currentUser

@app.route("/")
@app.route("/homepage")
def homepage():
    global currentUser
    return render_template("homepage.html", id = currentUser)

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signout")
def signout():
    global currentUser
    currentUser = 0
    return render_template("signin.html")

@app.route("/appointment")
def appointment():
    global currentUser
    if currentUser == 0:                    #userId == 0 means there are no valid user  
        return render_template("signin.html", currentUser = currentUser)
    areas = FootballArea.query.all()
    return render_template("appointment.html",areas=areas)

@app.route("/myprofil")
def myprofil():
    global currentUser
    if currentUser == 0:
        return redirect(url_for("signin"))

    user = Users.query.filter_by(id = currentUser).first()
    areas = FootballArea.query.all()
    
    return render_template("myprofil.html", user = user,areas=areas)
    

    
@app.route("/contactus")
def contactus():
    global currentUser
    return render_template("contactus.html", id = currentUser)

@app.route("/aboutus")
def aboutus():
    global currentUser
    return render_template("aboutus.html", id = currentUser)

@app.route("/signin")
def signin():
    return render_template("signin.html")
@app.route("/editMyProfil")
def editMyProfil():
    global currentUser
    if currentUser == 0:
        return redirect(url_for("signin"))

    user = Users.query.filter_by(id = currentUser).first()
    return render_template("editMyProfil.html",user = user)

@app.route("/addFootballArea")
def addFootballArea():
    return render_template("addFootballArea.html")


@app.route("/addArea",methods = ["POST"])
def addArea():
    global currentUser
    user = Users.query.filter_by(id = currentUser).first()
    OwnerName = user.name
    AreaName = request.form.get("area_name")
    City = request.form.get("city")
    adress = request.form.get("adress")
    OwnerNumber = request.form.get("owner_number")
    user.phoneNumber = OwnerNumber
    owner_name = user.name   
    newArea = FootballArea(OwnerName = OwnerName,AreaName = AreaName,OwnerNumber=OwnerNumber,City = City,adress=adress, users = user)
    newClock = Clocks(c10 = 0,owner_area = newArea, c11 = 0,c12 = 0,c13 = 0,c14 = 0,c15 = 0,c16 = 0,c17 = 0,c18 = 0,c19 = 0,c20 = 0,c21 = 0, c22 = 0,c23 = 0,c24 = 0)
    db.session.add(newArea)
    db.session.add(newClock)
    db.session.commit()

    return redirect(url_for("myprofil"))

@app.route("/editFootballArea")
def editFootballArea():
    global currentUser
    user = Users.query.filter_by(id = currentUser).first()
    id = user.football_areas[0].id
    area = FootballArea.query.filter_by(id = id).first()

    return render_template("editFootballArea.html",area=area)

@app.route("/editArea",methods = ["POST"])
def editArea():
    global currentUser
    user = Users.query.filter_by(id = currentUser).first()
    id = user.football_areas[0].id
    area = FootballArea.query.filter_by(id = id).first()

    area.AreaName = request.form.get("area_name")
    area.City = request.form.get("city")
    area.adress = request.form.get("adress")
    area.OwnerNumber = request.form.get("owner_number")
    user.phoneNumber = area.OwnerNumber
    db.session.commit()
    return redirect(url_for("myprofil"))

@app.route("/bookAppointment/<string:id>")
def bookAppointment(id):
    area = FootballArea.query.filter_by(id = id).first()

    return render_template("book_Appointment.html",area=area)

@app.route("/fillcurrentclock/<string:id>/<int:clock>")
def fillcurrentclock(id,clock):
    global currentUser
    user = Users.query.filter_by(id = currentUser).first()
    area = FootballArea.query.filter_by(id = id).first()
    if clock == 0:
        area.clocks[0].c10 = user.id
    if clock == 1:
        area.clocks[0].c11 = user.id
    if clock == 2:
        area.clocks[0].c12 = user.id
    if clock == 3:
        area.clocks[0].c13 = user.id
    if clock == 4:
        area.clocks[0].c14 = user.id
    if clock == 5:
        area.clocks[0].c15 = user.id
    if clock == 6:
        area.clocks[0].c16 = user.id
    if clock == 7:
        area.clocks[0].c17 = user.id
    if clock == 8:
        area.clocks[0].c18 = user.id
    if clock == 9:
        area.clocks[0].c19 = user.id
    if clock == 10:
        area.clocks[0].c20 = user.id
    if clock == 11:
        area.clocks[0].c21 = user.id
    if clock == 12:
        area.clocks[0].c22 = user.id
    if clock == 13:
        area.clocks[0].c23 = user.id
    if clock == 14:
        area.clocks[0].c24 = user.id
        
    db.session.commit()
    return render_template("book_Appointment.html",area=area)


@app.route("/signup")
def Check_User(name1):
    x = 1
    global user_DataBase_size
    print(user_DataBase_size)    
    for x in range(user_DataBase_size):
        user1 = Users.query.filter_by(id = x).first()
        if user1:
            if name1 == user1.username:
                return False
        
    return True



@app.route("/signup_user",methods = ["POST"])
def signup_user():
    name = request.form.get("name")
    surname = request.form.get("surname")
    username = request.form.get("user_name")
    email = request.form.get("email")
    password = request.form.get("password")
    newUser = Users(name = name,surname = surname,username=username,email = email,password = password, user_type = 0)
    if Check_User(username) == False :
        return redirect(url_for("signup"))
    db.session.add(newUser)
    db.session.commit()
    return redirect(url_for("signin"))

@app.route("/editMyProfil",methods = ["POST"])
def edit_profile():
    
    global currentUser
    if currentUser == 0:
        return redirect(url_for("signin"))

    user = Users.query.filter_by(id = currentUser).first()
    user.name = request.form.get("name")
    user.username = request.form.get("username")
    user.password = request.form.get("password")
    user.email = request.form.get("email")
    user.phoneNumber = request.form.get("phoneNumber")
    pass1 = "a" 
    pass1 = request.form.get("confirmpassword")

    #picture = FileField('Update Profile Picture', validators = [FileAllowed(['jpg', 'png'])])
    if user.password != pass1:
        return redirect(url_for("editMyProfil"))
    db.session.commit()

    return redirect(url_for("myprofil"))


@app.route("/signup_owner",methods = ["POST"])
def signup_owner():
    name = request.form.get("name")
    surname = request.form.get("surname")
    username = request.form.get("user_name")
    email = request.form.get("email")
    password = request.form.get("password")
    newOwner = Users(name = name,surname = surname,username=username,email = email,password = password,user_type = 1)

    db.session.add(newOwner)
    db.session.commit()
    return redirect(url_for("signin"))

@app.route("/signin_user", methods=["POST", "GET"])
def signin_user():
    global currentUser
    if request.method == "POST":
        username = request.form["nm"]
        password = request.form["psw"]
        user_check = Users.query.filter_by(username=username).first()
        if user_check:
            if user_check.password == password:
                currentUser = user_check.id
        if user_check:
            if user_check.password == password:
                return redirect(url_for("myprofil")) #passing with userId to url for book appoinment
        return '<h1>Invalid username or password.</h1>'
    else:
        return render_template("signin.html")

class Users(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    username = db.Column(db.String(80))
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
    user_type = db.Column(db.Integer)
    football_areas = db.relationship('FootballArea', backref = 'users')
    phoneNumber = db.Column(db.String(80), default = 'none')
    #image_file = db.Column(db.String(40), default = 'profil_photo.png')

class FootballArea(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    OwnerName = db.Column(db.String(80))
    OwnerNumber = db.Column(db.String(80))
    AreaName = db.Column(db.String(80))
    City = db.Column(db.String(80))
    adress = db.Column(db.Text)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    clocks = db.relationship('Clocks',backref = 'owner_area')

class Clocks(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    owner_area_id = db.Column(db.Integer,db.ForeignKey('football_area.id'))
    c10 = db.Column(db.Integer, default = 0)
    c11 = db.Column(db.Integer, default = 0)
    c12 = db.Column(db.Integer, default = 0)
    c13 = db.Column(db.Integer, default = 0)
    c14 = db.Column(db.Integer, default = 0)
    c15 = db.Column(db.Integer, default = 0)
    c16 = db.Column(db.Integer, default = 0)
    c17 = db.Column(db.Integer, default = 0)
    c18 = db.Column(db.Integer, default = 0)
    c19 = db.Column(db.Integer, default = 0)
    c20 = db.Column(db.Integer, default = 0)
    c21 = db.Column(db.Integer, default = 0)
    c22 = db.Column(db.Integer, default = 0)
    c23 = db.Column(db.Integer, default = 0)
    c24 = db.Column(db.Integer, default = 0)
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)