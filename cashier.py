#inventory containing items and prices
inventory = {"bread":10,"milk":12,"cola":7,"fanta":7,"water":20,"newspaper":12,"magazine":18,"candy":13,
             "juice":7,"oranges":3,"strawberries":25,"mango":99}
basket = []
total = []
def cashier():
    user_answer = input("Hello there sir/madam! What do you wish to purchase today?").lower()
    while user_answer != "quit":
        if user_answer in inventory:
            basket.append(user_answer)
            user_answer = input("Perfect! Added to the basket! Anything else?"
                                "Type 'quit' to end").lower()
        else:
            user_answer = input("item not available! anything else?"
                                "type quit to end").lower()
cashier()
print("Here are the items in your cart:",basket)
answer = input("Do you wish to add anything else?(Type yes/no)").lower()
if answer == "yes":
    cashier()
    print("here is all the groceries you ordered:",basket)
    for items in basket:
        total.append(inventory[items])
    amount_to_pay = sum(total)
else:
    for items in basket:
        total.append(inventory[items])
    amount_to_pay = sum(total)
print("your total amount is:",amount_to_pay)
# within a loop ask user for input (what do they wish to purchase), quit or end loop

# display the user's shopping cart and ask one more time if they wish to purchase anything else

# display the total amount to be paid for the items
