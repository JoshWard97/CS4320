import pytest
import Professor
import System


def test_student(prof_system):
    name = 'jawgrd'
    course = 'databases'
    if prof_system.add_student(name, course) is None:
        assert True
    else:
        assert False


@pytest.fixture
def prof_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    name = 'goggins'
    professorSystem = Professor.Professor(name, gradingSystem.users, gradingSystem.courses)
    return professorSystem
