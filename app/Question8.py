
##Question 08

"""
Create a function called listProd that accepts a list of integers. Return the product of all
the values in the list. Perform error checking to make sure the values passed are all the
correct type (list and integers within the list).
"""


def listProd(val):
  prod=1
  if isinstance(val,list):
    if all(isinstance(item, int) for item in val):
      for x in val:
          prod*=x
      return prod
    else:
        return "All arguments not type(int)"
  else:
    return "Argument not a list"
    
print(listProd([2,4,5,6,7]))
