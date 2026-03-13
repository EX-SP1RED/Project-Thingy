Cost = 0.0
print("Welcome to Timmy's Tacos. We have a wide selection of foods for you. We sell donuts for $3.00 and coffee for $1.50. We dont serve tacos...")
order = []
Order_Number_1= input("What would you like? Coffee, Donut, or both?")
if Order_Number_1 == "Coffee":
    print("That will be 1.50 dollars. I used my employee mark-up, though. 85 dollars, please...")
    order.append(Order_Number_1)
    Cost = (Cost + 85)
elif Order_Number_1 == "Donut" :
    print("The donuts would have been 3 dollars, but because of our talented chefs... we will pay you 5 dollars...")
    order.append(Order_Number_1)
    Cost = (Cost - 5)
elif Order_Number_1 == "Both" :
    print("That will be 80 dollars... We wish you luck...")
    order.append(Order_Number_1)
    Cost = (Cost + 80)
else :
    print("We are Timmy's Tacos... we obviously dont serve tacos or anything else here... lets try again...")

# The other menu

Order_Number_2 = input("We want more money! Order more! Would you like a main corse or a dessert?")
if Order_Number_2 == "Main Course" :
    Main_Course = input("Great! What would you like? Pancakes or Waffles?")
    if Main_Course == "Pancakes" :
        print("Thats a pretty lame choice... Cash or card? Your total is...")
        order.append(Main_Course)
        Cost = (Cost + 25)
    elif Main_Course == "Waffles" :
        print("Awesome! Your total is... ")
        order.append(Main_Course)
        Cost = (Cost + 30)
    else :
        print("We dont serve that... Restart... ")
elif Order_Number_2 == "Dessert" :
    Dessert = input("Great! Would you like a chocolate crape or croissant? ")
    if Dessert == "Chocolate Crape" :
        print("Fantastic! Your total is...")
        order.append(Dessert)
        Cost = (Cost + 20)
    elif Dessert == "Croissant" :
        print("Great! Your total is...")
        order.append(Dessert)
        Cost = (Cost + 15)
else :
    print("We are Timmy's Tacos... we obviously dont serve tacos or anything else here... lets try again...")
print(order)
print(Cost)