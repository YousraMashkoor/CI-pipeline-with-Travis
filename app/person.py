import unittest

class Person:
  def __init__(self, firstname, lastname, address):
    self.FirstName = firstname
    self.LastName = lastname
    self.Address = address

  def changeAddr(self,newAddr):
    self.Address=newAddr

  def __str__(self):
        return 'First Name: '+self.FirstName+'\nLast Name: '+self.LastName+'\nAddress: '+self.Address



# if __name__=='__main__':

#     print("\n**************Creating A Person Object:")
#     p1 = Person("Yousra", "Mashkoor", "Karachi street 123")
#     p1.changeAddr("London lane 5")
#     print(p1)

