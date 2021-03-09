from Person import Person
import unittest

class Student(Person):
  def __init__(self, firstname, lastname, address,studentlevel, gpa):
    super().__init__(firstname, lastname, address)
    self.StudentLevel=studentlevel
    self.GPA=gpa

  def changeGPA(self,newGPA):
    self.GPA=newGPA

  def __str__(self):
        return 'First Name: '+self.FirstName+'\nLast Name: '+self.LastName+'\nAddress: '+self.Address+'\nStudent Level: '+str(self.StudentLevel)+'\nGPA: '+str(self.GPA)
   

if __name__=='__main__':
    print("\n**************Creating A Student Object:")
    s1 = Student("Yousra", "Mashkoor", "Karachi street 123", 20, 3.4)
    s1.changeGPA(4.0)
    print(s1)
