import pytest
import System
import Student


def test_submit(student_system):
    course = 'comp_sci'
    assignment_name = 'assignment3'
    submission = 'This is a long paper'
    submission_date = '01/01/20'
    assert student_system.submit_assignment(course, assignment_name, submission, submission_date)


@pytest.fixture
def student_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    name = 'akend3'
    studentSystem = Student.Student(name, gradingSystem.users, gradingSystem.courses)
    return studentSystem
