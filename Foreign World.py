import random
import time

# The following code defines how to remove spelling and punctuation.

def removepunc(listx):
    def removeall (listy, removed):
        while listy.count (removed) > 0:
            listy.remove(removed)
        return(listy)
    listx = removeall(listx, ".")
    listx = removeall(listx, ",")
    listx = removeall(listx, "'")
    listx = removeall(listx, "!")
    listx = removeall(listx, "?")
    listx = removeall(listx, "'")
    listx = removeall (listx, "/")
    return listx

def formstring (listz):
    count = 0
    word = ""
    while count < len(listz):
        word += listz[count]
        count += 1
    return word

# The following code defines how combat works
def combat(cstats, cdamagemin, cdamagemax, cweapon, etype, elocation, cmagic, extraestats):
    # The following code defines how to remove punctuation

    def removepunc(listx):
        def removeall (listy, removed):
            while listy.count (removed) > 0:
                listy.remove(removed)
            return(listy)
        listx = removeall(listx, ".")
        listx = removeall(listx, ",")
        listx = removeall(listx, "'")
        listx = removeall(listx, "!")
        listx = removeall(listx, "?")
        listx = removeall(listx, "'")
        listx = removeall (listx, "/")
        listx = removeall(listx, " ")
        return listx

    def formstring (listz):
        count = 0
        word = ""
        while count < len(listz):
            word += listz[count]
            count += 1
        return word

    # The following code defines how to make random choices from a list.
    def randchoice(listy):
        numy = random.randint(1, len(listy)) - 1
        return listy[numy]

    # This code parses your stats into its parts
    chealth = cstats[0]
    cinventory = cstats[1]
    carmormax = cstats[2]
    carmor = cstats[2]
    cmana = cstats[3]

    # This code defines your enemies' stats based on its' type.
    if etype == "Guard":
        ehealth = 12
        ehealthmax = 12
        eatkmin = 2
        eatkmax = 10
        earmor = 4
        eweaponname = "Spear"
        earmorname = "Armor"
        einventory = list(["Spear", "Mail Armor"])
        eai = "Defensive"
    elif etype == "Soldier":
        ehealth = 12
        ehealthmax = 12
        eatkmin = 2
        eatkmax = 10
        earmor = 4
        eweaponname = "Spear"
        earmorname = "Armor"
        einventory = list(["Spear", "Mail Armor"])
        eai = "Aggressive"
    elif etype == "Wolf":
        ehealth = 5
        ehealthmax = 5
        eatkmin = 2
        eatkmax = 5
        earmor = 1
        eweaponname = "Bite"
        earmorname = "Fur"
        einventory = list([extraestats[1]])
        eai = "Aggressive"
        etype = extraestats[0]

    # This code writes a description based on the location and enemy type.
    if elocation == "Field":
        starterdescription = ("A "+str.lower(etype)+" stands in the grass ahead of you, bearing its "+str.lower(eweaponname)+".")

    # This introduces the combat
    print (starterdescription)

    # This defines any combat variables
    ehit = 0
    burnout = 0

    # This runs the combat
    while chealth > 0 and ehealth > 0:
        # This code asks you what you want to do.
        print ("What do you do?")
        print ("    1: Nothing.")
        print ("    2: Use an item.")
        print ("    3: Run away.")
        print ("    4: Attack.")
        if cmagic == 1:
            print ("    5: Cast a spell.")
        caction = input ("")

        # This code runs if you want to use an item.
        if caction == "2":
            # This code asks you what items you want to use.
            print ("You have the following items in your inventory: "+str(cinventory))
            print ("Name the item you want to use.")
            citem = input ("")

        # This code runs if you try to run
        elif caction == "3":
            if eai == "Aggressive":
                print("You run, but the "+str.lower(etype)+" chases you.")
            elif eai == "Defensive":
                print ("You run, and the "+str.lower(etype)+" does not give chase.")
                break

        # This code runs if you attack.
        elif caction == "4":
            print ("You attack with your "+str.lower(cweapon))
            damage = random.randint(cdamagemin, cdamagemax)
            ehit = 1
            if damage > earmor:
                print ("Your attack hits the "+str.lower(etype)+", dealing "+str(damage)+" damage!")
                ehealth -= damage
            else:
                print ("Your attack bounces off the "+str.lower(etype)+"'s "+str.lower(earmorname)+".")
                earmor -= 1

        # This code runs if you try to cast a spell.
        elif caction == "5" and cmagic == 1:
            print ("Enter your magic phrase.")
            cspell = formstring(removepunc(list(str.lower(input ("")))))
            # This handles the various spells in the game
            if cspell == "laedote" and cmana >= 10:
                damage = random.randint(3, 9)
                print("You fire a bolt of magic towards the "+str.lower(etype)+", dealing "+str(damage)+" damage.")
                ehealth -= damage
                ehit = 1
                burnout += random.randint(1, 2)
                cmana -= 10
            elif cspell == "sanome" and cmana >= 20:
                print ("A wave of healing passes over you, causing you to regain 3 hitpoints.")
                chealth += 3
                if chealth > 12:
                    chealth = 12
                burnout += random.randint(1, 2)
                cmana -= 20
            elif cspell == "medeortibi" and cmana >= 20:
                print ("A wave of healing passes over the "+str.lower(etype)+", causing it to regain 3 hitpoints.")
                ehealth += 3
                if ehealth > ehealthmax:
                    ehealth = ehealthmax
                burnout += random.randint(1, 2)
                cmana -= 20
            # This handles magic explosions caused by improper casting
            else:
                damage = random.randint(4, 10)
                print("The magic explodes in your face, dealing "+str(damage)+" damage to you.")
                chealth -= damage
                burnout += 2
            # This handles burnout
            if burnout > 3:
                damage = random.randint(1, int(burnout))
                print("As you cast the spell, it drains your spirit energy with it's power, dealing "+str(int(burnout))+" damage to you.")
                chealth -= damage

        # This code lets you wait for an enemy response.
        else:
            print ("You wait for the "+str.lower(etype)+" to react.")

        if caction != 4:
            burnout -= 1

        if burnout <= 0:
            burnout = 0

        print ()

        # This code determines the enemy reaction.
        if ehealth > 0:
            if eai == "Aggressive":
                print ("The "+str.lower(etype)+" attacks you with its "+str.lower(eweaponname)+".")
                damage = random.randint(eatkmin, eatkmax)
                if damage > carmor:
                    print ("The attack hits you, dealing "+str(damage)+" damage!")
                    chealth -= damage
                else:
                    print ("The attack bounces off of your armor.")
                    carmor -= 1
            elif eai == "Defensive":
                if ehit == 0:
                    print ("The "+str.lower(etype)+" waits to see what you do next.")
                else:
                    print ("The "+str.lower(etype)+" attacks you with its "+str.lower(eweaponname)+".")
                    damage = random.randint(2, 10)
                    if damage > carmor:
                        print ("The attack hits you, dealing "+str(damage)+" damage!")
                        chealth -= damage
                    else:
                        print ("The attack bounces off of your armor.")
                        carmor -= 1

        # This code performs upkeep at the end of the round
        print()
        print ("You have "+str(int(chealth))+" health remaining.")
        if magic == 1:
            print ("You have "+str(int(cmana))+" mana remaining.")
        print()
        if ehealth <= 0:
            print ("You slay the "+str.lower(etype+"!"))
            print ("You get "+str(einventory)+"!")
            cinventory += einventory
            print ()
    # This code forms your stats from its parts
    cstats = list([chealth, cinventory, carmormax, cmana])
    return cstats

