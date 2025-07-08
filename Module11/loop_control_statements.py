#Loop Control Statements

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    
    if fruit == "cherry":
        break #Exits the loop if cherry is found
    print(fruit)
    
    
print()

for fruit in fruits:
    
    if fruit == "cherry":
        continue # Skips cherry and moves to the iteration
    print(fruit)
    
    
print()

for fruit in fruits:
    
    if fruit == "cherry":
        pass #Placeholder, no action is needed fro cherry
    print(fruit)
    