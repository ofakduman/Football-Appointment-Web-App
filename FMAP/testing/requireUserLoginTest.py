import unittest

from helperTest import *

	

class requireUserLoginTest(unittest.TestCase):

	# Ensure that start application with no user -not yet login-
	def test_notToSignIn(self):
		self.assertEqual(getUser(), 0)

	# Ensure that signup page requires user login 
	def test_signupLogin(self):
		tester = app.test_client(self)
		response = tester.get('/signup', content_type = 'html/text')
		self.assertEqual(getUser(), 0)

	# Ensure that addArea page requires user login 
	def test_main_route_requires_addArea(self):
		tester = app.test_client(self)
		response = tester.get('/addArea', content_type = 'html/text')
		self.assertEqual(getUser(), 0)

	# Ensure that myprofil page requires user login 
	def test_main_route_requires_myprofil(self):
		tester = app.test_client(self)
		response = tester.get('/myprofil', content_type = 'html/text')
		self.assertEqual(getUser(), 0)
	
	# Ensure that addFootballArea page requires user login 
	def test_main_route_requires_addFootballArea(self):
		tester = app.test_client(self)		
		response = tester.get('/addFootballArea', content_type = 'html/text')
		self.assertEqual(getUser(), 0)


if __name__ == '__main__':
	unittest.main()	