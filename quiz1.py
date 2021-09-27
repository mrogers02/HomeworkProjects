# Ask user for two numbers
n1 = input("What is your first number?")
n2 = input("What is your second number?")
# Create a loop that does the following until the product and sum are the same
sum = (int(n1) + int(n2))
product = (int(n1) * int(n2))
while (product != sum):
    print ("You have to pick two more numbers because your sum and product are not equal")
    n1 = input("What is your first number?")
    n2 = input("What is your second number?")
    sum = (int(n1) + int(n2))
    product = (int(n1) * int(n2))
# Calculate and display their sum
print ("Your sum is " + str(sum))


# Calculate and display their product
print ("Your product is " + str(product))

# If their sum and their product are equal - tell the user
print ("Congratulations your sum and product are equal.")
# otherwise ask for two more numbers
if (product != sum):
    print ("You have to pick two more numbers because your sum and product are not equal")
    n1 = input("What is your first number?")
    n2 = input("What is your second number?")