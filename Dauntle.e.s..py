import json
import commands as cmd

# Pre __name__ == "__main__" code:
# the def function is used in several places to cut down on script size
# Setup_room to create the next room json and update current_room variable
# what_do() to request and process an input from the player
# Use action = cmd.command(i[0], i[1]) to run commands system

# ROOM GUIDE: start room loading with if current_room == "your_room"
# put the i = what_do() command in a while loop called while current_room == "your_room"
# ask for action  = cmd.command() after i = what_do()
# end your room with if i[0] == "go":
#       if action != "no passage":
#           setup_room(action)

# REMEMBER TO UPDATE ROOM DICTIONARY IN JSON


def setup_room(my_room_name):
    global current_room
    # Load json content from rooms.json
    with open('rooms.json') as f:
        rooms = json.load(f)

    # Set starting room
    current_room = my_room_name.lower()

    return rooms, current_room


def what_do():
    correct_format = "no"
    while correct_format == "no":
        print("What do you want to do?")
        i = input().split(" ")

        if len(i) > 3 or len(i) < 2 or i[0] not in ["use", "go", "inspect", "talk"]:
            print("Command not recognized, remember to specify a command and an action")
        else:
            correct_format = "yes"

    return i


if __name__ == "__main__":

# establish endgame variables
    batter_death = False
    wire_death = False
    ribs_death = False
    cook_death = False
    duck_death = False
    not_finished = True
    victory = False

# establishing ingame variables
    usb_counter = 0
    broken_ribs = False



# intro and guide for the player
    start = False
    print("What's your name, traveler?")
    user_name = input()
    print("Hello", user_name, ", welcome aboard The Dauntle.SS")
    print("In this game, you have 4 commands to interact with the world.")
    print('"Inspect, Use, Go and Duck." Remember them well.')
    print(""""Inspect" is used to inspect object CAPITALIZED in text.""")
    print(""""Use" is used to use items in your inventory.""")
    print(""""Go" can be used to move to rooms North, East, South or West of your current location""")
    print("""Finally, "Duck" can be used to, well... duck. You wouldn't wanna hit your head, right?""")
    print("To use these commands type the command, then the object, item, or direction.")
    print("""For example: "inspect chest", "go west" or "use hammer" """)
    print("Bonus: use 'inspect inv' to check you inventory")
    while not start:
        print("Type 'yes' if you understand and want to start the game")

        understand = input()
        if understand == "yes":
            print("Off you go, good luck!")
            print("")
            print("----game start----")
            current_room = "entrance"
            start = True

# start game loop when not_finished = True
    while not_finished:


# ENTRANCE CODE

        if current_room == "entrance":

            print("")
            print("You find yourself in a dark room. You entered it, just a minute ago.")
            print("But as soon as you set foot inside, the entrance door closed behind you.")

            while current_room == "entrance":

                print("")
                print("The closed DOOR is behind you, but all you see in front of you now, is a CORRIDOR.")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_door":
                    print("The entrance door won't budge. You notice four light bulbs surrounding it.")
                    if usb_counter == 0:
                        print("All four bulbs are turned off.")
                    elif usb_counter == 1:
                        print("One of the four bulbs turned on! It's buzzing quietly.")
                    elif usb_counter == 2:
                        print("Two of the four bulbs have turned on. They're buzzing an adequate amount that's expected from 2 light bulbs.")
                    elif usb_counter == 3:
                        print("Three of the four bulbs have turned on. The electrical humming is getting a little loud for your liking.")
                    elif usb_counter == 4:
                        print("All four bulbs have turned on. The noise is deafening. Go forwards, EXIT!")

                if i[0] == "go":
                    if action == "exit" and usb_counter == 4:
                        print("All four light bulbs flicker briefly. A loud rumbling shakes the ground as you watch the door slowly slide open.")
                        print("As if it's this horrible ship's last goodbye, the door gets stuck at the top of the frame.")
                        print("You're just a bit too tall to leave comfortably.")
                        print("Input your final command, and leave this place!")

                        final_command = (input()).split(" ")

                        if "duck" in final_command:
                            victory = True
                            not_finished = False
                            current_room = ""

                        else:
                            not_finished = False
                            current_room = ""
                            duck_death = True


                    elif action == "exit":
                        print("The door is closed.", str(usb_counter), "out of four bulbs are lit up.")

                    elif action != "no passage":
                        setup_room(action)


