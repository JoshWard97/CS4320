import pytest
import System
import Student


def test_viewAssignments(student_system):
    course = 'comp_sci'
    assert student_system.view_assignments(course)


@pytest.fixture
def student_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    name = 'akend3'
    studentSystem = Student.Student(name, gradingSystem.users, gradingSystem.courses)
    return studentSystem
