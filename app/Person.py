import unittest

"""##Question 09
Create a class called Person with the following attributes:

* i. FirstName
* ii. LastName
* iii. Address
> * b. Create a method to print all the attributes using the __str__ method.
> * c. Create a method to change the address.
> * d. Create at least 2 test cases and execute all the methods you’ve created on all your
test cases.
"""

class Person:
  def __init__(self, firstname, lastname, address):
    self.FirstName = firstname
    self.LastName = lastname
    self.Address = address

  def changeAddr(self,newAddr):
    self.Address=newAddr

  def __str__(self):
        return 'First Name: '+self.FirstName+'\nLast Name: '+self.LastName+'\nAddress: '+self.Address



if __name__=='__main__':

    print("\n**************Creating A Person Object:")
    p1 = Person("Yousra", "Mashkoor", "Karachi street 123")
    p1.changeAddr("London lane 5")
    print(p1)

