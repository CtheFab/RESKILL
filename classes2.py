class category:
    
        #constructor 
        def __init__(self, category, amount):
                self.category = category
                self.amount = amount
       
        #methods      
        def deposits(self, amount):
                self.amount += amount
                return "You have sucessfully deposited {} in {} category".format(amount,self.category)
        
        def budget_balance(self):
                return "This is the current balance: {}".format(self.amount)

        def check_balance(self, amount):
                #this should return a True or False, it checks if amount is less or greater than self.amount
                self.amount >= amount
                return True
                self.amount <= amount
                return False
 
        def withdraw(self, amount):
               self.amount -= amount 
               return "You have sucessfully withdrawn {} in {} category".format(amount,self.category)
        
        def transfer(self, amount, category):
                category.withdraw(amount) + '.' +category.deposits(amount)
                return 

food_category = category("food", 500)
clothing_category = category("clothing", 300)
car_category = category("car expenses", 600) 

print(food_category.deposits(250))
print(food_category.budget_balance())
print(food_category.check_balance(250))
print(food_category.withdraw(150))
print(food_category.transfer(50))
print(clothing_category.deposits(250))
print(clothing_category.budget_balance())
print(clothing_category.check_balance())
print(clothing_category.withdraw(150))
print(clothing_category.transfer(100))
print(car_category.deposits(250))
print(car_category.budget_balance())
print(car_category.check_balance())
print(car_category.withdraw(150))
print(car_category.transfer(100))