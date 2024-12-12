name = input("plz enter your name :")
if ( name =="VIP"):
   print("enjoy the show vor free")
else:   
   qt= int(input("how many tickets would you like to buy?"))
   total = qt * 15.5
   print(f"the total is ${total:.2f}")