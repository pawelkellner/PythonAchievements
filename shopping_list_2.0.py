import os
import time

GroceryList = ["Brood", "Worst", "Cola", "Chips", "Melk"]
ShoppingCart = ["", "", "", "", ""]

ShoppingCartLeeg = True

print("Hoi! Je hebt een lijst gekregen met volgende producten erop:\n", GroceryList,)
print("Je taak is om de producten te pakken en naar de kassa te gaan")

time.sleep(2)

os.system("clear")

while ShoppingCartLeeg == True:
    for word in GroceryList:
        antw = input()
        
        if antw == word:
            print("XD")
            continue
        else:
            break

    antw2 = input()

    if antw2 == "Y":
        ShoppingCartLeeg = False
        
    #if ShoppingCart[0] != "" and ShoppingCart[1] != "" and ShoppingCart[2] != "" and ShoppingCart[3] != "" and ShoppingCart[4] != "":
        #ShoppingCartLeeg = False


if ShoppingCartLeeg == False:
    print("Je winkelmand is vol!", ShoppingCart)
    print("En alles of je lijstje is afgestreepd", GroceryList)
    print("Doei!")
    time.sleep(1)
    os.system("clear")
