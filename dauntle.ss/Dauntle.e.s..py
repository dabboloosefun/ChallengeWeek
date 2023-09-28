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
        i = (input().lower()).split(" ")

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
    lever_death = False
    not_finished = True
    victory = False

# establishing in game variables
    usb_counter = 0
    # crew_cabin
    refreshed = False
    diseased = False
    bob_dying = True
    # hallway_a/ storage
    broken_ribs = False
    # hallway_a/ bridge
    engine_open = False
    # engine room
    switch_a_on = False
    switch_b_on = False
    switch_c_on = False
    switch_d_on = False
    #bridge
    button_open = False
    #captains cabin
    numpad_charged = False
    safe_open = False
    #hallway_c
    captain_open = False

# intro and guide for the player
    start = False
    print("What's your name, traveler?")
    user_name = input()
    print("Hello", user_name, ", welcome aboard The Dauntle.SS")
    print("In this game, you have 4 commands to interact with the world.")
    print('"Inspect, Use, Go and Duck." Remember them well.')
    print(""""Inspect" is used to inspect any object that's CAPITALIZED.""")
    print(""""Use" is used to use items in your inventory.""")
    print(""""Go" can be used to move to rooms North, East, South or West of your current location""")
    print("""Finally, "Duck" can be used to, well... duck. You wouldn't wanna hit your head, right?""")
    print("To use these commands type the command, then the object, item, or direction.")
    print("""For example: "inspect chest", "go west" or "use hammer" """)
    print("Bonus: use 'inspect inv' to check your inventory and use 'inspect map' to pull up a map")
    while not start:
        print("Type 'yes' if you understand and want to start the game")

        understand = input()
        if understand == "yes":
            print("Off you go, good luck!")
            print("")
            print("----game start----")

            current_room = "entrance"
            start = True

        if understand == "no":
            print("Tough luck. I'm sure you'll figure it out.")
            print("")
            print("----game start----")

            current_room = "entrance"
            start = True

# start game loop when not_finished = True
    while not_finished:

        # ENTRANCE CODE - FINISHED

        if current_room == "entrance":

            print("")
            print("You find yourself in a dark room.")
            print("You had docked your significantly smaller ship against the Dauntle.S.S, a large, now seemingly abandoned, cruiseship.")
            print("You just came here to loot this wreckage- you hadn't expected it to still have power.")
            print("Because as soon as you set foot inside, the entrance door closed behind you...")

            while current_room == "entrance":

                print("")
                print("The closed DOOR is to the north behind you, but all you see in front of you now, is a CORRIDOR.")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_corridor":
                    print("Before you looms the dark corridor... what awaits?")

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

                if action == "u_empty_batteries":
                    print("You push the batteries into the wires, hoping not to die. To your surprise, it actually worked.")
                    print(":EMPTY_BATTERIES removed from inventory:")
                    print(":CHARGED_BATTERIES added to inventory:")
                    cmd.add_inv("charged_batteries")
                    cmd.remove_inv("empty_batteries")

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)


# HALLWAY A CODE - FINISHED

        if current_room == "hallway_a":

            print("")
            print("You step into a hallway. A sign reads: 'Hallway A'. The lights are flashing, a lot, probably due to a power shortage.")
            print("It's a good thing you're no epileptic, or you would have had an attack right about now.")

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

                    if action == "engine_room" and not engine_open:
                        print("You try to enter the engine room but the door remains closed.")
                        print("Maybe you could find a key somewhere.")
                        cmd.command("go","west")

                    elif action != "no passage":
                        setup_room(action)


