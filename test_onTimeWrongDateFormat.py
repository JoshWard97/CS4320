import pytest
import System
import Student

def test_ontimeNoDate(student_system):
	test_dueDate = '10/14/20'
	submissionOnTime = 'October 14 2020'
	onTimeCheck = student_system.check_ontime(test_dueDate,submissionOnTime)
	if onTimeCheck:
		assert True
	else:
		assert False


@pytest.fixture
def student_system():
	gradingSystem = System.System()
	gradingSystem.load_data()
	name = 'akend3'
	studentSystem = Student.Student(name, gradingSystem.users, gradingSystem.courses)
	return studentSystem
