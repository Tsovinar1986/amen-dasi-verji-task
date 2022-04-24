from random import *

class HarryPotter:
    def __init__(self,barer,c):
        self.barer = barer
        self.c = c
   
    def  Vold(self): 
            choice = ['Avada Kedavra', 'Crucio', 'Imperio']
            self.barer == choice
            for i in self.barer(3):
                if choice == i:
                   self.barer1.append(choice)
                   self.c += 1
                   print(self.barer1)
                else:
                   self.c == 0
                   print(self.barer1)
                 
    # def count(self):
    #     if self.c >= 2:
    #         return 'You win'
    #     else:
    #         return 'You lose'
barer=input('enter barer--> ')
x = HarryPotter()
print(x.Vold())