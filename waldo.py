import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)

for x in people:
    if x == "Waldo":
        break




print("Waldo is gevonden op plaats", people.index("Waldo") + 1)
print(people)
