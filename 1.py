# from __future__ import braces
print('\\')
print(r'ye\ey')

# pythonic
numberOfPets = {'dogs': 2}
print('I have', numberOfPets.get('cats', 0), 'cats.') #checks whether the key
# 'cats' exists in the numberOfPets dictionary. If it does,
#  the method call returns the value for the 'cats' key. If it doesn’t, 
# it returns the second argument, 0, instead.

numberOfPets.setdefault('cats', 0) # Does nothing if 'cats' exists.

