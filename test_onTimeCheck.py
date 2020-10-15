import pytest
import System
import Student

def test_ontime(student_system):
	test_dueDate = '10/14/20'
	submissionOnTime = '10/13/20'
	submissionLate = '10/15/20'
	onTimeCheck = student_system.check_ontime(test_dueDate,submissionOnTime)
	lateCheck = student_system.check_ontime(test_dueDate,submissionLate)
	if onTimeCheck and not lateCheck:
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
