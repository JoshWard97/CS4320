import pytest
import System

#Tests if the program can handle a wrong username
def test_loginWrong(grading_system):
    username = 'thtrhg'
    password =  'fhjhjdhjdfh'
    grading_system.login(username,password)

#Tests if the program can handle a right username and wrong password
def test_loginWrongUser(grading_system):
	username = 'cmhbf5'
	password = 'okayTA'
	grading_system.login(username,password)

#Tests if the program can handle a right username pass combo:
def test_login(grading_system):
	username = 'cmhbf5'
	password = 'bestTA'
	grading_system.login(username,password)

#Tests if the program can handle null username pass combo
def test_loginBlank(grading_system):
	username = ''
	password = ''
	grading_system.login(username,password)

def test_loginMissingParameters(grading_system):
	username = 'ThisIsSent'
	password = 'thisIsn\'tSent'
	grading_system.login(username)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

@pytest.fixture
def submit_sys():
	submit_sys = Student.Student()
	submit_sys