# ENGINE ROOM CODE - FINISHED

        if current_room == "engine_room":
            print("You step into the engine room, you can hear the hyperdrive of the ship humming and buzzing.")

            while current_room == "engine_room":
                print("Looking around the room, you can see the massive MOTOR that drives the ship forward.")
                print("You also notice a desk with a NOTE on it.")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_motor":
                    print("You take a close look at the motor. It seems a USB is jammed inside the frame!")
                    print("You try to take it out, but the system won't let you. Next to the USB you notice some SWITCHES.")

                if action == "i_note":
                    print("The note reads:")
                    print("on, off, off, on")

                if action == "i_switches":
                    print("You inspect the SWITCHES next to the MOTOR, it seems there are four in total:")
                    print("SWITCH_A, SWITCH_B, SWITCH_C and SWITCH_D")

                if action == "i_usb":

                    if switch_a_on and not switch_b_on and not switch_c_on and switch_d_on:
                        print("After flicking the switches, the USB releases from it's compartment.")
                        print("You got one of four USB's on this ship.")
                        print(":USB_D added to inventory:")
                        cmd.add_inv("usb_d")

                    else:
                        print("The USB is still firmly held in place.")
                        print("Maybe inspect the SWITCHES?")

                if action == "i_switch_a":
                    if switch_a_on:
                        print("The switch is on")
                    else:
                        print("The switch is off")
                    print("Would you like to flick the switch?")

                    switch_flick_a = input().split(" ")

                    if "yes" in switch_flick_a:
                        switch_a_on = not switch_a_on

                if action == "i_switch_b":

                    if switch_b_on:
                        print("The switch is on")
                    else:
                        print("The switch is off")
                    print("Would you like to flick the switch?")

                    switch_flick_b = input().split(" ")

                    if "yes" in switch_flick_b:
                        switch_b_on = not switch_b_on

                if action == "i_switch_c":

                    if switch_c_on:
                        print("The switch is on")
                    else:
                        print("The switch is off")
                    print("Would you like to flick the switch?")

                    switch_flick_c = input().split(" ")

                    if "yes" in switch_flick_c:
                        switch_c_on = not switch_c_on

                if action == "i_switch_d":

                    if switch_d_on:
                        print("The switch is on")
                    else:
                        print("The switch is off")
                    print("Would you like to flick the switch?")

                    switch_flick_d = input().split(" ")

                    if "yes" in switch_flick_d:
                        switch_d_on = not switch_d_on

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)


# STORAGE ROOM CODE - FINISHED

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

                if action == "i_window":
                    print("You peer out the window, you see the endless void of space before you.")
                    print("You are very glad that this window protects you from that void.")

                if action == "i_tags":
                    print("You take a look at one of the tags. It seems they have mostly run out of batteries")
                    print("Maybe you could get BATTERIES from the tags somehow")

                if action == "i_batteries":
                    print("You notice that the batteries are stored behind a lil' hatch, much like a tv-remote, so you decide to get it out.")
                    print("How would you like to get the batteries out?")
                    print("")
                    print("Aggressively?")
                    print("Or carefully?")
                    print("")

                    batteries_get = (input()).split(" ")

                    if "aggressively" in batteries_get and broken_ribs:
                        ribs_death = True
                        not_finished = False
                        current_room = ""


                    elif "aggressively" in batteries_get:
                        print("You fucking batter-ram one of the tags against the WINDOW.")
                        batter_death = True
                        not_finished = False
                        current_room = ""


                    else:
                        print("you calmly remove the panel and take the batteries out, they seems uncharged")
                        print(":EMPTY_BATTERIES added inventory:")
                        cmd.add_inv("empty_batteries")

                if action == "i_piss":
                    print("It's a jar of piss, I am not quite sure what you expected")
                    print("While infatuated with the jar of piss however, you notice a GLINT on one of the top shelfs.")

                if action == "i_glint":
                    print("You try to reach the shiny thing, but you just too small")
                    print("Maybe you could use something to reach it?")

                if action == "u_ladder":
                    print("You step on the ladder to reach the shiny object. With the added step you are able to reach.")
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
                print("It's a bit dingy, but you can see various COUNTERTOPS lined along the wall, a FRIDGE, a STOVE and a POT on top of it.")
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
                        print(":MYSTERY_MEAT removed from inventory:")
                        cmd.remove_inv("mystery_meat")

                    else:
                        cook_death = True
                        not_finished = False
                        current_room = ""


                if action == "i_corpse":
                    print("Yup, definitely dead. Luckily you've played a lot of Skyrim in your time, and you know how to rob a corpse.")
                    print("You found an ENGINE_KEY!")
                    print(":ENGINE_KEY added to inventory:")
                    cmd.add_inv("engine_key")


                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)

 # NAVIGATION ROOM CODE - FINISHED

        if current_room == "nav_room":

            print("You enter the Navigation Room.")

            while current_room == "nav_room":

                print("Before you stand a big table with a ship MAP on it")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_map":
                    print("It shows the location of several usb's spread throughout the ship.")
                    print("Usb_A is located in the Storage Room.")
                    print("Usb_B is located in the Crew Cabins")
                    print("Usb_C is located in the Captain Cabin")
                    print("Usb_D is located in the Engine Room")

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)

