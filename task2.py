from math import sqrt


class Namenum:
    def __init__(self,count):  
        self._count = count
    
    def count(self):
          if sqrt(self._count) < 5:
            return 'Yes'
          else:
            return 'No'   
   
    def numbersstr(self,name):
           self._name1 = name
           for i in self._name1:
            if self._name1 == ('a' ,'j' , 's'):
                return  i == 1
            if self._name1 == ('b','k' ,'t'):
                return i == 2
            if self._name1 == ('c','l','u'):
               return i == 3
            if self._name1 == ('d','m','v'):
                return  i == 4
            if self._name1 == ('e', 'n', 'w'):
                return i == 5
            if self._name1 == ('f' , 'o' , 'x'):
                return i == 6
            if self._name1 == ('g','p' ,'y'):
                return i == 7
            if self._name1 == ('h', 'q','z'):
                return i == 8
           if self._name1 == ('i', 'r'):
             return i == 9
           self._name1 += int(i)
           self._count = self._name1
           return self._count
name = input('Enter your name please--> ')
name1 = name.lower()
y = Namenum(name1)
print(y._count)
print(y.count())
