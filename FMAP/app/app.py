from datetime import datetime
from flask import Flask,render_template,request,redirect,url_for,flash,Response
from flask_sqlalchemy import SQLAlchemy

from werkzeug.utils import secure_filename
import base64   #to convert string (blob database) to picture



app = Flask(__name__) 
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pfhfcvdsbaiijf:ffb41713a5a78f65ecd23b24086edec25a1ca22569a29e214639ab1e6b2e1d83@ec2-107-23-191-123.compute-1.amazonaws.com:5432/da6oja5nrlotcv'
db=SQLAlchemy(app)

currentEnablet = True
currentEnablef = True
currentUser = 0         
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
    return render_template("appointment.html",areas=areas,selection_city = "")

@app.route("/appointment",methods = ["POST"])
def searchCity():
    global currentUser
    if currentUser == 0:                    #userId == 0 means there are no valid user  
        return render_template("signin.html", currentUser = currentUser)
    selection_city = (request.form.get("selection"))
    areas = FootballArea.query.all()
    return render_template("appointment.html",areas=areas,selection_city = selection_city)

@app.route("/myprofil")
def myprofil():
    global currentUser
    if currentUser == 0:
        return redirect(url_for("signin"))

    user = Users.query.filter_by(id = currentUser).first()
    areas = FootballArea.query.all()
    pp = Img.query.filter_by(users_id =currentUser).first()
    
    if pp:
        image = pp.img
    if not pp:
        image = -1 #-1 is a magic number to represent not found image

    return render_template("myprofil.html", user = user,areas=areas, image = image)

@app.route("/myprofil/appointments")
def myAppointments():
    global currentUser
    if currentUser == 0:
        return redirect(url_for("signin"))

    user = Users.query.filter_by(id = currentUser).first()
    areas = FootballArea.query.all()
    pp = Img.query.filter_by(users_id = currentUser).first()
    
    if pp:
        image = pp.img
    if not pp:
        image = -1 
    
    return render_template("myAppointments.html", user = user,areas=areas, image = image)

    
@app.route("/payment")
def payment():
    global currentUser
    return render_template("payment.html", id = currentUser)
    
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
    newArea = FootballArea(OwnerName = OwnerName,AreaName = AreaName,OwnerNumber=OwnerNumber,City = City,adress=adress, users = user,LikeCoun=0)
    newClock = Clocks(c10 = 0,owner_area = newArea, c11 = 0,c12 = 0,c13 = 0,c14 = 0,c15 = 0,c16 = 0,c17 = 0,c18 = 0,c19 = 0,c20 = 0,c21 = 0, c22 = 0,c23 = 0,c24 = 0)
    db.session.add(newArea)
    db.session.add(newClock)
    db.session.commit()
    return redirect(url_for("myprofil"))

"""@app.route("/appointment_comment/<string:id>")
def appointment_comment(id):
    area = FootballArea.query.filter_by(id = id).first()
    return render_template("appointment_comment.html",area=area)    

@app.route("/app_comm/<string:id>",methods = ["POST"])
def app_comm(id):
    if request.method == 'POST':
        area = FootballArea.query.filter_by(id = id).first()
        newCommentCom = request.form.get("Com")
        newComment = Comment(owner_Com = id,Com = newCommentCom)
        print(newCommentCom)
        db.session.add(newComment)
        db.session.commit()
        return redirect(url_for("appointment"))"""

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
    area.img1 

    db.session.commit()


    return redirect(url_for("myprofil"))

@app.route("/bookAppointment/<string:id>")
def bookAppointment(id):
    area = FootballArea.query.filter_by(id = id).first()
    comments = comment.query.all()
    users = Users.query.all()
    return render_template("book_Appointment.html",area=area, comments=comments, users = users)

"""@app.route("/addComment/<string:id>",methods=['GET','POST'])    
def addComment(id):
    global currentUser
    an = datetime.now()
    user = Users.query.filter_by(id = currentUser).first()
    area = FootballArea.query.filter_by(id = id).first()
    com = request.form.get("Comment")
    user = Users.query.filter_by(id = currentUser).first()
    if not user:
        return redirect(url_for("appointment"))

    owner_Com = area.id
    owner_Id = user.id
    owner_User = user.name
    owner_Y = an.year
    owner_M = an.month
    owner_D = an.day
    owner_H = an.hour
    owner_Mi = an.minute
    newComment = comment(Com = com,owner_Com=owner_Com,owner_Id = owner_Id,owner_User=owner_User,Year=owner_Y,Month=owner_M,Day=owner_D,Hour=owner_H,Minute=owner_Mi)
    db.session.add(newComment)
    db.session.commit()
    comments = comment.query.all()
    users = Users.query.all()
    return render_template("book_Appointment.html",area=area,comments=comments, users=users)"""

@app.route("/incrementlike/<int:curent_id>")
def incrementlike(curent_id):
    global currentUser
    global currentEnablef
    global currentEnablet
    if currentEnablet == True :
        area = FootballArea.query.filter_by(id = curent_id).first()
        area.LikeCoun +=1
        db.session.commit()
        currentEnablet = False ;
        currentEnablef = True  
        return redirect(url_for("appointment"))
    else :
        return redirect(url_for("appointment"))

