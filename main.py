Cost = 0.0
print("Welcome to Timmy's Tacos. We have a wide selection of foods for you. We sell donuts for $3.00 and coffee for $1.50. We dont serve tacos...")
order = []
Do_it_again = "yes"
while(Do_it_again == "yes"):
    Order_Number_1= input("What would you like? Coffee, Donut, or both?").strip().lower()
    if Order_Number_1 == "coffee":
        print("That will be 1.50 dollars. I used my employee mark-up, though. 85 dollars, please...")
        order.append(Order_Number_1)
        Cost = Cost + 85
    elif Order_Number_1 == "donut":
        print("The donuts would have been 3 dollars, but because of our talented chefs... we will pay you 5 dollars... If you order this and waffles, you will get 3 more dollars off.")
        order.append(Order_Number_1)
        Cost = Cost - 5
    elif Order_Number_1 == "both" :
        print("That will be 80 dollars... We wish you luck...")
        order.append(Order_Number_1)
        Cost = Cost + 80
    else :
        print("We are Timmy's Tacos... we obviously dont serve tacos or anything else here... lets try again...")

    # The other menu

    Order_Number_2 = input("We want more money! Order more! Would you like a main course or a dessert?").strip().lower()
    if Order_Number_2 == "main course" :
        Main_Course = input("Great! What would you like? Pancakes or Waffles?")
        if Main_Course == "pancakes" :
            print("Thats a pretty lame choice... Cash or card? ")
            order.append(Main_Course)
            Cost = (Cost + 25)
        elif Main_Course == "waffles" :
            print("Awesome!  ")
            order.append(Main_Course)
            Cost = (Cost + 30)
        else :
            print("We dont serve that... Restart... ")
    elif Order_Number_2 == "Dessert" :
        Dessert = input("Great! Would you like a chocolate crepe or croissant? ")
        if Dessert == "Chocolate Crepe" :
            print("Fantastic! ")
            order.append(Dessert)
            Cost = (Cost + 20)
        elif Dessert == "Croissant" :
            print("Great! ")
            order.append(Dessert)
            Cost = (Cost + 15)
    else :
        print("We are Timmy's Tacos... we obviously dont serve tacos or anything else here... lets try again...")

    Do_it_again = input("Would you like to order more/again?").strip().lower()

    # TODO: Also request numeric input from user for order a certain quantity of a condiment.
Sauce_Option = input("Would you like to order a sauce?").strip().lower()
if (Sauce_Option == "yes"):
    Sauce_Choice = input("Would you like maple syrup or honey?").strip().lower()
    if (Sauce_Choice == "maple syrup"):
        Maple_Amount = int(input("How much would you like?"))
        Cost = Cost + (1 * Maple_Amount)
    else:
        Honey_Amount = int(input("How much honey would you like?"))
        Cost + (1.50 * Honey_Amount)
else:
    pass

if (Order_Number_1 == "donut")and(Main_Course == "waffles"):
    Cost -= 3
else:
    pass
print("Your Order:")
print(order)
print(Cost)