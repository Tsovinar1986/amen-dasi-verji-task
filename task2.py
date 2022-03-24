from math import sqrt

class Namenum:
    def __init__(self,name):
        self.name  = name
     
        
    def numbersstr(self,x):
           self.x = x
           self.name = self.name.lower()
           if self.name == 'a' and self.name == 'j' and self.name == 's':
            return  self.x == 1
           if self.name == 'b' and self.name == 'k' and self.name == 't':
            return self.x == 2
           if self.name == 'c' and self.name == 'l' and self.name == 'u':
             return self.x == 3
           if self.name == 'd' and self.name == 'm' and self.name == 'v':
             return self.x == 4
           if self.name == 'e' and self.name == 'n' and self.name == 'w':
              return self.x == 5
           if self.name == 'f' and self.name == 'o' and self.name == 'x':
             return self.x == 6
           if self.name == 'g' and self.name == 'p' and self.name == 'y':
             return  self.x == 7
           if self.name == 'h' and self.name == 'q' and self.name == 'z':
             return  self.x == 8
           if self.name == 'i' and self.name == 'r':
             return  self.x == 9      
    def count(self):
         if sqrt(self.name) < 5:
                return 'Yes'
         else:
                return 'No'
name = input('Your name please -- > ')
y = Namenum(name)
print(y.count())
         
        

    