from selenium import webdriver
import time
import unittest

# Aisha Idowu
# Task 24

flag = False
drag_and_drop = 'Implemented'


class chatscrumProductAppTest(unittest.TestCase):
    @unittest.expectedFailure
    def test_loginfunctionality(self):
        print('Login Test')
    @unittest.skip('The Signup is yet to be implemented')
    def test_signupfunctionality(self):
        print('Signup Test')

    if drag_and_drop == 'Implemented':
        flag = True
    else:
        flag = False
    @unittest.skipIf(flag == True, 'flag returned ' + str(flag))
    def test_raganddropfeature(self):
        print('Drag and Drop Test')

    def test_createtaskfeature(self):
        print('Create task features')

    def test_chatcollaborationfeature(self):
        print('Chat Collaboration test')


if __name__ == '__main__':  # To make the code run call the main method from the unit test module
    unittest.main()