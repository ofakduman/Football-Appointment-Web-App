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
    upload_ap_add

    return redirect(url_for("myprofil"))
 