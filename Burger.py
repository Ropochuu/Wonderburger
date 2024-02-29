print("What is your order?")
print("We only sell burgers")

burger_cost = "20"
user_input = input("Your burger here: ") 
if user_input is "Texas Angus" or "Carolina Angus":
    print(user_input + " burger costs " + burger_cost)