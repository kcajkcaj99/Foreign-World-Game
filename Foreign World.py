
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
def combat(cstats, cdamagemin, cdamagemax, cweapon, etype, elocation, cmagic, etitle):
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
        ehealth = 7
        ehealthmax = 7
        eatkmin = 2
        eatkmax = 5
        earmor = 1
        eweaponname = "Bite"
        earmorname = "Fur"
        einventory = list([("Wolf Corpse")])
        eai = "Aggressive"

    # This code writes a description based on the location and enemy type.
    if elocation == "Field":
        starterdescription = (etitle+" stands in the grass ahead of you, bearing its "+str.lower(eweaponname)+".")

    # This introduces the combat
    print (starterdescription)

    # This defines any combat variables
    ehit = 0
    burnout = 0

    # This runs the combat
    while chealth > 0 and ehealth > 0 and health > 0:
        # This code asks you what you want to do.
        print ("What do you do?")
        print ("    1: Nothing.")
        print ("    2: Run away.")
        print ("    3: Attack.")
        if cmagic == 1:
            print ("    5: Cast a spell.")
        caction = input ("")

        '''
        # This code runs if you want to use an item.
        if caction == "2":
            # This code asks you what items you want to use.
            print ("You have the following items in your inventory:")
            count = 0
            for item in inventory:
                count += 1

            print ("Name the item you want to use.")
            citem = input ("")
        '''
        # This code runs if you try to run
        if caction == "2":
            if eai == "Aggressive":
                print("You run, but the "+str.lower(etype)+" chases you.")
            elif eai == "Defensive":
                print ("You run, and the "+str.lower(etype)+" does not give chase.")
                break

        # This code runs if you attack.
        elif caction == "3":
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
        elif caction == "4" and cmagic == 1:
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

