import pytest
import Staff


def test_grades(staff_system):
    username = 'hdjsr7'
    course = 'cloud_computing'
    assignment = "assignment2"
    assert staff_system.change_grade(username, course, assignment, 50)


@pytest.fixture
def staff_system():
    staffSys = Staff.Staff()
    return staffSys