# CREW CABIN CODE - FINISHED

        if current_room == "crew_cabin":

            print("You enter the crew cabin in hope to find someone. As you enter, you feel the ground turning mushy beneath you feet.")
            print("It seems to crew was long gone before you got here, for some type of infection has nested in this room.")

            while current_room == "crew_cabin":

                print("You take another look around. You see some BUNK_BEDS, a great deal of JUNK on the floor, and the INFECTION")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_junk":
                    print("You search around in the junk for something useful. You are disgusting.")
                    print("You do find something however; 'Bob's LOCKBOX'. It seems to be locked with a 4 digit code.")

                if action == "i_bunk_beds":
                    print("You gander at the bunk beds, you too would like a nap around now. The beds look disgusting, but also comfortable.")
                    print("Would you like to take a nap? yes or no.")

                    nap_time = input().split(" ")

                    if "yes" in nap_time:
                        print("You lay down on one of the beds and take a quick 30 minute nap.")
                        print("This achieved relatively little, but you do feel refreshed.")
                        print("Also you might have some space disease now, who knows who slept in that bed before you.")
                        refreshed = True
                        diseased = True

                    else:
                        print("You decide it's best to not risk space-aids for a little rest.")

                if action == "i_infection":
                    print("You analyze the infectious patterns, on the floor. This way you can determine what your dealing with.")
                    print("Except your not a biologist and have no fucking clue what you're looking at. Fyi, it's bad.")
                    print("You do notice a crew member in the corner of the room, barely breathing. His name tag reads: BOB")

                if action == "i_bob":

                    if bob_dying:
                        print("You walk up to the injured crew member")
                        print("Bob: O-Oi, buddy, mate, my man. *cough* *cough * C-Could you help a friend out here? ")
                        print("Bob: I don't know who you are or how you got here, but please get me a medkit.")
                        print("Bob: If you do I'll give you the code to my lockbox. It's somewhere in the JUNK")
                    else:
                        print("You take another look at Bob. He seems to watching porn on his bed.")
                        print("You are not sure helping him was the right decision.")

                if action == "u_medkit":

                    print("You give the medkit to Bob. He looks around in it for a while until he finds a bottle of alcohol.")
                    print("He downs the entire bottle in one go, surprisingly enough, he actually gets up like he's all better.")
                    print("Bob: Thanks for the help buddy, as promised: The pincode to my lockbox is 0238.")
                    print(":MEDKIT removed from inventory:")
                    bob_dying = False
                    cmd.remove_inv("medkit")

                if action == "i_lockbox":
                    print("You take a look at the pin code in the lockbox.")
                    print("Please enter a 4 digit code:")
                    code = input()

                    if code == "0238":
                        print("The lockbox opens. Inside you find another USB. You wonder if Bob stole it...")
                        print("You've found one of the four USB's on the ship.")
                        print(":USB_B added to inventory:")
                        cmd.add_inv("usb_b")

                    else:
                        print("An error message pops up, you've entered the wrong code.")

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)

