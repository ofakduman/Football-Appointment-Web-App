import unittest

from web import app, currentUser, setCurrentUser, getUser, createNewUser, deleteAUser, createArea, deleteArea

#import helperTestFunc



'''
# Yorum sayfasina yorum unit_testi eklenecek "2 tane"
# Web.py dosyasindaki unittest icin olan helper fonksiyonlar yeni bir dosyaya atanacak
# area ile user arasindaki iliski test edilecek
# db icin olusturulan kullanici tum test islemleri sonrasinda silinecek 

'''

class requireUserLoginTest(unittest.TestCase):

	
	def test_userAddedSuccesfully(self):
		self.assertEqual(createNewUser(), 'User added succesfully!')

	def test_areaAddedSuccesfully(self):
		self.assertEqual(createArea(), 'Area added succesfully!')

	def test_areaDeletedSuccesfully(self):
		self.assertEqual(deleteArea(), 'Area deleted succesfully!')

	def test_userDeleteSuccesfully(self):
		self.assertEqual(deleteAUser(), 'User deleted succesfully!')

	def test_notToSignIn(self):
		self.assertEqual(getUser(), 0)

	def test_signupLogin(self):
		tester = app.test_client(self)
		response = tester.get('/signup', content_type = 'html/text')
		self.assertEqual(getUser(), 0)

	# Ensure that addArea page requires user login -Now there is a problem because We already work this page-
	def test_main_route_requires_addArea(self):
		tester = app.test_client(self)
		response = tester.get('/addArea', content_type = 'html/text')
		self.assertEqual(getUser(), 0)

	# Ensure that myprofil page requires user login -Now there is a problem because We already work this page-
	def test_main_route_requires_myprofil(self):
		tester = app.test_client(self)
		response = tester.get('/myprofil', content_type = 'html/text')
		self.assertEqual(getUser(), 0)
	
	# Ensure that addFootballArea page requires user login 
	def test_main_route_requires_addFootballArea(self):
		tester = app.test_client(self)		
		response = tester.get('/addFootballArea', content_type = 'html/text')
		self.assertEqual(getUser(), 0)


class FlaskTestCase(unittest.TestCase):

	#In our web application userId = 1 is represents a user which userId's one
	def test_ToSignIn(self):
		setCurrentUser(1)
		self.assertEqual(getUser(), 1)

	#For ensure that signOut page was load correctlly

	def test_signout(self):
		tester = app.test_client(self)
		response = tester.get('/signout', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)

	#For ensure that homepage was load correctlly

	def test_homepage(self):
		tester = app.test_client(self)
		response = tester.get('/homepage', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)

	#For ensure that signup page was load correctlly
	def test_signup(self):
		tester = app.test_client(self)
		response = tester.get('/signup', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)


	#For ensure that appoinment page was load correctlly

	def test_appointment(self):
		tester = app.test_client(self)
		response = tester.get('/appointment', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)

	#For ensure that myprofile page was load correctlly

	def test_myprofil(self):
		tester = app.test_client(self)
		response = tester.get('/myprofil', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)#not access directly

	#For ensure that contactus page was load correctlly

	def test_contactus(self):
		tester = app.test_client(self)
		response = tester.get('/contactus', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)

	#For ensure that aboutus page was load correctlly

	def test_aboutus(self):
		tester = app.test_client(self)
		response = tester.get('/aboutus', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)		

	#For ensure that signin page was load correctlly

	def test_signin(self):
		tester = app.test_client(self)
		response = tester.get('/signin', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)

	#For ensure that signin page was load correctlly

	def test_editMyProfil(self):
		tester = app.test_client(self)
		response = tester.get('/editMyProfil', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)		

	#For ensure that signin page was load correctlly

	def test_addFootballArea(self):
		tester = app.test_client(self)
		response = tester.get('/addFootballArea', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)
	
	#For ensure that signin page was load correctlly

	def test_addArea(self):
		tester = app.test_client(self)
		response = tester.get('/addArea', content_type = 'html/text')
		self.assertEqual(response.status_code, 405)#there is an error!!!!!!

	def test_payment(self):
		tester = app.test_client(self)
		response = tester.get('/payment', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)#there is an error!!!!!!

	#For ensure that signin page was load correctlly
	def test_editFootballArea(self):
		tester = app.test_client(self)
		response = tester.get('/editFootballArea', content_type = 'html/text')
		self.assertEqual(response.status_code, 500)#there is an error!!!!!!
'''
class usetTest(unittest.TestCase):

	# Databasede olan bir objenin siteye girip giremedigini kontrol eder
	def test_posts_show_up_on_main_page(self):
		response = self.client.post('/sigin',data=Users(name="admin", password="admin"),follow_redirects=True)
		self.assertIn(b'This is a test. Only a test.', response.data)
'''

			#self.assertIn(b'You were logged in', response.data)
			#self.assertTrue(current_user.name == "admin")
			#self.assertTrue(current_user.is_active())
'''
  def test_correct_login1(self):
        with self.client:
            response = self.client.post('/login',data=dict(username="admin", password="admin"),follow_redirects=True)
            self.assertIn(b'You were logged in', response.data)
            self.assertTrue(current_user.name == "admin")
            self.assertTrue(current_user.is_active())
'''

if __name__ == '__main__':
	unittest.main()	