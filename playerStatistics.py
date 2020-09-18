name_p = "Pawel"
surname_p = "Kellner"
age_p = 17
sex_p = "male"
skater_p = True
level_p = 69
car_p = "Chevrolet camaro"
game_p = "Escape from Tarkov"
currency_euro = "€"
money_p = 420692137
color_p = "Blue"



print("Kies een speler die je wilt gebruiken: Pawel")

speler_keuze = input()

if speler_keuze == "Pawel":
    print("Naam: " + name_p + "\nAchternaam: " + surname_p + "\nLeeftijd: " + str(age_p) + "\nGeslacht: " + sex_p + "\nSkateboarder: " + str(skater_p) + "\nLevel: " + str(level_p) + "\nAuto: " + car_p + "\nGame: " + game_p + "\nGeld: " + currency_euro + str(money_p) + "\nKleur: " + color_p)