# HALLWAY B CODE - FINISHED

        if current_room == "hallway_b":
            print("You step into another hallway. A sign reads: 'Hallway B'. The windows in the hallway let a large amount of starlight through.")
            print("Its a good thing you're no albino, or you would've burned to death right now.")

            while current_room == "hallway_b":
                print("You take a look around the hallway. The passage is connected to a SOUTH_DOOR and a WEST_DOOR. You peer out the WINDOW once more.")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_window":
                    print("You try to decipher what star you are looking at. You are pretty sure this one is called Centurion 6B")
                    print("This hallway also seems to be strangely absent of any signs of infection, maybe the light of the star keeps it in check...")

                if action == "i_south_door":
                    print("The plate above the door reads:'Server Room'. The door seems too function just fine.")

                if action == "i_west_door":
                    print("The plate above the door reads:'Crew Cabins'. It seems the crew left the door unlocked.")

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)

# SERVER ROOM CODE - FINISHED

        if current_room == "server_room":
            print("You enter into a stuffy room. The air inside is crisp, it seems that at least the AC is functional.")

            while current_room == "server_room":
                print("You see rows and rows of flickering LIGHTS and LEVERS in front of you. There are low lights buzzing around four different USB_PORTS. You also notice a darkened SCREEN hanging from the ceiling.")
                print("Hanging on the wall behind you, you notice a MEDKIT.")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_medkit":
                    print("You found a MEDKIT! You sure hope you won't need to use it for yourself.")
                    print(":MEDKIT added to inventory:")
                    cmd.add_inv("medkit")

                if action == "i_lights":
                    print("The lights flicker in a constant pattern, it feels like you eaten some shrooms.")
                    print("""
                    Red
                    Yellow
                    Green
                    Blue""")
                    print("But you are pretty sure the ones you ate yesterday have lost their potency by now")


                if action == "i_levers":
                    print("You flick the levers at random, and didn't notice one of them said self-destruct.")
                    lever_death = True
                    not_finished = False
                    current_room = ""

                if action == "i_screen":
                    print("The screen is completely black. You tap it, to try to get it to turn on. All you do is get fingerprints all over it.")

                if action == "i_usb_ports":
                    print("The ports are individually labeled A, B, C and D. It seems they could be activated by a USB stick.")
                    print("Currently, you've activated", usb_counter, "ports.")
                    if usb_counter == 4:
                        print("That's all of them! Better go check on that door you entered from!")

                if action == "u_usb_a":
                    usb_counter += 1
                    print("You put USB_A into the dedicated port, and twist it. You hear a low rumbling, as if an engine is starting.")
                    print("The screen turns on, to display a light flickering on next to the door in the first room you entered.")
                    print(":USB_A removed from inventory:")
                    cmd.remove_inv("usb_a")

                if action == "u_usb_b":
                    usb_counter += 1
                    print("You put USB_B into the dedicated port, and twist it. You hear a low rumbling, as if an engine is starting.")
                    print("The screen turns on, to display a light flickering on next to the door in the first room you entered.")
                    print(":USB_B removed from inventory:")
                    cmd.remove_inv("usb_b")

                if action == "u_usb_c":
                    usb_counter += 1
                    print("You put USB_C into the dedicated port, and twist it. You hear a low rumbling, as if an engine is starting.")
                    print("The screen turns on, to display a light flickering on next to the door in the first room you entered.")
                    print(":USB_C removed from inventory:")
                    cmd.remove_inv("usb_c")

                if action == "u_usb_d":
                    usb_counter += 1
                    print("You put USB_D into the dedicated port, and twist it. You hear a low rumbling, as if an engine is starting.")
                    print("The screen turns on, to display a light flickering on next to the door in the first room you entered.")
                    print(":USB_D removed from inventory:")
                    cmd.remove_inv("usb_d")

                if action == "u_keycard":
                    print("You slide the captains card along the door. You hear a soft beep.")
                    print("It seems the door has been opened.")
                    print(":KEYCARD removed from inventory:")
                    cmd.remove_inv("keycard")
                    captain_open = True

                if i[0] == "go":

                    if action == "captain_cabin" and not captain_open:
                        print("The door to the captain cabin is shut, maybe you could find his keycard?")
                        cmd.command("go", "east")

                    if action != "no passage":
                        setup_room(action)

