bottles = int(input("How many bottles of wine are there: "))
pizza = int(input("How many pizzas are there: "))

if bottles and pizza == 5:
    print("This is a good party")
elif bottles and pizza > 5:
    print("This party is fantastic")
else:
    print("This party is just stupid")