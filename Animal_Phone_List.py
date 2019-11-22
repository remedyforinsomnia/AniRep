
AnimalPhones = [("Whale", "+380979697786"),("Tapir", "+380999999999"),("Koala", "+380999998999"),("Cat", "+380999999799"),("Deer", "+380990999999")]


SpeciesInput = input("What animal are you interested in?\n")


for animal in AnimalPhones:
    species = animal[0]
    PhoneNo = animal[1]
    Lower = species.lower()
    

    
    if SpeciesInput in species or SpeciesInput in Lower:
         print("We have found your animal. The animal's number is" + PhoneNo)

if SpeciesInput not in AnimalPhones[0] and SpeciesInput not in AnimalPhones[1] and SpeciesInput not in AnimalPhones[2] and SpeciesInput not in AnimalPhones[3] and SpeciesInput not in AnimalPhones[4] and SpeciesInput not in Lower and SpeciesInput not in str(AnimalPhones[0]).lower() and SpeciesInput not in str(AnimalPhones[1]).lower() and SpeciesInput not in str(AnimalPhones[2]).lower() and SpeciesInput not in str(AnimalPhones[3]).lower() and SpeciesInput not in str(AnimalPhones[4]).lower():
     print("No such animal. Consider seeing Whale cuz she's extra friendly ^_^")
     
SpeciesInput = input("What animal are you interested in? Type in ""End"" to stop.\n")

while SpeciesInput != "End":
    
    for animal in AnimalPhones:
        species = animal[0]
        PhoneNo = animal[1]
        Lower = species.lower()
    
        if SpeciesInput in species or SpeciesInput in Lower:
            print("We have found your animal. The animal's number is" + PhoneNo)

    if SpeciesInput not in AnimalPhones[0] and SpeciesInput not in AnimalPhones[1] and SpeciesInput not in AnimalPhones[2] and SpeciesInput not in AnimalPhones[3] and SpeciesInput not in AnimalPhones[4] and SpeciesInput not in Lower and SpeciesInput not in str(AnimalPhones[0]).lower() and SpeciesInput not in str(AnimalPhones[1]).lower() and SpeciesInput not in str(AnimalPhones[2]).lower() and SpeciesInput not in str(AnimalPhones[3]).lower() and SpeciesInput not in str(AnimalPhones[4]).lower():
        print("No such animal. Consider seeing Whale cuz she's extra friendly ^_^")

    SpeciesInput = input("What animal are you interested in? Type in ""End"" to stop.\n")        
    