@app.route("/decrementlike/<int:curent_id>")
def decrementlike(curent_id):
    global currentUser
    global currentEnablet
    global currentEnablef
    if currentEnablef == True : 
        area = FootballArea.query.filter_by(id = curent_id).first()
        area.LikeCoun -=1
        db.session.commit()
        currentEnablef = False
        currentEnablet = True
        return redirect(url_for("appointment"))
    else :
        return redirect(url_for("appointment"))

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
    return redirect(url_for("payment"))


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
    global currentEnablet
    currentEnablet = True
    global currentEnablef 
    currentEnablef = True
    name = request.form.get("name")
    surname = request.form.get("surname")
    username = request.form.get("user_name")
    email = request.form.get("email")
    password = request.form.get("password")
    newUser = Users(name = name,surname = surname,username=username,email = email,password = password, user_type = 0)
    #newComment=comment(Com="Bos",owner_Com="1",owner_User="None",Year=1,Month=1,Day=1,Hour=1,Minute=2)
    if Check_User(username) == False :
        return redirect(url_for("signup"))
    db.session.add(newUser)
    #db.session.add(newComment)
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
        flash("Invalid username or password !!!" , "error")
        return render_template("signin.html")
    else:
        return render_template("signin.html")

@app.route('/<int:id>')
def get_img(id):
    image = Img.query.filter_by(users_id = currentUser).first()
    if not image:
        return 'no image', 400

    return Response(image.img , mimetype = image.mimetype)

@app.route('/upload_pp', methods = ['POST'])
def upload():
    pic = request.files['pic']

    if not pic:
        return 'no pic uploaded' , 400

    user = Users.query.filter_by(id = currentUser).first()
    if not user:
        return 'no user' , 400

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    img = pic.read()

    img = base64.b64encode(img).decode('ascii')
    #img = img.decode('utf-8')
    user.pp = img

    image = Img.query.filter_by(users_id = currentUser).first()

    if not image:
        image = Img(img = img, mimetype = mimetype, name = filename, users = user)
        db.session.add(image)
        db.session.commit()
        #return 'Img has been uploaded', 200
        return redirect(url_for("myprofil"))

    if image:
        image.img = img
        image.mimetype = mimetype
        image.name = filename
        db.session.commit()
        #flash("Photo Uploaded" , "200")
        return redirect(url_for("myprofil"))

@app.route('/upload_ap', methods = ['POST'])
def upload_ap():

    pic = request.files['pic']
    area = FootballArea.query.filter_by(users_id = currentUser).first()

    if not pic:
        return 'no pic uploaded' , 400

    
    if not area:
        return 'no area found' , 400

    user = Users.query.filter_by(id = currentUser).first()
    if not user:
        return 'no user' , 400

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    img = pic.read()

    img = base64.b64encode(img).decode('ascii')
    #img = img.decode('utf-8')

    #if area.img1 == "none":
    area.img1 = img


    db.session.commit()

    return redirect(url_for("editFootballArea"))

@app.route('/upload_ap_add', methods = ['POST'])
def upload_ap_add():

    pic = request.files['pic']
    area = FootballArea.query.filter_by(users_id = currentUser).first()

    if not pic:
        return 'no pic uploaded' , 400

    if not area:
        return 'no area found' , 400

    user = Users.query.filter_by(id = currentUser).first()
    if not user:
        return 'no user' , 400

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    img = pic.read()

    img = base64.b64encode(img).decode('ascii')
    #img = img.decode('utf-8')

    if area.img1 == "none":
        area.img1 = img


    elif area.img2 == "none":
        area.img2 = img
    
    elif area.img3 == "none":
        area.img3 = img
            
    elif area.img4 == "none":
        area.img4 = img

    db.session.commit()

    return redirect(url_for("editFootballArea"))

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
    image_profile = db.relationship('Img', backref = 'users')
    pp = db.Column(db.Text, default = "none")
    #image_file = db.Column(db.String(40), default = 'profil_photo.png')

class Img(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    img = db.Column(db.Text, default = "none")
    name = db.Column(db.Text, nullable = False)
    mimetype = db.Column(db.Text, nullable = False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), default = -1)
   # owner_area_id = db.Column(db.Integer,db.ForeignKey('football_area.id'), default = -1)

class comment(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    owner_Id = db.Column(db.Integer, default = -1)
    owner_User = db.Column(db.String(80))
    owner_Com = db.Column(db.Integer)
    Com  =  db.Column(db.String(80))
    Year = db.Column(db.Integer)
    Month = db.Column(db.Integer)
    Day = db.Column(db.Integer)
    Hour = db.Column(db.Integer)
    Minute = db.Column(db.Integer)

class FootballArea(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    OwnerName = db.Column(db.String(80))
    OwnerNumber = db.Column(db.String(80))
    AreaName = db.Column(db.String(80))
    LikeCoun = db.Column(db.Integer)
    City = db.Column(db.String(80))
    adress = db.Column(db.Text)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    clocks = db.relationship('Clocks',backref = 'owner_area')
    img1 = db.Column(db.Text, default = "none")
    img2 = db.Column(db.Text, default = "none")
    img3 = db.Column(db.Text, default = "none")
    img4 = db.Column(db.Text, default = "none")


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

