current_Money = 0

while current_Money < 75:
    
    money = int(input("""Input Coins
                  50p
                  20p
                  10p
                  5p
                  : """))
    current_Money += money
    moneyLeft = 75 - current_Money
    print(str(moneyLeft)+"p left to give.")
    
    if current_Money >= 75:
        change = current_Money - 75

print("Your change is: "+str(change)+"p")
    
