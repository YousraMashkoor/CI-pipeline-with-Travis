# import sys, os
# sys.path.append(os.path.abspath('..'))

from app.person import Person
from app.student import Student



import unittest

class TestPerson(unittest.TestCase):
    def test_changeAddr(self):
        p1 = Person("Yousra", "Mashkoor", "Karachi street 123")
        p1.changeAddr("London lane 5")
        self.assertNotEqual("Karachi street 123", p1.Address)

    def test_check_person_str(self):
        p1 = Person("Yousra", "Mashkoor", "Karachi street 123")
        self.assertEqual(str(p1), 'First Name: Yousra\nLast Name: Mashkoor\nAddress: Karachi street 123')
    
class TestStudent(unittest.TestCase):
    def test_changeGPA(self):
        s1 = Student("Yousra", "Mashkoor", "Karachi street 123", 30, 3.7)
        s1.changeGPA(4.0)
        self.assertNotEqual(3.7, s1.GPA)

    def test_check_student_str(self):
        s1 = Student("Yousra", "Mashkoor", "Karachi street 123", 30, 3.7)
        self.assertEqual(str(s1), 'First Name: Yousra\nLast Name: Mashkoor\nAddress: Karachi street 123\nStudent Level: 30\nGPA: 3.7')
    

if __name__=='__main__':
    unittest.main()