while True: #everything is in a giant while loop so that the game can be reset afterward.
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
    PoisonBerryName = BasicBerryName
    while PoisonBerryName == BasicBerryName:
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

    # The following code sets Wolf related names
    WolfFurColor = randchoice(["Grey", "White", "Black", "Brown"])
    WolfName = "A fanged, bipedal "+str.lower(WolfFurColor)+"-furred animal"
    WolfFurName = "A piece of "+str.lower(WolfFurColor)+" fur"
    WolfFangName = "A "+randchoice(["curved", "long", "serrated"])+" fang"
    WolfCorpseName = "The corpse of "+str.lower(WolfName)
    WolfMeatName = "The uncooked meat of "+str.lower(WolfName)


    # The following code sets wood names.
    BasicWoodName = "A "+randchoice(list(["dark", "light", "red", "pale"]))+" wood"
    BasicTwigName = "A twig made of "+str.lower(BasicWoodName)
    BasicBranchName = "A branch made of "+str.lower(BasicWoodName)
    RabbitsClubName = "A rabbit's club made of " + str.lower(BasicWoodName)
    # The following code sets your characters abilities
    health = 12
    inventory = list ([BasicFruitName, BasicFruitName, BasicFruitName, SecondaryFruitName, BasicClothesName])
    armor = 0
    mana = 10
    magic = 0
    hunger = 75
    ClothesName = [BasicClothesName]
    sleeptime = 0
    warm = 0
    furnace = 0
    time = 0
    inittime = 0
    weapon = "Fists"
    damagemin = 1
    damagemax = 4
    event = 0
    fire = 0
    luck = 0
    firetime = -1 #If the player makes a campfire, this is the # of hours since the fire has been started. It dies down after 24 hours of not being fed. The player can feed it with twigs and branches.
    starving = 0
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
        print("So far, you have survived for " + str(4*time) + " hours.")
        print("Your health: " + str(health) + "/12")
        print("Your hunger level: " + str(hunger) + "/100 (higher is more full)")
        if fire == 1:
            print("Your fire should burn for " + str(firetime) + " more hours.")
        if luck > 0:
            print("Your good luck score: " + str(luck))
        hungerstr = "You are not hungry."

        if warm == 0:
            randchance = random.randint(1, 3)
            if randchance == 1:
                print ("You are freezing.")
                health -= timediff
            else:
                print ("You are cold.")
        if (time > 6 and event == 0) or (random.randint(1, 40) == 1 and event == 1):
            print()
            stats = list([health, inventory, armor, mana])
            stats = combat(stats, damagemin, damagemax, weapon, "Wolf", "Field", magic, WolfName)
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
        print ("    e: Eat something")
        print ("    g: Change garments")
        print ("    s: Search for things")
        print ("    r: Rest")
        print ("    c: Craft")
        print ("    h: Hunt")
        if fire == 1:
            print("    f: Feed the campfire")
      #  print ("    w: Change weapons")
        print ("    ?: Help")
        action = str.lower(input (""))
        print()
        # This code executes eating
        if action == "e":
            foodnames = [BasicFruitName, SecondaryFruitName, TertiaryFruitName, PoisonBerryName, BasicBerryName, FlaxSeedName]
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
            if "Raw wolf meat" in inventory:
                print ("    7: Raw wolf meat")
            if "Burnt wolf meat" in inventory:
                print ("    8: Burnt wolf meat")
            if "Cooked wolf meat" in inventory:
                print ("    9: Cooked wolf meat")
            if "Raw rabbit meat" in inventory:
                print ("    10: Raw rabbit meat")
            if "Cooked rabbit meat" in inventory:
                print ("    11: Cooked rabbit meat")
            if "Burnt rabbit meat" in inventory:
                print ("    12: Burnt rabbit meat")
            action = input("")
            print()
            # This code runs the results of what you eat.
            if action == "1" and BasicFruitName in inventory:
                print ("You eat "+str.lower(BasicFruitName))
                inventory.remove(BasicFruitName)
                hunger += 15
                health += 0.5
            if action == "2" and SecondaryFruitName in inventory:
                print ("You eat "+str.lower(SecondaryFruitName))
                inventory.remove(SecondaryFruitName)
                hunger += 20
                health += 0.5
            if action == "3" and TertiaryFruitName in inventory:
                print ("You eat "+str.lower(TertiaryFruitName))
                inventory.remove(TertiaryFruitName)
                hunger += 20
                health += 0.5
            if action == "4" and PoisonBerryName in inventory:
                print ("You eat "+str.lower(PoisonBerryName)+". It makes you feel sick.")
                inventory.remove(PoisonBerryName)
                health -= random.randint(1, 3)
            if action == "5" and BasicBerryName in inventory:
                print ("You eat "+str.lower(BasicBerryName))
                inventory.remove(BasicBerryName)
                hunger += 5
                health += 0.25
            if action == "6" and FlaxSeedName in inventory:
                print ("You eat "+str.lower(FlaxSeedName))
                inventory.remove(FlaxSeedName)
                hunger += 2
                health += 0.25
            if action == "7" and "Raw wolf meat" in inventory:
                inventory.remove("Raw wolf meat")
                if random.randint(0, 1) == 0: #Sometimes it should make you sick, sometimes it shouldn't.
                    print("You eat the raw wolf meat.")
                    hunger += 15
                    health += 1
                else:
                    print("You eat the raw wolf meat. It makes you feel sick.")
                    health -= random.randint(2, 4)
            if action == "8" and "Burnt wolf meat" in inventory:
                print ("You eat the burnt wolf meat. It tastes disgusting.")
                inventory.remove("Burnt wolf meat")
                hunger += 10
                health += 1
            if action == "9" and "Cooked wolf meat" in inventory:
                print ("You eat the cooked wolf meat.")
                inventory.remove("Cooked wolf meat")
                hunger += 30
                health += 5
            if action == "10" and "Raw rabbit meat" in inventory:
                inventory.remove("Raw rabbit meat")
                if random.randint(0, 1) == 0: #Sometimes it should make you sick, sometimes it shouldn't.
                    print("You eat the raw rabbit meat.")
                    hunger += 10
                    health += 1
                else:
                    print("You eat the raw rabbit meat. It makes you feel sick.")
                    health -= random.randint(2, 4)
            if action == "11" and "Cooked rabbit meat" in inventory:
                print ("You eat the cooked rabbit meat.")
                inventory.remove("Cooked rabbit meat")
                hunger += 17
                health += 2
            if action == "12" and "Burnt rabbit meat" in inventory:
                print ("You eat the burnt rabbit meat. It tastes disgusting.")
                inventory.remove("Burnt rabbit meat")
                hunger += 7

            #These next lines make sure that you don't have more than 100 hunger and 12 health.
            if hunger > 100:
                hunger = 100
            if health > 12:
                health = 12
        #This code executes searching your inventory
        elif action == "i":
            print ("You are wearing: ")
            for x in ClothesName:
                print(x)
            print("\nYour inventory:\n")
            count = 0
            for item in inventory:
                count += 1
                print(str(count) + ". " + item)

        #This code executes changing clothing
        elif action == "g":
            # This code asks you want you want to wear
            print ("What do you want to wear?")
            if BasicClothesName in inventory and (not BasicClothesName in ClothesName):
                print ("    bc: "+ BasicClothesName)
            if FlaxClothesName in inventory and (not FlaxClothesName in ClothesName):
                print ("    fc: "+ FlaxClothesName)
            if "A fur coat" in inventory and (not "A fur coat" in ClothesName):
                print ("    co: A warm fur coat")
            if "A good luck charm" in inventory and (not "A good luck charm" in ClothesName):
                print ("    gl: A good luck charm")
            action = input("")
            if action == "bc" and BasicClothesName in inventory:
                print ("You put on "+str.lower(BasicClothesName)+".")
                ClothesName += [BasicClothesName]
                if fire == 0:
                    warm = 0
            elif action == "fc" and FlaxClothesName in inventory:
                print ("You put on "+str.lower(FlaxClothesName)+".")
                ClothesName += [FlaxClothesName]
                if fire == 0:
                    warm = 0
            elif action == "co" and "A fur coat" in inventory:
                print ("You put on the fur coat. It is warm.")
                ClothesName += ["A fur coat"]
                warm = 1
            elif action == "gl":
                print ("You put on the good luck charm. It gives you a +5 good luck score!")
                ClothesName += ["A good luck charm"]
                luck = 5
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
            time += 0.25
            hunger -= 10
        #This code executes processing raw materials
        elif action == "p":
            #This code asks what you want to process
            print ("What do you want to process?")
            if FlaxName in inventory:
                print ("    1: "+str.lower(FlaxName))
            action = input("")

        # This code executes resting
        elif action == "r":
            print ("You rest for a while, and are now well rested.")
            hunger -= int(3*sleeptime)
            time += 1+(sleeptime/2)
            sleeptime = 0
            hunger -= 3

        # This code executes crafting
        elif action == "c":
            cancraft = "" #This is similar to the string "canbuild." It remains empty unless you can craft something.

            if FlaxName in inventory:
                cancraft += ("    fl: Extract seeds from "+str.lower(FlaxName) + ".\n")
            if FlaxFibreName in inventory:
                cancraft += ("    tw: Spin twine out of "+str.lower(FlaxFibreName)+".\n")
            if inventory.count(FlaxTwineName) >= 4:
                cancraft += ("    ft: Weave fabric out of "+str.lower(FlaxTwineName)+".\n")
            if inventory.count(FlaxFabricName) >= 7:
                cancraft += ("    fc: Weave fabric out of "+str.lower(FlaxClothesName)+".\n")
            if "Wolf Corpse" in inventory:
                cancraft += ("    sw: Skin the wolf corpse.\n")
            if "Wolf hide" in inventory:
                cancraft += ("    wc: Make a fur coat out of wolf hide.\n")
            if "Raw wolf meat" in inventory and fire == 1:
                cancraft += ("    cw: Cook the wolf meat over the fire.\n")
            if (inventory.count(BasicTwigName)) > 3 and (inventory.count(BasicBranchName)) > 1:
                cancraft += ("    cf: A basic campfire consisting of 4 twigs and 2 branches.\n")
            if BasicBranchName in inventory:
                cancraft += ("    rc: " + RabbitsClubName + " for hunting game.\n")
            if "Rabbit corpse" in inventory:
                cancraft += ("    sr: Skin a rabbit's corpse\n")
            if "Raw rabbit meat" in inventory:
                cancraft += ("    cr: Cook the raw rabbit meat\n")
            if "Rabbit foot" in inventory and FlaxTwineName in inventory:
                cancraft += ("    gl: Make a \"Good luck\" charm")
            if cancraft == "":
                print ("Sorry, you cannot craft anything with your current inventory.")

            else:
                print(cancraft)
                action = input("What do you want to craft?")

                if action == "fl" and FlaxName in inventory:
                    count = random.randint(0, 5)
                    while count > 0:
                        inventory += [FlaxSeedName]
                        print ("You have extracted " + str.lower(FlaxSeedName) + ".")
                        count -= 1
                    count = random.randint(1, 2)
                    while count > 0:
                        inventory += [FlaxFibreName]
                        print ("You have extracted " + str.lower(FlaxFibreName) + ".")
                        count -= 1
                    inventory.remove(FlaxName)
                    sleeptime += 0.5
                    time += 1
                    hunger -= 3
                # This code makes flaxen twine
                if action == "tw" and FlaxFibreName in inventory:
                    inventory.remove(FlaxFibreName)
                    inventory += [FlaxTwineName]
                    print ("You spin "+FlaxTwineName+".")
                    sleeptime += 0.1
                    time += 0.1
                # This code makes flaxen fabric
                elif action == "ft" and inventory.count(FlaxTwineName) > 3:
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
                elif action == "fc" and inventory.count(FlaxFabricName) > 7:
                    recurrence = 8
                    while recurrence > 0:
                        inventory.remove(FlaxFabricName)
                        recurrence -= 1
                    inventory += [FlaxClothesName]
                    print ("You make "+str.lower(FlaxClothesName)+".")
                    sleeptime += 0.75
                    time +=0.75
                    hunger -= 3
                elif action == "sw" and "Wolf Corpse" in inventory:
                    sleeptime += 0.75
                    time += 0.75
                    hunger -= 3
                    inventory.remove("Wolf Corpse")
                    inventory += ["Wolf hide", "Raw wolf meat"]
                    print ("You skin the wolf. Now, you have a wolf hide and raw wolf meat.")
                elif action == "wc" and "Wolf hide" in inventory:
                    print ("You make a fur coat from the wolf hide.")
                    inventory.remove("Wolf hide")
                    sleeptime += 0.75
                    time += 0.75
                    hunger -= 3
                    inventory += ["A fur coat"]
                elif action == "cw" and "Raw wolf meat" in inventory:
                    inventory.remove("Raw wolf meat")
                    if random.randint(1, 3) == 1:
                        print("You burn the wolf meat to a crisp.")
                        inventory += ["Burnt wolf meat"]
                    else:
                        print("You carefully cook the wolf meat. It looks delicious.")
                        inventory += ["Cooked wolf meat"]
                    sleeptime += 0.75
                    time += 0.75
                    hunger -= 3
                elif action == "cf"and (inventory.count(BasicTwigName)) > 3 and (inventory.count(BasicBranchName)) > 1:
                    # This code consumes twigs.
                    count = 4
                    while count > 0:
                        if BasicTwigName in inventory:
                            inventory.remove(BasicTwigName)
                        count -= 1
                    # This code consumes branches
                    count = 2
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
                    warm = 1
                    firetime = 24
                elif action == "rc" and BasicBranchName in inventory:
                    print("You make " + str.lower(RabbitsClubName) + ". Now you can hunt rabbits!")
                    inventory.remove(BasicBranchName)
                    inventory += [RabbitsClubName]
                    sleeptime += 1
                    time += 1
                    hunger -= 5
                elif action == "sr" and "Rabbit corpse" in inventory:
                    #This code skins a rabbit corpse
                    print ("You skin the rabbit's corpse. Now, you have a rabbit hide, a rabbit's foot, and raw rabbit meat.")
                    inventory.remove("Rabbit corpse")
                    inventory += ["Rabbit hide", "Rabbit foot", "Raw rabbit meat"]
                    sleeptime += 1
                    time += 1
                    hunger -= 5
                elif action == "cr" and "Raw rabbit meat" in inventory:
                    inventory.remove("Raw rabbit meat")
                    if random.randint(1, 3) == 1:
                        print("You burn the rabbit meat to a crisp.")
                        inventory += ["Burnt rabbit meat"]
                    else:
                        print("You carefully cook the rabbit meat. It looks delicious.")
                        inventory += ["Cooked rabbit meat"]
                    sleeptime += 0.75
                    time += 0.75
                    hunger -= 3
                elif action == "gl" and "Rabbit foot" in inventory and FlaxTwineName in inventory:
                    inventory.remove("Rabbit foot")
                    inventory.remove(FlaxTwineName)
                    print("You make a good luck charm! Wear it to get good luck.")
                    inventory += ["A good luck charm"]

        elif action == "h":
            #This code facilitates hunting.
            canhunt = ""
            if RabbitsClubName in inventory:
                canhunt += "r: Hunt rabbits"
            if canhunt == "":
                print("Sorry, you need to craft a weapon in order to hunt.")
            else:
                print("What do you want to hunt?")
                action = input(canhunt)
                if str.lower(action) == "r" and RabbitsClubName in inventory:
                    outcome = random.randint(1, 3)
                    if outcome == 1:
                        print ("You see a rabbit and throw your club at it. You hit it! You collect the rabbit corpse.")
                        inventory += ["Rabbit corpse"]
                    elif outcome == 2:
                        print ("You see a rabbit and throw your club at it. You miss.")
                    else:
                        print ("You go looking for game but you cannot find anything.")
                health -= 1
                hunger -= 10
        elif action == "f" and fire == 1:
            canfeed = ""

            if BasicBranchName in inventory:
                canfeed += "     b: " + str.lower(BasicBranchName) + "\n"
            if BasicTwigName in inventory:
                canfeed += "     t: " + str.lower(BasicTwigName) + "\n"

            if canfeed == "":
                print("Sorry, you need a twig or a branch to feed the fire with.")
            else:
                print("What do you want to feed the fire with?")
                print("The fire will last for " + str(firetime) + "more hours.")
                action = input(canfeed)
                if action == "b" and BasicBranchName in inventory:
                    inventory.remove(BasicBranchName)
                    firetime += 4
                if action == "t" and BasicTwigName in inventory:
                    inventory.remove(BasicTwigName)
                    firetime += 2

        elif action == "?":
            print("Welcome to Foreign world! This is an in-depth explanation of how the commands work. \n"
                  "i - This lists your inventory.\n"
                  "e - This lets you eat something from your inventory. It adds to your health levels and subtracts from your hunger levels. Note that some foods are poisonous. Every time you restart the game, the colors of poisonous foods change.\n"
                  "g - This lets you change clothes if you have made any new clothes (using the craft command)\n"
                  "s - This lets you gather items for your inventory. You can search for berries, flowers, and twigs/branches.\n"
                  "r - If the game says you are tired, this will make you slightly less tired. But beware of wolves!\n"
                  "c - Lets you make/cook/process things. See below for a crafting guide.\n"
                  "h - Hunting requires a weapon, such as a rabbit's club. If done successfully, you get an animal corpse."
           #       "w - Change weapons, if you have any weapons in your inventory.\n\n\n"
                  "A good way to start is to gather enough twigs and branches to start a fire."
                  "Have fun!\n")
        print()
        firetime -= timediff*4
        if firetime <= 0 and fire == 1:
            print("Your fire died out! Remember to feed it with twigs and branches.")
            fire = 0
            if not ("A fur coat" in ClothesName):
                warm = 0
        if health <= 0:
            print ("Your health is below 0! You die!")
            break
        if hunger > 0:
            starving = 0
        if hunger <= 0 and starving == 0:
            print ("You are starving! You need to eat something quick!")
            hunger = 1
            starving = 1
        if hunger <= 0 and (not starving == 0):
            print ("You died of hunger!")
            break
    exitinput = input("You died! You lasted for "+str(int(4*time))+" hours. Press enter to play again, or type \"quit\" to quit.")
    if exitinput.lower() == "quit":
        break