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
    print("Je bent nu in de winkel! \nDit zijn de producten die je nog moet pakken:", GroceryList)

    while True:
        if GroceryList[0] == "---" and GroceryList[1] == "---" and GroceryList[2] == "---" and GroceryList[3] == "---" and GroceryList[4] == "---":
            print("Je bent klaar met boodschappen")
            break
        else:
            print("Wat wil je nu pakken?", GroceryList)

            antw = input()
            
        if antw == "Brood" and GroceryList[0] == "Brood":
            GroceryList[0] = "---"
            ShoppingCart[0] = "Brood"
            print("Je hebt brood gepakt!")
            time.sleep(1)
            os.system("clear")
            continue
        elif antw == "Worst" and GroceryList[1] == "Worst":
            GroceryList[1] = "---"
            ShoppingCart[1] = "Worst"
            print("Je hebt worst gepakt!")
            time.sleep(1)
            os.system("clear")
        elif antw == "Cola" and GroceryList[2] == "Cola":
            GroceryList[2] = "---"
            ShoppingCart[2] = "Cola"
            print("Je hebt cola gepakt!")
            time.sleep(1)
            os.system("clear")
        elif antw == "Chips" and GroceryList[3] == "Chips":
            GroceryList[3] = "---"
            ShoppingCart[3] = "Chips"
            print("Je hebt chips gepakt")
            time.sleep(1)
            os.system("clear")
        elif antw == "Melk" and GroceryList[4] == "Melk":
            GroceryList[4] = "---"
            ShoppingCart[4] = "Melk"
            print("Je hebt Melk Gepakt!")
            time.sleep(1)
            os.system("clear")
        elif antw != GroceryList[0:4]:
            print("Je hebt", antw, "al gepakt. Pak een ander product.")
            time.sleep(1)
            os.system("clear")
        else:
            print("Je kan aleen uit deze producten kiezen", GroceryList)
            time.sleep(1)
            os.system("clear")
            
    
    if ShoppingCart[0] != "" and ShoppingCart[1] != "" and ShoppingCart[2] != "" and ShoppingCart[3] != "" and ShoppingCart[4] != "":
        ShoppingCartLeeg = False


if ShoppingCartLeeg == False:
    print("Shopping Done")
    print(GroceryList)
    print(ShoppingCart)