# The following code defines how to choose a random element from a list.

def randchoice(listy):
    numy = random.randint(1, len(listy)) - 1
    return listy[numy]

# The following code sets fruit names.

BasicFruitName = "A "+randchoice(list(["spherical", "tubular", "bulbous"]))+" "+randchoice(list(["red", "green", "yellow"]))+" fruit"
SecondaryFruitName = ""
while SecondaryFruitName == "" or SecondaryFruitName == BasicFruitName:
    SecondaryFruitName = "A "+randchoice(list(["spherical", "tubular", "bulbous"]))+" "+randchoice(list(["red", "green", "yellow"]))+" fruit"
TertiaryFruitName = ""
while TertiaryFruitName == "" or TertiaryFruitName == BasicFruitName or TertiaryFruitName == SecondaryFruitName:
    TertiaryFruitName = "A "+randchoice(list(["spherical", "tubular", "bulbous"]))+" "+randchoice(list(["red", "green", "yellow"]))+" fruit"

# The following code sets berry names.
BasicBerryName = "A "+randchoice(list(["red", "green", "blue", "black", "white", "pink", "purple", "magenta"]))+" berry"
PoisonBerryName = ""
while PoisonBerryName == "" or PoisonBerryName == BasicBerryName:
    PoisonBerryName = "A "+randchoice(list(["red", "green", "blue", "black", "white", "purple", "pink", "magenta"]))+" berry"

