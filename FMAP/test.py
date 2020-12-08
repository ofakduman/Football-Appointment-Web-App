import unittest
from web import app

class FlaskTestCase(unittest.TestCase):

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
		self.assertEqual(response.status_code, 404)#not constructed page 

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

	def test_addFootballArea(self):
		tester = app.test_client(self)
		response = tester.get('/addFootballArea', content_type = 'html/text')
		self.assertEqual(response.status_code, 404)#not constructed page

class requireUserLoginTest(unittest.TestCase):

	# Ensure that addArea page requires user login -Now there is a problem because We already work this page-
	def test_main_route_requires_addArea(self):
		response = self.client.get('/addArea', follow_redirects=True)
		self.assertIn(b'Please log in to access this page', response.data)

	# Ensure that myprofil page requires user login -Now there is a problem because We already work this page-
	def test_main_route_requires_myprofil(self):
		response = self.client.get('/myprofil', follow_redirects=True)
		self.assertIn(b'Please log in to access this page', response.data)

	# Ensure that addFootballArea page requires user login 
	def test_main_route_requires_addFootballArea(self):
		response = self.client.get('/addFootballArea', follow_redirects=True)
		self.assertIn(b'Please log in to access this page', response.data)


class usetTest(unittest.TestCase):

	# Databasede olan bir objenin siteye girip giremedigini kontrol eder
	def test_posts_show_up_on_main_page(self):
		response = self.client.post('/sigin',data=Users(name="admin", password="admin"),follow_redirects=True)
		self.assertIn(b'This is a test. Only a test.', response.data)

if __name__ == '__main__':
	unittest.main()	