import pytest
import System


# Tests if the program can pass check right, using right and wrong inputs
def test_password(grading_system):
   username = 'hdjsr7'
   password = 'WrongPass'
   test1 = grading_system.check_password(username, password)

   username = 'hdjsr7'
   password = 'pass1234'
   test2 = grading_system.check_password(username, password)

   if not test1:
   	assert True, "Wrong Combo Reject"
   else:
   	assert False, "Wrong Combo Accpeted, Fail"
	if test2:
		assert True, "Right login combo worked"
	else:
		assert False, "Right Login Combo Failed"

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
