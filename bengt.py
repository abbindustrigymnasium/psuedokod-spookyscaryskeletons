import math
 
def money(money):
    if money < 13.95:
        print("error")
       

    else:
        amountofthreepacks = math.floor(money/30)
     
        if amountofthreepacks < 1:
            money = math.floor(money/13.95)
            print("single cans:", money)
    
        else:
            moneyforthreepacks = amountofthreepacks*30
            moneyforsinglecan = money - moneyforthreepacks
     
            if moneyforsinglecan < 13.95:
                print(amountofthreepacks, "Amount of three packs")
    
            else:
                amountofsinglecans = math.floor(moneyforsinglecan/13.95)
                print("The amount of single cans is:",  amountofsinglecans, "The amount of three packs is:", amountofthreepacks)

money(347)