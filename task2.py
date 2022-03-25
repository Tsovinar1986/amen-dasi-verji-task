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
            if self._name1 == 'a' and self._name1 == 'j' and self._name1 == 's':
                return  i == 1
            if self._name1 == 'b' and self._name1 == 'k' and self._name1 == 't':
                return i == 2
            if self._name1 == 'c' and self._name1 == 'l' and self._name1 == 'u':
               return i == 3
            if self._name1 == 'd' and self._name1 == 'm' and self._name1 == 'v':
                return  i == 4
            if self._name1 == 'e' and self._name1 == 'n' and self._name1 == 'w':
                return i == 5
            if self._name1 == 'f' and self._name1 == 'o' and self._name1 == 'x':
                return i == 6
            if self._name1 == 'g' and self._name1 == 'p' and self._name1 == 'y':
                return i == 7
            if self._name1 == 'h' and self._name1 == 'q' and self._name1 == 'z':
                return i == 8
           if self._name1 == 'i' and self._name1 == 'r':
             return i == 9
           self._name1 += int(i)
           self._count = self._name1
           return self._count
name = input('Enter your name please--> ')
name1 = name.lower()
y = Namenum(name1)
print(y._count)
print(y.count())
