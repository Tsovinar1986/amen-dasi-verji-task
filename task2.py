from math import sqrt


class Namenum:
    def __init__(self,count):  
        self._count = count
    
    # def get_count(self):
    #       if sqrt(self._count) < 5:
    #         return 'Yes'
    #       else:
    #         return 'No'   
   
    def set_numbersstr(self,name,count = 0):
           self._name = name
           self._count = count
           if self._name == 'a' and self._name == 'j' and self._name == 's':
            return self._count == 1
           if self._name == 'b' and self._name == 'k' and self._name == 't':
              return self._count == 2
           if self._name == 'c' and self._name == 'l' and self._name == 'u':
             return self._count == 3
           if self._name == 'd' and self._name == 'm' and self._name == 'v':
             return self._count ==4
           if self._name == 'e' and self._name == 'n' and self._name == 'w':
             return self._count == 5
           if self._name == 'f' and self._name == 'o' and self._name == 'x':
             return self._count == 6
           if self._name == 'g' and self._name == 'p' and self._name == 'y':
             return self._count == 7
           if self._name == 'h' and self._name == 'q' and self._name == 'z':
             return self._count == 8
           if self._name == 'i' and self._name == 'r':
             return self._count == 9
           sum(map(int, self._count))
name = input('Enter your name  ')
name1 = name.lower()
y = Namenum(name1)
print(y._count)
print(y.set_numbersstr(name1))


