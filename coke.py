coke_amount=50
while coke_amount>0:
    print("coke_amount: ", coke_amount)
    coin_inserted=int(input("Insert a coin, one by one: "))
    if coin_inserted in[25,10,5]:
        coke_amount-=coin_inserted
customers_change=abs(coke_amount)
print("change: ", customers_change)
