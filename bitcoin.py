"""Bitcoin բրոքերի օրինակ"""



purchase_price =float(input("Purchase Price: ") )
current_price = float(input("Current Price: ") )

if current_price < purchase_price * 0.9:
    print("Not a good idea to sell your bitcoin now")
    print("You will lose ", purchase_price - current_price, "dram per bitcoin")
elif current_price > purchase_price * 1.2:
    print("You will make ", purchase_price - current_price, "dram per bitcoin")
else:
    print("Not worth selling right now.")