import pytest
import System
import Student

def test_ontimeNoDate(student_system):
	test_dueDate = '10/14/20'
	submissionOnTime = '10/15/20'
	onTimeCheck = student_system.check_ontime(test_dueDate,submissionOnTime)
	if onTimeCheck:
		assert True
	else:
		assert False


@pytest.fixture
def student_system():
	gradingSystem = System.System()
	gradingSystem.load_data()
	name = 'nonUserName'
	studentSystem = Student.Student(name, gradingSystem.users, gradingSystem.courses)
	return studentSystem
