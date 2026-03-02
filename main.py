print("Welcome to Timmy's Tacos. We have a wide selection of foods for you. We sell donuts for $3.00 and coffee for $1.50. We dont serve tacos...")
Order_Number_1= input("What would you like? Coffee, Donut, or both?")
if Order_Number_1 == "Coffee":
    print("That will be 1.50 dollars. I used my employee mark-up, though. 85 dollars, please...")
elif Order_Number_1 == "Donut" :
    print("The donuts would have been 3 dollars, but because of our talented chefs... we will pay you 5 dollars...")
elif Order_Number_1 == "Both" :
    print("That will be 80 dollars... We wish you luck...")
else :
    print("We are Timmy's Tacos... we obviously dont serve tacos or anything else here... lets try again...")