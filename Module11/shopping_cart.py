#Create a shopping cart programme that will contionuosly ask the user for the food product and the price that product
#Have an exit clause if the user wishes to shop adding more things to their cart
#at the end show food items and the total cost to the user

foods = []
prices = []
total = 0

while True:
    
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() =='q':
       break
        
 
    else:
       price = float(input(f"Enter the price of the {food}: R"))
       foods.append(food)
       prices.append(price)
    
print("------YOUR CART------")

for food in foods:
    print(food, end = " ")
    
for price in prices:
    total += price    

print("\n")
print(f"Your total is: R{total})")



