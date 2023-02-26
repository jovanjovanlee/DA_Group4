import unittest
import os
class Testrecon(unittest.TestCase):
    def test(self):
        os.system("C:\\Users\\jovan\\PycharmProjects\\DA_Group4\\spider1\\spider1\\spiders\\getindexpage.py")

class Testresponse(unittest.TestCase):
    def test(self):
        os.system("C:\\Users\\jovan\\PycharmProjects\\DA_Group4\\spider1\\spider1\\spiders\\getphotodir.py")

class Testimage(unittest.TestCase):
    def test(self):
        os.system("C:\\Users\\jovan\\PycharmProjects\\DA_Group4\\spider1\\spider1\\spiders\\getreqchangeheader.py")
if __name__ == '__main__':
    unittest.main()