import unittest

from helperTest import *


class userCreateDatabase(unittest.TestCase):
	def test_userAddedSuccesfully(self):
		self.assertEqual(createNewUser(), 'User added succesfully!')

class Database(unittest.TestCase):
	def test_areaAddedSuccesfully(self):
		self.assertEqual(createArea(), 'Area added succesfully!')

	def test_areaDeletedSuccesfully(self):
		self.assertEqual(deleteArea(), 'Area deleted succesfully!')

	def test_userAreaRelation(self):
		self.assertEqual(getCheckAreaUserRelation(),True)

	def test_imageAddedSuccesfully(self):
		self.assertEqual(createImage(), 200)

	def test_imageDeletedSuccesfully(self):
		self.assertEqual(deleteImage(), 200)

	def test_userImageRelation(self):
		self.assertEqual(getCheckImageUserRelation(),True)

	def test_userDeleteSuccesfully(self):
		self.assertEqual(deleteAUser(), 'User deleted succesfully!')


if __name__ == '__main__':
	unittest.main()	