# The following code sets flax and flax fabric names.

FlaxName = "A "+randchoice(list(["small", "large", "wide", "tall", "clustered"]))+" "+randchoice(list(["red", "white", "pink", "purple", "blue", "orange", "yellow", "black"]))+" flower with a "+randchoice(list(["tall", "short", "rough"]))+" stem"
FlaxFibreColor = randchoice(list(["brown", "white", "black", "grey", "tan"]))
FlaxTwineName = "Some "+FlaxFibreColor+" twine"
FlaxFabricName = "A fibrous "+FlaxFibreColor+" fabric"
FlaxClothesName = "Clothes made from "+str.lower(FlaxFabricName)
FlaxSeedName = "A "+randchoice(list(["hard", "round", "sharp", "soft"]))+" "+randchoice(list(["golden", "brown", "tan", "black"]))+" seed"
FlaxFibreName = "A "+FlaxFibreColor+" fibre"

# The following code sets fabric names.

BasicFabricName = "A "+randchoice(list(["soft", "rough", "fleecy"]))+" "+randchoice(list(["red", "white", "brown", "black", "grey", "tan"]))+" fabric"

# The following code sets items made of various materials names
BasicClothesName = "Clothes made from " + str.lower(BasicFabricName)

# The following code sets wood names.
BasicWoodName = "A "+randchoice(list(["dark", "light", "red", "pale"]))+" wood"
BasicTwigName = "A twig made of "+str.lower(BasicWoodName)
BasicBranchName = "A branch made of "+str.lower(BasicWoodName)

# The following code sets Wolf related names
WolfFurColor = randchoice(["Grey", "White", "Black", "Brown"])
WolfName = "A fanged, bipedal "+str.lower(WolfFurColor)+"-furred animal"
WolfFurName = "A piece of "+str.lower(WolfFurColor)+" fur"
WolfFangName = "A "+randchoice(["curved", "long", "serrated"])+" fang"
WolfCorpseName = "The corpse of "+str.lower(WolfName)
WolfMeatName = "The uncooked meat of "+str.lower(WolfName)

# The following code sets your characters abilities
health = 12
inventory = list ([BasicFruitName, BasicFruitName, BasicFruitName, SecondaryFruitName, BasicClothesName])
armor = 0
mana = 10
magic = 0
hunger = 75
ClothesName = BasicClothesName
sleeptime = 0
fire = 0
furnace = 0
time = 0
inittime = 0
weapon = "Fists"
damagemin = 1
damagemax = 4
event = 0

# The following code forms your stats from its parts
stats = list([health, inventory, armor, mana])

# The following code begins the game

print ("Foreign World")

print ()
print ()
print ()
print ()
print ()
print ()
print ()

