from web import *

#global variables for check one to many relation with user
check_area_user = False
check_image_user = False

#getters
def getCheckAreaUserRelation():
    global check_area_user
    return check_area_user

def getCheckImageUserRelation():
    global check_image_user
    return check_image_user


def createNewUser():
    newOwner = Users(name = 'TemelReis',surname = 'owner1' ,username='owner1',
        email = 'owner1',password = 'owner1',user_type = -1)
    db.session.add(newOwner)
    db.session.commit()
    user = Users.query.filter_by(user_type = -1).first()

    if user:                #If added there must be a user who has user_type -1
        return 'User added succesfully!'

    return 'User didnt add, Error!'

def createArea():
    global check_area_user
    user = Users.query.filter_by(user_type = -1).first()
    if not user:
        return 'Error, there is not any user whose created for test! Look back createNewUser function.'

    OwnerName = 'TemelReis'
    AreaName = 'test_case'
    City = 'test_case'
    adress = 'test_case'
    OwnerNumber = 'test_case'
    owner_name = 'test_case'   
    newArea = FootballArea(OwnerName = OwnerName,AreaName = AreaName,
        OwnerNumber=OwnerNumber,City = City,adress=adress,LikeCoun=0, users = user)
   
    db.session.add(newArea)
    db.session.commit()    
    area = FootballArea.query.filter_by(adress = 'test_case').first()

    if area.users_id == user.id:
        check_area_user = True  #area and user connection is OK if check_area_user is True

    if area:                #If added there must be a user who has user_type -1
        return 'Area added succesfully!'

    return 'Area didnt add, Error!'


def deleteArea():
    area = FootballArea.query.filter_by(adress = 'test_case').first()

    if not area:                #If added there must be a user who has user_type -1
        return 'Error, There is no area which is created by createArea function! Look for createArea function.'

    db.session.delete(area)
    db.session.commit()
    area = FootballArea.query.filter_by(adress = 'test_case').first()

    if not area:          
        return 'Area deleted succesfully!'

    return 'Error, Area didnt deleted!'

def deleteAUser():
    user = Users.query.filter_by(user_type = -1).first()
    if not user:                #If didnt user add so didnt delete
        return 'Error, there is no user for delete! Look back to createNewUser function'
    db.session.delete(user)
    db.session.commit()

    user = Users.query.filter_by(user_type = -1).first()
    
    if not user:
        return 'User deleted succesfully!'
    return 'Error, User didnt deleted!'

def createImage():
    global check_image_user

    user = Users.query.filter_by(user_type = -1).first()
    if not user:
        return 'no user' , 400

    filename = "this is an example!"
    mimetype = "this is an example!"
    img = "this is an example!"


    image = Img(img = img, mimetype = mimetype, name = filename, users = user)

    db.session.add(image)
    db.session.commit()

    image = Img.query.filter_by(mimetype = "this is an example!" ).first()

    if image.users_id == user.id:
        check_image_user = True #to check image user relation

    if image:
        return 200 # "Blob created succesfully!" ,

    if not image:
        return "Blob didnt create!" , 400


def deleteImage():

    image = Img.query.filter_by(mimetype = "this is an example!" ).first()
    db.session.delete(image)
    db.session.commit()
    image = Img.query.filter_by(mimetype = "this is an example!" ).first()


    if not image:
        return 200 # "Blob deleted succesfully!" ,

    if  image:
        return "Blob didnt delete!" , 400

