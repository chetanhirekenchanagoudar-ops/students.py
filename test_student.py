
from student import get_student

def test_student_name():
    student = get_student()
    assert student["name"] == "Chetan"

def test_student_usn():
    student = get_student()
    assert student["usn"] == "01FE25BCA320"

def test_student_college():
    student = get_student()
    assert student["college"] == "ABC College"

def test_student_city():
    student = get_student()
    assert student["city"] == "Hubli"