# HALLWAY C CODE - FINISHED

        if current_room == "hallway_c":
            print("You enter another hallway. The plate above the door read: 'Hallway C'.")
            print("I guess you are pretty deep in the ship now...")
            print("Good thing you aren't lactose intolerant... Not because you would've died or anything, just cause that would suck.")

            while current_room == "hallway_c":

                print("You are faced with three doors. An EAST_DOOR, a SOUTH DOOR and a WEST_DOOR")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_east_door":
                    print("The plate above the door reads: 'Captains Cabin'")

                if action == "i_south_door":
                    print("The plate above the door reads: 'Bridge'")

                if action == "i_west_door":
                    print("The plate above the door reads: 'Navigation'")

                if action == "u_keycard":
                    print("You swipe the keycard against the captains door, a green light flickers on.")
                    print("It seems you have opened the door...")
                    print(":KEYCARD removed from inventory:")
                    cmd.remove_inv("keycard")
                    captain_open = True

                if i[0] == "go":

                    if action == "captain_cabin" and not captain_open:
                        print("The door to the captain cabin is shut, maybe you could find his keycard?")
                        cmd.command("go", "west")

                    elif action != "no passage":
                        setup_room(action)

# CAPTAINS CABIN CODE - FINISHED ALMOST

        if current_room == "captain_cabin":

            print("entered captains cabin")

            while current_room == "captain_cabin":

                print("SAFE, DESK (hidden: NOTE, DOCUMENTS, NUMPAD)")

                i = what_do()
                action = cmd.command(i[0], i[1])

                # player inspect safe
                if action == "i_safe":

                    # if safe is closed (safe_open = False)
                    if not safe_open:
                        print("It's definitely locked. Next to it, there's a NUMPAD.")

                    # if safe is open
                    else:
                        print("You've successfully opened the safe, now why are you staring at it.")

                # player inspects numpad
                if action == "i_numpad":

                    # if batteries not used
                    if not numpad_charged:

                        print("It's an old thing. It requires a four number code.")
                        print("Please input a 4 digit code:")
                        safe_code_empty = input()

                        print("You try to enter a code, but there's no response.")
                        print("You realize the battery hatch of the case is missing, and there are no batteries inside at all.")
                        print("Just your luck.")

                    # if batteries are used and safe is closed
                    elif numpad_charged and not safe_open:
                        print("It seems using the batteries has indeed turned the numpad on.")
                        print("Please input a 4 digit code:")
                        safe_code = input()

                        if safe_code == "1693":
                            print("The light turns green and the safe swings open! Inside you find USB_C, and you see a note.")
                            print(":USB_C was added to your inventory:")
                            safe_open = True
                            cmd.add_inv("usb_c")

                        else:
                            print("The light turns red. It looks like the code is wrong. Try again maybe?")

                    # if safe is open
                    else:
                        print("You've already opened the safe. What else do you want from it?")

                # if player uses charged batteries to charge numpad
                if action == "u_charged_batteries":
                    print("You pop the batteries into the numpad, and see a white spot of light flicker on.")
                    print(":CHARGED_BATTERIES removed from inventory:")
                    numpad_charged = True
                    cmd.remove_inv("charged_batteries")

                # player inspects note
                if action == "i_note":
                    print("It's a neatly folded paper note, lying next to the USB.")
                    print("You fold it open. It reads:")

                # when player inspects desk tell them about the documents
                if action == "i_desk":
                    print("The desk is filled with piles upon piles of DOCUMENTS")

                # un-nested. Remember, we know there are documents. The player doesn't know until they inspect the desk
                # else the player would have to inspect the desk every single time they'd want to inspect the docs
                if action == "i_documents":
                    print('Upon further inspection, you see the majority of these "documents" are pornography. You feel gross.')
                    print("But, you notice that the very few legit documents have different ink colors.")
                    print("The yellow inked document has page number 6")
                    print("The blue inked document has page number 3")
                    print("The green inked document has page number 9")
                    print("The red inked document has page number 1")

                if i[0] == "go":

                    if action != "no passage":
                        setup_room(action)

 # BRIDGE CODE - FINISHED

        if current_room == "bridge":
            print("Ahh, the bridge! The center of all control of this ship.")

            while current_room == "bridge":
                print("You're immediately greeted by a massive WINDOW. You're standing on the DOORMAT, and see the CAPTAIN sleeping lazily in his chair.")
                print("There's a BUTTON on the dashboard.")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_captain":
                    print("You poke the captain lightly. He doesn't react. You tilt his cap up from over his eyes, and realize the captain is very, very dead.")
                    print("You quickly put the cap back over his eyes, out of respect for the dead.")
                    print("Then, out of disrespect for the dead, you empty his pockets.")
                    print("Inside, you find the captains cabin KEYCARD!")
                    print(":KEYCARD added to inventory:")
                    cmd.add_inv("keycard")

                if action == "i_doormat":
                    print("Getting sick of these dumb puzzles, you decide to check the doormat for a key. No luck, bummer.")

                if action == "i_button":

                    # check if button is open
                    if not button_open:
                        print("It's a big red button veiled in a cubic clear plastic case, with a keyhole right underneath it.")
                        print('The label above it reads "engine".')

                    # change engine room to open if button is open and engine room is closed
                    elif button_open and not engine_open:
                        print("With a long history of being unable to ignore big red buttons, you hit the big red button.")
                        print("The engine room has now opened")
                        engine_open = True

                    # insult the player if engine room already open
                    else:
                        print("You have already pressed this button and opened the engine room. Stop HITTING THE BUTTON")

                if action == "u_engine_key":

                    # update button to open after player uses engine key
                    print("As you twist the key, the clear case around the button flips open. Before you lies the BUTTON, ready to press.")
                    print(":ENGINE_KEY removed from inventory:")
                    button_open = True
                    cmd.remove_inv("engine_key")

                if action == "i_window":
                    print("You look out of the large window. A million stars greet you. It's gorgeous out there.")
                    print("You suddenly feel significantly smaller than you did a second ago. Do your problems even matter?")
                    print("What is your purpose? Is it fate that you're stuck on this hellish ship?")
                    print("You have obtained an existential crisis!")

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)