# BOILER ROOM CODE - FINISHED

        if current_room == "boiler_room":

            print("")
            print("You walk into the boiler room. It is really stuffy in here")
            print("You can already feel yourself sweating from the boilers heat.")

            while current_room == "boiler_room":

                print("")
                print("You squint your eyes trying to look around the room.")
                print("You spot a dark CORNER a beaten and broken CABINET, and some sparking WIRES")

                i = what_do()
                action = cmd.command(i[0],i[1])

                if action == "i_corner":
                    print("You take a step closer to the dark corner. As your eyes adjust to the darkness,")
                    print("you bonk your ahead against some large OBJECT. For some reason you take up a fighting stance...")
                    print("As if you know how to fight", user_name)

                if action == "i_cabinet":
                    print("You pry open the cabinet with your hands. Great. Now you got a cut on your hands, dumbass")
                    print("You got it open though. There is a TOOLKIT inside")

                if action == "i_wires":
                    print("You take a look at the sparking wires. You can smell burner rubber.")
                    print("Maybe you could charge something with the electricity outputted from these wires...")

                if action == "i_object":
                    print("Apparently you bonked your head against a comically large small step ladder.")
                    print("You think it might come in handy later so you put it imn your pockets.")
                    print(":LADDER added to inventory:")
                    cmd.add_inv("ladder")

                if action == "i_toolkit":
                    print("While taking a closer look at the toolkit you notice that it has a bomb strapped to the side")
                    print("There is a red and blue wire, QUICK WHICH ONE DO YOU BITE THROUGH?!")
                    wire = ((input()).lower()).split(" ")

                    if "blue" in wire:
                        not_finished = False
                        current_room = ""
                        wire_death = True

                    else:
                        print("You somehow defused the bomb safely... who straps a bomb too a toolkit???")
                        print("You take a look inside the toolkit. There is a retro gun inside")
                        cmd.add_inv("gun")
                        print(":GUN added to inventory:")

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)


# HALLWAY A CODE - FINISHED

        if current_room == "hallway_a":

            print("")
            print("You step into a split hallway. The lights are flashing, probably due to a power shortage.")
            print("It's a good thing you don't have the flashing lights disease thingy.")

            while current_room == "hallway_a":

                print("")
                print("The hallway forks into two different doors. An EAST_DOOR and a WEST_DOOR")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_east_door":
                    print("""The plate above reads "Engine Room" """)
                    print("You try and open the door, but it seems very stuck. Would you like to ram the door?")
                    ram = (input()).split(" ")
                    if "yes" in ram:
                        print("YOU RAM YOUR ENTIRE BODY AGAINST THE DOOR")
                        print(user_name + ", you now have broken ribs... and the door is still closed")
                        broken_ribs = True
                        print(broken_ribs)

                if action == "i_west_door":
                    print("""The plate above reads "Boiler Room" """)
                    print("Somehow the door has been lodged out of place, providing passage to the west room.")

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)


# ENGINE ROOM CODE

        if current_room == "engine_room":

            while current_room == "engine_room":

                i = what_do()
                action = cmd.command(i[0], i[1])

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)


# STORAGE ROOM CODE

        if current_room == "storage":

            print("")
            print("You enter the storage room.")
            print("The room is stacked with futuristic items you have never seen before, all labeled with hologram tags.")
            print("They kinda look like advanced supermarket tags.")
            print("""Also you are pretty sure you read "Filtered Piss" on one of the tags.... tasty.""")

            while current_room == "storage":

                print("")
                print("There is a WINDOW in the back of the room.")
                print("Maybe the TAGS could be of some use, the PISS bottle also looked quite interesting.")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_tags":
                    print("You take a look at one of the tags. It seems they have mostly run out of batteries")
                    print("Maybe you could get a BATTERY from the tags somehow")
                if action == "i_battery":
                    print("You notice that the batteries are stored behind a lil' panel, much like a tv-remote, so you decide to get it out.")
                    print("How would you like to get the batteries out?")
                    print("")
                    print("aggressively")
                    print("carefully")
                    battery_get = (input()).split(" ")

                    if "aggressively" in battery_get and broken_ribs:
                        ribs_death = True
                        not_finished = False
                        current_room = ""


                    elif "aggressively" in battery_get:
                        print("you fucking batter-ram one of the tags against the WINDOW.")
                        batter_death = True
                        not_finished = False
                        current_room = ""


                    else:
                        print("you calmly remove the panel and take the battery out, it seems uncharged")
                        print(":EMPTY_BATTERY added inventory:")
                        cmd.add_inv("EMPTY_BATTERY")

                if action == "i_piss":
                    print("It's a jar of piss, I am not quite sure what you expected")
                    print("While infatuated with the jar of piss however, you notice a GLINT on one of the top shelfs.")

                if action == "i_glint":
                    print("You try to reach the shiny thing, but you just too small")
                    print("Maybe you could use something to reach it?")

                if action == "u_ladder":
                    print("You step on the ladder to reach the shiny object. With the add step you are able to reach.")
                    print("You've found 1 of the 4 USB's on the ship.")
                    print(":USB_A added to inventory:")
                    cmd.add_inv("usb_a")
                    print(":LADDER removed from inventory:")
                    cmd.remove_inv("ladder")

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)


