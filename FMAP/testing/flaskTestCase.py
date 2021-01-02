import unittest

from helperTest import *



class flaskTestCase(unittest.TestCase):

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
		self.assertEqual(response.status_code, 200)

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

	#For ensure that addFootballArea page was load correctlly
	def test_addFootballArea(self):
		tester = app.test_client(self)
		response = tester.get('/addFootballArea', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)

	#For ensure that payment page was load correctlly
	def test_payment(self):
		tester = app.test_client(self)
		response = tester.get('/payment', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
	unittest.main()	