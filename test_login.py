import pytest
import System


def test_login(grading_system):
	username = 'hdjsr7'
	password = 'pass1234'
	testRight = grading_system.login(username, password) == None
	if testRight:
		assert True
	else:
		assert False


@pytest.fixture
def grading_system():
	gradingSys = System.System()
	gradingSys.load_data()
	return gradingSys