# KITCHEN CODE - FINISHED

        if current_room == "kitchen":
            noise_gone = False
            print("")
            print("You... think this is a kitchen? It smells so bad in here, that you're suddenly thankful that you haven't eaten yet.")
            print("While trying to stomach the- uhm- intense... aroma... you look around.")

            while current_room == "kitchen":

                print("")
                print("It's a bit dingy, but you can see various COUNTERTOPS lined along the wall, a FRIDGE, a FURNACE and a POT on top of it.")
                if noise_gone == False:
                    print("you also hear some soft... wet... NOISE. You can just about make out a shape in the corner of the room.")
                else:
                    print("The CORPSE is laying motionless on the floor.")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_countertops":
                    print("You check all countertops thoroughly, but they don't seem to have anything of use to you.")

                if action == "i_fridge":
                    print("You open the fridge. You're greeted with a dim flickering white light and a Very pungent smell.")
                    print("You obtained some MYSTERY_MEAT. You're suddenly reminded of your mother's home cooking.")
                    print(":MYSTERY_MEAT added to inventory:")
                    cmd.add_inv("mystery_meat")

                if action == "i_stove":
                    print("It's covered in soot. You try to turn it on, but it's a wasted effort.")
                    print("You watch as the stove sputters out a final spark, before it moves on to the great beyond.")
                    print("All you gained from this is dirty soot-covered fingers, and a death on your conscience.")

                if action == "i_pot":
                    print("When you try to lift the lid off the pot, you struggle. It's completely caked shut.")
                    print("Just as you get ready to put more effort into it, something inside the pot clangs against the metal.")
                    print("You decide you don't want to know what's inside this pot anymore.")

                if action == "i_noise":
                    noise_gone = True
                    print("As you slowly approach the source of the noise, the shape snaps upwards.")
                    print("It is- it Was... the headchef. It seems he still has an affinity for good food though, as he's munching away on some poor fellow's corpse.")
                    print("Unfortunately for you, it's noticed you and is now lunging at you. I sure hope you've got a weapon to use.")

                    i = what_do()
                    action = cmd.command(i[0], i[1])

                    if action == "u_gun":
                        print("With a quick draw, you shoot the chef down. You think, and hope, his meal is dead. Poor CORPSE, what a way to go.")

                    elif action == "u_mystery_meat":
                        print("In a panic, you throw the disgusting mushy slab of meat into the furthest corner away from you.")
                        print("The chef seems interested in this well-aged delicacy you've put in front of him and rushes to go eat it.")
                        print("It leaves the CORPSE it was eating alone.")
                        cmd.remove_inv("mystery_meat")

                    else:
                        cook_death = True
                        not_finished = False
                        current_room = ""


                if action == "i_corpse":
                    print("Yup, definitely dead. Luckily you've played a lot of Skyrim in your time, and you know how to rob a corpse.")
                    print("You found a RED_KEY!")
                    print(":RED_KEY added to inventory:")
                    cmd.add_inv("RED_KEY")


                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)

 # NAVIGATION ROOM CODE

        if current_room == "navigation_room":

            while current_room == "navigation_room":

                i = what_do()
                action = cmd.command(i[0], i[1])

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)

 # CREW CABIN CODE

        if current_room == "crew_cabin":

            while current_room == "crew_cabin":

                i = what_do()
                action = cmd.command(i[0], i[1])

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)

 # HALLWAY B CODE

        if current_room == "hallway_b":

            while current_room == "hallway_b":

                i = what_do()
                action = cmd.command(i[0], i[1])

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)

 # SERVER ROOM CODE

        if current_room == "server_room":
            print("You enter into a musty room. Seems that there's no ventilation in here. ")

            while current_room == "server_room":
                print("")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)

 # HALLWAY C CODE

        if current_room == "hallway_c":

            while current_room == "hallway_c":

                i = what_do()
                action = cmd.command(i[0], i[1])

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)

 # BRIDGE CODE

        if current_room == "bridge":

            while current_room == "bridge":

                i = what_do()
                action = cmd.command(i[0], i[1])

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)
#END IN-LOOP SCRIPT

# end game when not_finished == False.
# these are the death screens:
    if wire_death:
        print("- You horrifically exploded into a million itty bitty parts -")
        print("Pro Tip: You should have chosen the red wire, you absolute buffoon.")

    if cook_death:
        print("- You are torn to shreds by the cook, who is happy to have found his next meal. -")
        print("Pro Tip: If only you had understood THE VERY OBVIOUS HINT...")

    if ribs_death:
        print("- Your ribs give in and collapse, you feel them puncture all your organs. -")
        print("Pro Tip: Maybe if you weren't so aggressive while you had BROKEN RIBS...")

    if duck_death:
        print("- As you try to walk through the final door, you hit your head hard on the top of it. So hard, in fact, that you die. -")
        print("Pro Tip: If only you had remembered all the commands...")

    if batter_death:
        print("-you get sucked into outer space and die a quick death-")
        print("Pro Tip: WHY WOULD YOU THROW IT AGAINST THE WINDOW, WHAT, WHY?!?!??!?!")

    # end game when not_finished == False!
    # this is the victory screen!
    if victory:
        print("You step outside The Dauntle.S.S, back onto the deck of your own docked-on shuttle.")
        print("Finally, the complete wind-stillness not in your hair... the freezing cold of outerspace on your skin...")
        print("Oh, how you've missed this!")
        print("You settle back into the comfort of your own shuttle, trying to ignore the itch in the back of your throat.")
        print("You're sure it's no real issue.")
