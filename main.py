# Car rent system

class Car:

    def __init__(self, stock ):
        self.stock = stock


    def displaycar(self):
        print("Total cars in stock:",self.stock) 

    def rentforcar(self,q):
        if q <= 0:

            print("Enter positive number minimum 1.")
        
        elif q >self.stock:
            print("Enter the value less than stock")

        else:
            self.stock = self.stock - q
            print("Total price", q*5000)
            print("Total cars remaining stock:",self.stock)        

while True:
    obj = Car(50) 

    uc = int(input('''
                   
    1 Total stock
    2 Enter quantity of car for rent
    3 exit

'''))
    
    if uc == 1:
        obj.displaycar()
    elif uc == 2:
        n = int(input("Enter the qty:"))
        obj.rentforcar(n)

    else:
        break        