# This code runs the game
while True:
    timediff = time-inittime
    if health < 1:
        break
    # This code asks what you want to do
    if hunger < 1:
        print ("You are starving.")
        health -= timediff
    elif hunger < 10:
        print ("You are very hungry.")
    elif hunger < 25:
        print ("You are significantly hungry.")
    elif hunger < 50:
        print ("You are hungry.")
    elif hunger < 75:
        print ("You are slightly hungry.")
    if sleeptime > 11:
        print ("You are overtired.")
        health -= timediff
    elif sleeptime > 3:
        print ("You are tired.")
    elif sleeptime > 2:
        print ("You are a little tired.")
    if health < 3:
        print ("You are near death.")
    elif health < 6:
        print ("You are severely injured.")
    elif health < 12:
        print ("You are injured.")
    if fire == 0:
        randchance = random.randint(1, 3)
        if randchance == 1:
            print ("You are freezing.")
            health -= timediff
        else:
            print ("You are cold.")
    if time > 4 and event == 0:
        print()
        stats = list([health, inventory, armor, mana])
        stats = combat(stats, damagemin, damagemax, weapon, "Wolf", "Field", magic, list([WolfName, WolfCorpseName]))
        health = stats[0]
        inventory = stats[1]
        armor = stats[2]
        mana = stats[3]
        if health < 1:
            break
        event = 1
    inittime = time
    print ("What do you want to do?")
    print ("    i: Inspect your Inventory")
    print ("    e: Eat something.")
    print ("    g: Change garments")
    print ("    s: Search for things")
    print ("    p: Process raw materials")
    print ("    r: Rest")
    print ("    c: Craft")
    print ("    b: Build")
    print ("    w: Change weapons")
    action = str.lower(input (""))
    print()
    # This code executes eating
    if action == "e":
        # This code asks what you want to eat
        print ("What do you want to eat?")
        if BasicFruitName in inventory:
            print ("    1: "+BasicFruitName)
        if SecondaryFruitName in inventory:
            print ("    2: "+SecondaryFruitName)
        if TertiaryFruitName in inventory:
            print ("    3: "+TertiaryFruitName)
        if PoisonBerryName in inventory:
            print ("    4: "+PoisonBerryName)
        if BasicBerryName in inventory:
            print ("    5: "+BasicBerryName)
        if FlaxSeedName in inventory:
            print ("    6: "+FlaxSeedName)
        action = input("")
        print()
        # This code runs the results of what you eat.
        if action == "1" and BasicFruitName in inventory:
            print ("You eat "+str.lower(BasicFruitName))
            inventory.remove(BasicFruitName)
            hunger += 15
            if hunger > 100:
                hunger = 100
        if action == "2" and SecondaryFruitName in inventory:
            print ("You eat "+str.lower(SecondaryFruitName))
            inventory.remove(SecondaryFruitName)
            hunger += 20
            if hunger > 100:
                hunger = 100
        if action == "3" and TertiaryFruitName in inventory:
            print ("You eat "+str.lower(TertiaryFruitName))
            inventory.remove(TertiaryFruitName)
            hunger += 20
            if hunger > 100:
                hunger = 100
        if action == "4" and PoisonBerryName in inventory:
            print ("You eat "+str.lower(PoisonBerryName)+". It is poisonous.")
            inventory.remove(PoisonBerryName)
            health -= random.randint(1, 3)
        if action == "5" and BasicBerryName in inventory:
            print ("You eat "+str.lower(BasicBerryName))
            inventory.remove(BasicBerryName)
            hunger += 5
            if hunger > 100:
                hunger = 100
        if action == "6" and FlaxSeedName in inventory:
            print ("You eat "+str.lower(FlaxSeedName))
            inventory.remove(FlaxSeedName)
            hunger += 2
            if hunger > 100:
                hunger = 100
    #This code executes searching your inventory
    elif action == "i":
        print ("You are wearing "+str.lower(ClothesName)+".")
        print (inventory)
    #This code executes changing clothing
    elif action == "g":
        # This code asks you want you want to wear
        print ("What do you want to wear?")
        if BasicClothesName in inventory:
            print ("    1: "+BasicClothesName)
        if FlaxClothesName in inventory:
            print ("    2: "+FlaxClothesName)
        action = input("")
        if action == "1" and BasicClothesName in inventory:
            print ("You put on "+str.lower(BasicClothesName)+".")
            ClothesName = BasicClothesName
        elif action == "2" and FlaxClothesName in inventory:
            print ("You put on "+str.lower(FlaxClothesName)+".")
            ClothesName = FlaxClothesName
    #This code executes changing weapons
    elif action == "w":
        # This code asks you want you want to wield
        print ("What do you want to wield?")
        print ("    1: "+BasicClothesName)
        action = input("")
        if action == "1":
            print ("You are wielding your fists.")
            weapon = "Fists"
            damagemin = 1
            damagemax = 4
    #This code executes searching
    elif action == "s":
        # This code asks what you want to search for.
        print ("What do you want to search for?")
        print ("    b: Berries")
        print ("    f: Flowers")
        print ("    t: Twigs and Branches")
        action = input ("")
        print ("You have spent some time searching.")
        if str.lower(action) == "b":
            count = random.randint(3, 7)
            while count > 0:
                find = randchoice(list([BasicBerryName, BasicBerryName, PoisonBerryName]))
                inventory += [find]
                print ("You have found "+str.lower(find)+"!")
                count -= 1
        elif str.lower(action) == "f":
            count = random.randint(1, 4)
            while count > 0:
                find = randchoice(list([FlaxName, FlaxName, FlaxName]))
                inventory += [find]
                print ("You have found "+str.lower(find)+"!")
                count -= 1
        elif str.lower(action) == "t":
            count = random.randint(1, 3)
            while count > 0:
                find = randchoice(list([BasicTwigName, BasicTwigName, BasicTwigName, BasicTwigName, BasicTwigName, BasicBranchName, BasicBranchName]))
                inventory += [find]
                print ("You have found "+str.lower(find)+"!")
                count -= 1
        sleeptime += 1
        time += 1
        hunger -= 10
    #This code executes processing raw materials
    elif action == "p":
        #This code asks what you want to process
        print ("What do you want to process?")
        if FlaxName in inventory:
            print ("    1: "+str.lower(FlaxName))
        if WolfCorpseName in inventory:
            print ("    2: "+str.lower(WolfCorpseName))
        action = input("")
        # This code processes the flax plant
        if action == "1" and FlaxName in inventory:
            count = random.randint(0, 5)
            while count > 0:
                inventory += [FlaxSeedName]
                print ("You have extracted "+str.lower(FlaxSeedName)+".")
                count -= 1
            count = random.randint(1, 2)
            while count > 0:
                inventory += [FlaxFibreName]
                print ("You have extracted "+str.lower(FlaxFibreName)+".")
                count -= 1
            inventory.remove(FlaxName)
        # This code process a wolf corpse.
        if action == "2" and WolfCorpseName in inventory:
            count = random.randint(1, 3)
            while count > 0:
                inventory += [WolfFurName]
                print ("You have extracted"+str.lower(WolfFurName)+".")
                count -= 1
            count = random.randint(1, 2)
            while count > 0:
                inventory += [WolfMeatName]
                print ("You have extracted "+str.lower(WolfMeatName)+".")
                count -= 1
            count = random.randint(0, 2)
            while count > 0:
                inventory += [WolfFangName]
                print ("You have extracted "+str.lower(WolfFangName)+".")
                count -= 1
            inventory.remove(WolfCorpseName)
        sleeptime += 0.5
        time += 1
        hunger -= 3
    # This code executes resting
    elif action == "r":
        print ("You rest for a while, and are now well rested.")
        hunger -= int(3*sleeptime)
        time += 1+(sleeptime/2)
        sleeptime = 0
        hunger -= 3
    # This code executes crafting
    elif action == "c":
        print ("What do you want to craft?")
        if FlaxFibreName in inventory:
            print ("    1: Spin twine out of "+str.lower(FlaxFibreName)+".")
        if inventory.count(FlaxTwineName) >= 4:
            print ("    2: Weave fabric out of "+str.lower(FlaxTwineName)+".")
        if inventory.count(FlaxFabricName) >= 7:
            print ("    3: Weave fabric out of "+str.lower(FlaxClothesName)+".")
        action = input("")
        # This code makes flaxen twine
        if action == "1" and FlaxFibreName in inventory:
            inventory.remove(FlaxFibreName)
            inventory += [FlaxTwineName]
            print ("You spin "+FlaxTwineName+".")
            sleeptime += 0.1
            time += 0.1
        # This code makes flaxen fabric
        elif action == "2" and inventory.count(FlaxTwineName) > 3:
            inventory.remove(FlaxTwineName)
            inventory.remove(FlaxTwineName)
            inventory.remove(FlaxTwineName)
            inventory.remove(FlaxTwineName)
            inventory += [FlaxFabricName]
            print ("You weave "+str.lower(FlaxFabricName)+".")
            sleeptime += 0.5
            time += 0.5
            hunger -= 2
        # This code makes flaxen clothes
        elif action == "3" and inventory.count(FlaxFabricName) > 7:
            recurrence = 8
            while recurrence > 0:
                inventory.remove(FlaxFabricName)
                recurrence -= 1
            inventory += [FlaxClothesName]
            print ("You make "+str.lower(FlaxClothesName)+".")
            sleeptime += 0.75
            time +=0.75
            hunger -= 3
    # This code executes building
    elif action == "b":
        # This code asks you what you want to build
        print ("What do you want to build?")
        if (inventory.count(BasicTwigName)) > 4 and (inventory.count(BasicBranchName)) > 2 and fire != 1 and furnace < 1:
            print ("    1: A basic campfire")
        action = input()
        # This code builds a campfire
        if action == "1" and (inventory.count(BasicTwigName)) > 4 and (inventory.count(BasicBranchName)) > 2:
            # This code consumes twigs.
            count = 5
            while count > 0:
                if BasicTwigName in inventory:
                    inventory.remove(BasicTwigName)
                count -= 1
            # This code consumes branches
            count = 3
            while count > 0:
                if BasicBranchName in inventory:
                    inventory.remove(BasicBranchName)
                count -= 1
            # This code creates the campfire and applies it's properties.
            fire = 1
            if furnace < 1:
                furnace = 1
            # This code manages the time and hunger incurred by building the campfire.
            sleeptime += 1
            time += 1
            hunger -= 5
    print()
print  ("You have died! Good game. You lasted for "+str(int(4*time))+" hours.")