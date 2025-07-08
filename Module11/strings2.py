#Advanced concepts - Strings

message=' Hello ,World! '

print(message.strip()) #Removing leading and trailing whitespace
print(message.lower()) #Convert all characters to lowecase
print(message.split(',')) #Split the string into a list based on the comma


#upper method
print(message.upper())
#replace method
my_string="Hello World"
new_stringssage=my_string.replace("e","o")
print(my_string)