# END IN-LOOP SCRIPT

# end game when not_finished == False.
# these are the death screens:
    if wire_death:
        print("- You horrifically exploded into a million itty bitty parts -")
        print("Pro Tip: You should have chosen the red wire, you absolute buffoon.")

    if cook_death:
        print("- You are torn to shreds by the chef, who is happy to have found his next meal. -")
        print("Pro Tip: If only you had some kind of weapon, or a way to distract it...")

    if ribs_death:
        print("- Your ribs give in and collapse, you feel them puncture all your organs. -")
        print("Pro Tip: Maybe if you weren't so aggressive while you had BROKEN RIBS...")

    if duck_death:
        print("- As you try to walk through the final door, you hit your head hard on the top of it. So hard, in fact, that you die. -")
        print("Pro Tip: If only you had remembered all the commands...")

    if batter_death:
        print("-you get sucked into outer space and die a quick death-")
        print("Pro Tip: WHY WOULD YOU THROW IT AGAINST THE WINDOW, WHAT, WHY?!?!??!?!")

    if lever_death:
        print("-you died, taking the whole ship with you-")
        print("Pro Tip: Never touch futuristic levers if you don't know what they do.")
    # end game when not_finished == False!
    # this is the victory screen!
    if victory:
        print("You step outside The Dauntle.S.S, back onto the deck of your own docked-on ship.")
        print("Finally, the complete wind-stillness not in your hair... the freezing cold of outerspace on your skin...")
        print("Oh, how you've missed this!")
        print("You settle back into the comfort of your own ship, trying to ignore the itch in the back of your throat.")
        print("You're sure it's nothing.")
