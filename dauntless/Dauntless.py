import os
import json
import time
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

    # Get the directory where main.py is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to rooms.json
    json_file_path = os.path.join(script_dir, 'rooms.json')

    # Load json content from rooms.json
    with open(json_file_path, 'r') as rooms_file:
        rooms = json.load(rooms_file)

    # Set starting room
    current_room = my_room_name.lower()

    return rooms, current_room


def sleep():
    time.sleep(60)

def ssprint(sentence):
    print("-" * 30)
    print(sentence)


def esprint(sentence):
    print(sentence)
    print("-" * 30)


def sprint(sentence):
    print("-" * 30)
    print(sentence)
    print("-" * 30)


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

    # ENDGAME VARIABLES
    charge_death = False
    batter_death = False
    wire_death = False
    ribs_death = False
    cook_death = False
    duck_death = False
    lever_death = False
    starlight_death = False
    bridge_death = False
    space_aids_death = False
    not_finished = True
    victory = False

    # INGAME VARIABLES
    usb_counter = 0

    # boiler room
    ladder_get = False
    gun_get = False
    battery_charged = False

    # engine
    usb_d_get = False

    # bridge/storage/hallway_b
    existential_dread = 0

    # crew_cabin
    diseased = False
    bob_dying = True
    usb_b_get = False

    # storage
    inspect_glint = False
    batteries_get = False
    usb_a_get = False

    # hallway_a/ storage
    broken_ribs = False

    # hallway_a/ bridge
    engine_open = False

    # engine room
    switch_a_on = False
    switch_b_on = False
    switch_c_on = False
    switch_d_on = False

    # bridge
    button_open = False
    captain_dead = False

    # captains cabin
    numpad_charged = False
    safe_open = False

    # hallway_c
    captain_open = False

    # hallway b
    zombie_killed = False

    # server_room
    medkit_taken = False

    # kitchen
    noise_gone = False
    mystery_meat_get = False
    engine_key_get = False

    # intro and guide for the player
    start = False
    print("What's your name, traveler?")
    user_name = input()
    print("Hello", user_name + """, welcome aboard The Dauntle.S.S
A large spaceship, drifting alone through outerspace.
In this game, you have 4 commands to interact with the world.
"Inspect, Use, Go and Duck." Remember them well.
"Inspect" is used to inspect any object that's CAPITALIZED.
"Use" is used to use items in your inventory.
"Go" can be used to move to rooms North, East, South or West of your current location
Finally, "Duck" can be used to, well... duck. You wouldn't wanna hit your head, right?
To use these commands type the command, then the object, item, or direction.
For example: "inspect CHEST", "go west" or "use HAMMER"
Bonus: use 'inspect inv' to check your inventory and use 'inspect map' to pull up a map""")

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
            print("""You find yourself in a dark room.
You had docked your significantly smaller ship against the Dauntle.S.S, a large, now seemingly abandoned, cruiseship.
You just came here to loot this wreckage- you hadn't expected it to still have power.
Because as soon as you set foot inside, the entrance door closed behind you...""")

            while current_room == "entrance":

                if usb_counter != 4:

                    print("The closed DOOR is to the north behind you,")

                if usb_counter == 4:

                    print("All the light bulbs surrounding the entrance DOOR have lit up...")
                print("all you see in front of you now, is a CORRIDOR.")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_corridor":
                    sprint("Before you looms a dark corridor... what awaits?")

                if action == "i_door":
                    sprint("The entrance door won't budge. You notice four light bulbs surrounding it.")

                    if usb_counter == 0:
                        sprint("All four bulbs are turned off.")

                    elif usb_counter == 1:
                        sprint("One of the four bulbs turned on! It's buzzing quietly.")
                    elif usb_counter == 2:
                        sprint("Two of the four bulbs have turned on. They're buzzing an adequate amount that's expected from 2 light bulbs.")
                    elif usb_counter == 3:
                        sprint("Three of the four bulbs have turned on. The electrical humming is getting a little loud for your liking.")
                    elif usb_counter == 4:
                        sprint("All four bulbs have turned on. The noise is deafening. Go forwards, EXIT!")

                if i[0] == "go":

                    if action == "exit" and usb_counter == 4:
                        ssprint("All four light bulbs flicker briefly. A loud rumbling shakes the ground as you watch the door slowly slide open.")
                        print("As if it's this horrible ship's last goodbye, the door gets stuck at the top of the frame.")
                        print("You're just a bit too tall to leave comfortably.")
                        esprint("Input your final command, and leave this place!")

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
                        sprint(f"The door is closed. {str(usb_counter)} out of four bulbs are lit up.")

                    elif action != "no passage":
                        setup_room(action)


# BOILER ROOM CODE - FINISHED

        if current_room == "boiler_room":

            print("You walk into the boiler room. It is really stuffy in here")
            print("You can already feel yourself sweating from the boilers heat.")

            while current_room == "boiler_room":

                print("")
                print("You squint your eyes trying to look around the room.")
                print("You spot a dark CORNER a beaten and broken CABINET, and some sparking WIRES")

                i = what_do()
                action = cmd.command(i[0],i[1])

                if action == "i_corner":
                    ssprint("You take a step closer to the dark corner. As your eyes adjust to the darkness,")
                    print("you bonk your ahead against some large OBJECT. For some reason you take up a fighting stance...")
                    esprint("As if you know how to fight," + user_name)

                if action == "i_cabinet":
                    ssprint("You pry open the cabinet with your hands. Great. Now you've got a cut on your hands, dumbass")
                    esprint("You got it open though. There is a TOOLKIT inside")

                if action == "i_wires":
                    if not battery_charged:
                        ssprint("You take a look at the sparking wires. You can smell burned rubber.")
                        esprint("Maybe you could charge something with the electricity outputted from these wires...")

                    elif battery_charged:
                        ssprint("Tempted by the sparks of the wires, you reach out your hand...")
                        esprint("Do you proceed?")
                        sparks_reach = input().split(" ")

                        if "yes" in sparks_reach:
                            sprint("You jam your hand in the electric current.")
                            not_finished = False
                            charge_death = True
                            current_room = ""

                        else:
                            sprint("You get back to your senses and quickly pull your hand back.")


                if action == "i_object":

                    if not ladder_get:
                        ssprint("You bonked your head against a comically large small step ladder.")
                        print("You think it might come in handy later so you put it in your pockets.")
                        esprint(":LADDER added to inventory:")
                        cmd.add_inv("ladder")
                        ladder_get = True

                    elif ladder_get:
                        ssprint("You already put the ladder in you pocket. Now that you think about it...")
                        esprint("How the hell did it fit in your pocket???")

                if action == "i_toolkit":

                    if not gun_get:
                        ssprint("While taking a closer look at the toolkit you notice that it has a bomb strapped to the side")
                        print("You pick it up, and you hear a timer go off! If only you had just let it be.")
                        print("You take a frantic look around the frame of the bomb, and you spot a red an blue wire.")
                        esprint("Which wire do you snap?!")
                        wire = ((input()).lower()).split(" ")

                        if "red" in wire:
                            ssprint("You somehow defused the bomb safely... who straps a bomb to a toolkit???")
                            print("You take a look inside the toolkit. There is an old timey gun inside. You know, the ones that don't use lasers.")
                            esprint("As you pick up the -what you think is a- Dessert Eagle, you suddenly feel the urge to 'make america great again.'")
                            cmd.add_inv("gun")
                            print(":GUN added to inventory:")
                            gun_get = True

                        else:
                            not_finished = False
                            current_room = ""
                            wire_death = True

                    elif gun_get:
                        sprint("You are still very confused as to why there was a bomb strapped to the toolkit.")

                if action == "u_empty_batteries":

                        sprint("You push the batteries into the wires, hoping not to die. To your surprise, it actually worked.")
                        print(":EMPTY_BATTERIES removed from inventory:")
                        print(":CHARGED_BATTERIES added to inventory:")
                        cmd.add_inv("charged_batteries")
                        cmd.remove_inv("empty_batteries")
                        battery_charged = True

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)


# HALLWAY A CODE - FINISHED

        if current_room == "hallway_a":

            print("")
            print("You step into a hallway. A sign reads: 'Hallway A'. The lights are flashing rapidly, probably due to a power shortage.")
            print("It's a good thing you're no epileptic, or you would have had an attack right about now.")

            while current_room == "hallway_a":

                if diseased:
                    sprint("As you stumble into the hallway, you feel your legs suddenly collapse. You hit the floor with a loud thud.")
                    space_aids_death = True
                    not_finished = False
                    current_room = ""

                print("")
                print("The hallway forks into two different doors. An EAST_DOOR and a WEST_DOOR")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_east_door":
                    ssprint("""The plate above reads "Engine Room" """)
                    esprint("You try and open the door, but it seems very stuck. Would you like to ram the door?")
                    ram = (input()).split(" ")
                    if "yes" in ram:
                        ssprint("YOU RAM YOUR ENTIRE BODY AGAINST THE DOOR")
                        esprint(user_name + ", you now have broken ribs... and the door is still closed")
                        broken_ribs = True

                if action == "i_west_door":
                    ssprint("""The plate above reads "Boiler Room" """)
                    esprint("Somehow the door has been lodged out of place, providing passage to the west room.")

                if i[0] == "go":

                    if action == "engine_room" and not engine_open:
                        ssprint("You try to enter the engine room but the door remains closed.")
                        esprint("Maybe you could find a key somewhere.")
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
                    ssprint("You take a close look at the motor. It seems a USB is jammed inside the frame!")
                    esprint("You try to take it out, but the system won't let you. Next to the USB you notice some SWITCHES.")

                if action == "i_note":
                    ssprint("The note reads:")
                    esprint("on, off, off, on")

                if action == "i_switches":
                    ssprint("You inspect the SWITCHES next to the MOTOR, it seems there are four in total:")
                    esprint("SWITCH_A, SWITCH_B, SWITCH_C and SWITCH_D")

                if action == "i_usb":

                    if switch_a_on and not switch_b_on and not switch_c_on and switch_d_on:

                        if not usb_d_get:
                            ssprint("After flicking the switches, the USB releases from it's compartment.")
                            print("You got one of four USB's on this ship.")
                            esprint(":USB_D added to inventory:")
                            cmd.add_inv("usb_d")
                            usb_d_get = True

                        elif usb_d_get:
                            sprint("You feel very smart for solving that puzzle... You're really not though.")

                    else:
                        ssprint("The USB is still firmly held in place.")
                        esprint("Maybe inspect the SWITCHES?")

                if action == "i_switch_a":
                    if switch_a_on:
                        ssprint("The switch is on")
                    else:
                        ssprint("The switch is off")
                    esprint("Would you like to flick the switch?")

                    switch_flick_a = input().split(" ")

                    if "yes" in switch_flick_a:
                        switch_a_on = not switch_a_on

                if action == "i_switch_b":

                    if switch_b_on:
                        ssprint("The switch is on")
                    else:
                        ssprint("The switch is off")
                    esprint("Would you like to flick the switch?")

                    switch_flick_b = input().split(" ")

                    if "yes" in switch_flick_b:
                        switch_b_on = not switch_b_on

                if action == "i_switch_c":

                    if switch_c_on:
                        ssprint("The switch is on")
                    else:
                        ssprint("The switch is off")
                    esprint("Would you like to flick the switch?")

                    switch_flick_c = input().split(" ")

                    if "yes" in switch_flick_c:
                        switch_c_on = not switch_c_on

                if action == "i_switch_d":

                    if switch_d_on:
                        ssprint("The switch is on")
                    else:
                        ssprint("The switch is off")
                    esprint("Would you like to flick the switch?")

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
                    ssprint("You peer out the window, you see the endless void of space before you.")
                    esprint("You are very glad that this window protects you from that void.")

                if action == "i_tags":
                    ssprint("You take a look at one of the tags. It seems they have mostly run out of batteries")
                    esprint("Maybe you could get BATTERIES from the tags somehow")

                if action == "i_batteries":
                    if not batteries_get:
                        ssprint("You notice that the batteries are stored behind a lil' hatch, much like a tv-remote, so you decide to get it out.")
                        print("How would you like to get the batteries out?")
                        print("")
                        print("Aggressively?")
                        esprint("Or carefully?")

                        batteries = (input()).split(" ")

                        if "aggressively" in batteries and broken_ribs:
                            ribs_death = True
                            not_finished = False
                            current_room = ""


                        elif "aggressively" in batteries:
                            sprint("You fucking batter-ram one of the tags against the WINDOW.")
                            batter_death = True
                            not_finished = False
                            current_room = ""

                        else:
                            sprint("you calmly remove the panel and take the batteries out, they seems uncharged")
                            print(":EMPTY_BATTERIES added inventory:")
                            cmd.add_inv("empty_batteries")
                            batteries_get = True

                    elif batteries_get:
                        ssprint("Although you did get the batteries, you still have the urge to yeet them against the window.")
                        esprint("You don't know why though...")

                if action == "u_ladder":
                    if not inspect_glint:

                        ssprint("You set the ladder down in the middle of the room and stand on it.")
                        print("You feel a little bit taller, you suppose.")
                        esprint("... you step off and repocket the ladder.")

                    else:
                        ssprint("You step on the ladder to reach the shiny object. With the added length you are able to reach the shelf.")
                        esprint("You've found 1 of the 4 USB's on the ship.")
                        print(":USB_A added to inventory:")
                        cmd.add_inv("usb_a")
                        usb_a_get = True
                        print(":LADDER removed from inventory:")
                        cmd.remove_inv("ladder")

                if action == "i_piss":
                    ssprint("It's a jar of piss, I am not quite sure what you expected")
                    esprint("While infatuated with the jar of piss however, you notice a GLINT on one of the top shelves.")

                if action == "i_glint":
                    if not usb_a_get:
                        ssprint("You try to reach the shiny item, but you're just too small. You tiny little person.")
                        esprint("Maybe you could use something to reach it?")
                        inspect_glint = True

                    elif usb_a_get:
                        sprint("You already got the shiny. You are still extremely small though. Gnome looking ass.")

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)


# KITCHEN CODE - FINISHED

        if current_room == "kitchen":

            print("")
            print("You... think this is a kitchen? It smells so bad in here, that you're suddenly thankful that you haven't eaten yet.")
            print("While trying to stomach the- uhm- intense... aroma... you look around.")

            while current_room == "kitchen":

                print("")
                print("It's a bit dingy, but you can see various COUNTERTOPS lined along the wall, a FRIDGE, a STOVE and a POT on top of it.")
                if not noise_gone:
                    print("you also hear some soft... wet... NOISE. You can just about make out a shape in the corner of the room.")
                else:
                    print("The CORPSE is laying motionless on the floor.")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_countertops":
                    sprint("You check all countertops thoroughly, but they don't seem to have anything of use to you.")

                if action == "i_fridge":
                    if not mystery_meat_get:
                        ssprint("You open the fridge. You're greeted with a dim flickering white light and a Very pungent smell.")
                        esprint("You obtained some MYSTERY_MEAT. You're suddenly reminded of your mother's home cooking.")
                        print(":MYSTERY_MEAT added to inventory:")
                        cmd.add_inv("mystery_meat")
                        mystery_meat_get = True

                    elif mystery_meat_get:
                        ssprint("You sniff the items in the fridge. You throw up, but swallow it all.")
                        esprint("... you disgust me.")

                if action == "i_stove":
                    ssprint("It's covered in soot. You try to turn it on, but it's a wasted effort.")
                    print("You watch as the stove sputters out a final spark, before it moves on to the great beyond.")
                    esprint("All you gained from this is dirty soot-covered fingers, and a death on your conscience.")

                if action == "i_pot":
                    ssprint("When you try to lift the lid off the pot, you struggle. The goo around the lid has caked it completely shut.")
                    print("Just as you get ready to put more effort into it, something inside the pot clangs against the metal.")
                    esprint("You decide you don't want to know what's inside this pot anymore.")

                if action == "u_mystery_meat":
                    sprint("You don't think you're desperate enough to eat this yet.")

                if action == "i_noise":
                    if not noise_gone:
                        ssprint("As you slowly approach the source of the noise, you start to be able to make out a shape.")
                        print("It is- it Was... the headchef. It seems he still has an affinity for good food though, as he's munching away on some poor fellow's corpse.")
                        esprint("Unfortunately for you, it's noticed you and is now lunging at you. I sure hope you've got a weapon to use.")
                        noise_gone = True

                        i = what_do()
                        action = cmd.command(i[0], i[1])

                        if action == "u_gun":
                            ssprint("With a quick draw, you shoot the chef down. You think, and hope, his meal is dead. Poor CORPSE, what a way to go.")
                            esprint("You feel america getting greater...")

                        elif action == "u_mystery_meat":
                            ssprint("In a panic, you throw the mushy slab of meat into the furthest corner away from you.")
                            print("The chef seems interested in this well-aged delicacy you've put in front of him and rushes to go eat it.")
                            esprint("It leaves the CORPSE it was eating alone.")
                            print(":MYSTERY_MEAT removed from inventory:")
                            cmd.remove_inv("mystery_meat")

                        else:
                            cook_death = True
                            not_finished = False
                            current_room = ""

                    elif noise_gone:
                        sprint("You are not brave enough to poke the zombie chef.")

                if action == "i_corpse":
                    if not engine_key_get:
                        ssprint("Yup, definitely dead. Luckily you've played a lot of Skyrim in your time, and you know how to rob a corpse.")
                        esprint("You found an ENGINE_KEY! You give it a good sniff for sniffing's sake.")
                        print(":ENGINE_KEY added to inventory:")
                        cmd.add_inv("engine_key")
                        engine_key_get = True

                    elif engine_key_get:
                        sprint("You take another look at the corpse, then you slap it a few times for good measure.")

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)

 # NAVIGATION ROOM CODE - FINISHED

        if current_room == "nav_room":

            print("You enter the Navigation Room.")

            while current_room == "nav_room":

                print("Before you stand a big table with a ship LOCALIZED_MAP on it")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_localized_map":
                    ssprint("It shows the location of several usb's spread throughout the ship.")
                    print("Usb_A is located in the Storage Room.")
                    print("Usb_B is located in the Crew Cabins")
                    print("Usb_C is located in the Captain Cabin")
                    esprint("Usb_D is located in the Engine Room")

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
                    ssprint("You search around in the junk for something useful. You are disgusting.")
                    esprint("You do find something however; 'Bob's LOCKBOX'. It seems to be locked with a 4 digit code.")

                if action == "i_bunk_beds":
                    ssprint("You gander at the bunk beds, you would like a nap right about now... The beds look disgusting, but also comfortable.")
                    esprint("Would you like to take a nap? yes or no.")

                    nap_time = input().split(" ")

                    if "yes" in nap_time:
                        ssprint("You lay down on one of the beds and take a quick 30 minute nap.")
                        print("This achieved relatively little, but you do feel refreshed.")
                        esprint("Also, you're pretty sure you got space aids, who knows who slept in that bed before you.")
                        refreshed = True
                        diseased = True

                    else:
                        sprint("You decide it's best to not risk space-aids for a little rest.")

                if action == "i_infection":
                    ssprint("You analyze the infectious patterns, on the floor. This way you can determine what your dealing with.")
                    print("Except you're not a biologist and have no fucking clue what you're looking at. Fyi, it's bad.")
                    esprint("You do notice a crew member in the corner of the room, barely breathing. His name tag reads: BOB")

                if action == "i_bob":

                    if bob_dying:
                        ssprint("You walk up to the injured crew member")
                        print("Bob: O-Oi, buddy, mate, my man. *cough* *cough * C-Could you help a friend out here? ")
                        print("Bob: I don't know who you are or how you got here, but please get me a medkit.")
                        esprint("Bob: If you do I'll give you the code to my lockbox. It's somewhere in the JUNK")
                    else:
                        ssprint("You take another look at Bob. He seems to be watching porn on his bed.")
                        esprint("You are not sure helping him was the right decision.")

                if action == "u_medkit":

                    ssprint("You give the medkit to Bob. He looks around in it for a while until he finds a bottle of alcohol.")
                    print("He downs the entire bottle in one go and, surprisingly enough, he actually gets up like he's all better.")
                    esprint("Bob: Thanks for the help buddy, as promised: The pincode to my lockbox is 0238.")
                    print(":MEDKIT removed from inventory:")
                    bob_dying = False
                    cmd.remove_inv("medkit")

                if action == "i_lockbox":
                    if not usb_b_get:
                        ssprint("You take a look at the pin code in the lockbox.")
                        print("Please enter a 4 digit code:")
                        code = input()

                        if code == "0238":
                            print("The lockbox opens. Inside you find a USB. You wonder if Bob stole it...")
                            esprint("You've found one of the four USB's on the ship.")
                            print(":USB_B added to inventory:")
                            cmd.add_inv("usb_b")
                            usb_b_get = True

                        else:
                            esprint("An error message pops up, you've entered the wrong code.")

                    elif usb_b_get:
                        sprint("Yeaaaaaah, no. he definitely stole that usb...")

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)

# HALLWAY B CODE - FINISHED

        if current_room == "hallway_b":
            print("You step into another hallway. A sign reads: 'Hallway B'. The windows in the hallway let a large amount of starlight through.")
            print("Its a good thing you're no albino, or you would've burned to death right now.")

            while current_room == "hallway_b":
                print("You take a look around the hallway. The passage is connected to a SOUTH_DOOR, a WEST_DOOR, and some STAIRS leading up north.")
                print("You peer out the WINDOW once more.")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_stairs":
                    ssprint("The plate above the door reads: 'Passengers Deck'")
                    print("The passage is completely soldered shut, you can see the infection seeping through some holes.")
                    esprint("You hear banging from behind the door. There is no way in hell you are ever going in there.")

                if action == "i_window":
                    ssprint("You try to decipher what star you are looking at. You are pretty sure this one is called Centurion 6B")
                    print("This hallway also seems to be strangely absent of any signs of infection, maybe the light of the star keeps it in check...")
                    esprint("As you face away from the window, you notice a BODY in the dark corner of the hallway.")

                if action == "i_body":

                    if not zombie_killed:
                        ssprint("The body juts upwards the second you look at it. And starts to shamble towards you.")
                        print("It starts burning in the starlight, but seems to care little and continues your way...")
                        print("You better do something about this! And quick!")

                        i = what_do()
                        action = cmd.command(i[0], i[1])

                        if action == "u_gun":
                            print("You shoot the shambling corpse clean through the skull.")
                            esprint("Your urge to make america great again grows stronger...")
                            zombie_killed = True

                        else:
                            print("As you fumble around looking for a solution to the walking corpse issue,")
                            esprint("You didn't realize it was already right in front of you.")

                            starlight_death = True
                            not_finished = False
                            current_room = ""

                    elif zombie_killed:
                        sprint("You slap the lifeless body. On the cheeks. They wiggle. You smile.")

                if action == "i_south_door":
                    sprint("The plate above the door reads:'Server Room'. The door seems too function just fine.")

                if action == "i_west_door":
                    sprint("The plate above the door reads:'Crew Cabins'. It seems the crew left the door unlocked.")

                if i[0] == "go":

                    if action == "stairs":
                        sprint("Nope, no, nu-uh, your are not setting one foot on that deck. Hell. No.")

                    elif action != "no passage":
                        setup_room(action)

# SERVER ROOM CODE - FINISHED

        if current_room == "server_room":
            print("You enter into a stuffy room. The air inside is crisp, it seems that at least the AC is functional.")

            while current_room == "server_room":
                print("You see rows and rows of flickering LIGHTS and LEVERS in front of you.")
                print("There are low lights buzzing around four different USB_PORTS. You also notice a darkened SCREEN hanging from the ceiling.")
                if not medkit_taken:
                    print("Hanging on the wall behind you, you notice a MEDKIT.")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_medkit":
                    if not medkit_taken:
                        ssprint("You found a MEDKIT! You sure hope you won't need to use it for yourself.")
                        esprint(":MEDKIT added to inventory:")
                        cmd.add_inv("medkit")
                        medkit_taken = True

                    else:
                        sprint("You take a look inside the medkit, it's mostly just bottles of vodka...")

                if action == "i_lights":
                    ssprint("The lights flicker in a constant pattern, it feels like you eaten some shrooms.")
                    print("""
                    Red
                    Yellow
                    Green
                    Blue
                    """)
                    esprint("But you are pretty sure the ones you ate yesterday have lost their potency by now")

                if action == "i_levers":
                    sprint("You flick the levers at random, and didn't notice one of them said self-destruct.")
                    lever_death = True
                    not_finished = False
                    current_room = ""

                if action == "i_screen":
                    sprint("The screen is completely black. You tap it, to try to get it to turn on. All you do is get fingerprints all over it.")

                if action == "i_usb_ports":
                    ssprint("The ports are individually labeled A, B, C and D. It seems they could be activated by a USB stick.")
                    esprint(f"Currently, you've activated {str(usb_counter)} ports.")
                    if usb_counter == 4:
                        esprint("That's all of them! Better go check on that door you entered from!")

                if action == "u_usb_a":
                    usb_counter += 1
                    ssprint("You put USB_A into the dedicated port, and twist it. You hear a low rumbling, as if an engine is starting.")
                    esprint("The screen turns on, to display a light flickering on next to the door in the first room you entered.")
                    print(":USB_A removed from inventory:")
                    cmd.remove_inv("usb_a")

                if action == "u_usb_b":
                    usb_counter += 1
                    ssprint("You put USB_B into the dedicated port, and twist it. You hear a low rumbling, as if an engine is starting.")
                    esprint("The screen turns on, to display a light flickering on next to the door in the first room you entered.")
                    print(":USB_B removed from inventory:")
                    cmd.remove_inv("usb_b")

                if action == "u_usb_c":
                    usb_counter += 1
                    ssprint("You put USB_C into the dedicated port, and twist it. You hear a low rumbling, as if an engine is starting.")
                    esprint("The screen turns on, to display a light flickering on next to the door in the first room you entered.")
                    print(":USB_C removed from inventory:")
                    cmd.remove_inv("usb_c")

                if action == "u_usb_d":
                    usb_counter += 1
                    ssprint("You put USB_D into the dedicated port, and twist it. You hear a low rumbling, as if an engine is starting.")
                    esprint("The screen turns on, to display a light flickering on next to the door in the first room you entered.")
                    print(":USB_D removed from inventory:")
                    cmd.remove_inv("usb_d")

                if action == "u_keycard":
                    ssprint("You swipe the keycard against the captains door. You hear a soft beep")
                    esprint("It seems you have opened the door...")
                    print(":KEYCARD removed from inventory:")
                    cmd.remove_inv("keycard")
                    captain_open = True

# if player input "go direction"
                if i[0] == "go":
# if outcome of input is captains cabin and the door is closed.
                    if action == "captain_cabin" and not captain_open:
                        sprint("The door to the captain cabin is shut, maybe you could find his keycard?")
# reset the location in the commands file
                        cmd.command("go", "east")

                    elif action != "no passage":
                        setup_room(action)

# HALLWAY C CODE - FINISHED

        if current_room == "hallway_c":
            print("You enter another hallway. The plate above the door read: 'Hallway C'.")
            print("I guess you are pretty deep in the ship now...")
            print("Good thing you aren't lactose intolerant... Not because you would've died or anything, just cause that would suck.")

            while current_room == "hallway_c":

                print("You are faced with three doors. An EAST_DOOR, a SOUTH_DOOR and a WEST_DOOR")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_east_door":
                    sprint("The plate above the door reads: 'Captains Cabin'. That is one hell of a fancy door.")

                if action == "i_south_door":
                    sprint("The plate above the door reads: 'Bridge'. The ship kind, not the car kind.")

                if action == "i_west_door":
                    sprint("The plate above the door reads: 'Navigation'. You like maps.")

                if action == "u_keycard":
                    ssprint("You swipe the keycard against the captains door, a green light flickers on.")
                    esprint("It seems you have opened the door...")
                    print(":KEYCARD removed from inventory:")
                    cmd.remove_inv("keycard")
                    captain_open = True

                if i[0] == "go":

                    if action == "captain_cabin" and not captain_open:
                        sprint("The door to the captain cabin is shut, maybe you could find his keycard?")
                        cmd.command("go", "west")

                    elif action != "no passage":
                        setup_room(action)

# CAPTAINS CABIN CODE - FINISHED ALMOST

        if current_room == "captain_cabin":

            print("You've entered the captain's cabin. Should you really be here?")

            while current_room == "captain_cabin":

                print("You see an open cabinet with a SAFE in it. The safe has a NUMPAD next to it. In the corner, there's a messy DESK.")

                i = what_do()
                action = cmd.command(i[0], i[1])

                # player inspect safe
                if action == "i_safe":

                    # if safe is closed (safe_open = False)
                    if not safe_open:
                        sprint("It's definitely locked. Next to it, there's a NUMPAD.")

                    # if safe is open
                    else:
                        sprint("You've successfully opened the safe, now why are you staring at it.")

                # player inspects numpad
                if action == "i_numpad":

                    # if batteries not used
                    if not numpad_charged:

                        ssprint("It's an old thing. It requires a four number code.")
                        print("Please input a 4 digit code:")
                        safe_code_empty = input()

                        print("You try to enter a code, but there's no response.")
                        print("You realize the battery hatch of the case is missing, and there are no batteries inside at all.")
                        esprint("Just your luck.")

                    # if batteries are used and safe is closed
                    elif numpad_charged and not safe_open:
                        ssprint("It seems using the batteries has indeed turned the numpad on.")
                        print("Please input a 4 digit code:")
                        safe_code = input()

                        if safe_code == "1693":
                            esprint("The light turns green and the safe swings open! Inside you find USB_C, and you see a note.")
                            print(":USB_C was added to your inventory:")
                            safe_open = True
                            cmd.add_inv("usb_c")

                        else:
                            esprint("The light turns red. It looks like the code is wrong. Try again maybe?")

                    # if safe is open
                    else:
                        sprint("You've already opened the safe. What else do you want from it?")

                # if player uses charged batteries to charge numpad
                if action == "u_charged_batteries":
                    sprint("You pop the batteries into the numpad, and see a white spot of light flicker on.")
                    print(":CHARGED_BATTERIES removed from inventory:")
                    numpad_charged = True
                    cmd.remove_inv("charged_batteries")

                # player inspects note
                if action == "i_note":
                    ssprint("It's a neatly folded paper note, lying next to the USB.")
                    print("You fold it open. It reads:")
                    print("Captain's log. 20-9-2269")
                    print("I decided it best to fully lock down the ship.")
                    print("The infection has gotten out of hand. Multiple guests and crew members are sick.")
                    print("I cannot risk the virus escaping.")
                    esprint("I'm sorry, everyone.")

                # when player inspects desk tell them about the documents
                if action == "i_desk":
                    ssprint("The desk is filled with piles upon piles of DOCUMENTS")
                    esprint("There's a painting of a beautiful meadow with a rainbow hung above the desk. How sweet.")

                # un-nested. Remember, we know there are documents. The player doesn't know until they inspect the desk
                # else the player would have to inspect the desk every single time they'd want to inspect the docs
                if action == "i_documents":
                    ssprint('Upon further inspection, you see the majority of these "documents" are pornography. You feel gross.')
                    print("But, you notice that the very few legit documents have different ink colors.")
                    print("The YELLOW inked document has page number 6")
                    print("The BLUE inked document has page number 3")
                    print("The GREEN inked document has page number 9")
                    esprint("The RED inked document has page number 1")

                if i[0] == "go":

                    if action != "no passage":
                        setup_room(action)

 # BRIDGE CODE - FINISHED

        if current_room == "bridge":
            print("Ahh, the bridge! The center of all control of this ship.")

            while current_room == "bridge":
                if not captain_dead:
                    print("You're immediately greeted by a massive WINDOW. You're standing on the DOORMAT, and see the CAPTAIN sleeping lazily in his chair.")
                    print("There's an encased BUTTON on the dashboard.")
                elif captain_dead:
                    print("""You're immediately greeted by a massive WINDOW. You're standing on the DOORMAT, and see the CAPTAIN "...sleeping" lazily in his chair.""")
                    print("There's an encased BUTTON on the dashboard. A sign reads 'No shooting in the bridge!'")

                i = what_do()
                action = cmd.command(i[0], i[1])

                if action == "i_captain":
                    if not captain_dead:
                        ssprint("You poke the captain lightly. He doesn't react. You tilt his cap up from over his eyes, and realize the captain is very, very dead.")
                        print("You quickly put the cap back over his eyes, out of respect for the dead.")
                        print("Then, out of disrespect for the dead, you empty his pockets.")
                        esprint("Inside, you find the captains cabin KEYCARD!")
                        print(":KEYCARD added to inventory:")
                        cmd.add_inv("keycard")
                        captain_dead = True

                    elif captain_dead:
                        sprint("You want to disrespect the dead even more, so you give the captain a good slap.")

                if action == "i_doormat":
                    sprint("Getting sick of these dumb puzzles, you decide to check the doormat for a key. No luck, bummer.")

                if action == "i_button":

                    # check if button is open
                    if not button_open:
                        ssprint("It's a big red button veiled in a cubic clear plastic case, with a keyhole right underneath it.")
                        esprint('The label above it reads "engine".')

                    # change engine room to open if button is open and engine room is closed
                    elif button_open and not engine_open:
                        ssprint("With a long history of being unable to ignore big red buttons, you hit the big red button.")
                        esprint("The engine room has now opened")
                        engine_open = True

                    # insult the player if engine room already open
                    else:
                        sprint("You have already pressed this button and opened the engine room. Stop HITTING THE BUTTON")

                if action == "u_engine_key":

                    # update button to open after player uses engine key
                    sprint("As you twist the key, the clear case around the button flips open. Before you lies the BUTTON, ready to press.")
                    print(":ENGINE_KEY removed from inventory:")
                    button_open = True
                    cmd.remove_inv("engine_key")

                if action == "i_window":
                    ssprint("You look out of the large window. A million stars greet you. It's gorgeous out there.")
                    print("You suddenly feel significantly smaller than you did a second ago. Do your problems even matter?")
                    print("What is your purpose? Is it fate that you're stuck on this hellish ship?")
                    esprint("You have obtained an existential crisis!")
                    existential_dread += 1

                if action == "u_gun":
                    sprint("You shoot inside the bridge despite the explicit warning saying 'No shooting in the bridge!'")

                    bridge_death = True
                    not_finished = False
                    current_room = ""

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)

# END IN-LOOP SCRIPT

# end game when not_finished == False.
# these are the death screens:
    if wire_death:
        print("- You horrifically exploded into a million itty bitty parts -")
        print("Pro Tip: You should have chosen the red wire, you absolute buffoon.")
        sleep()

    if cook_death:
        print("- You are torn to shreds by the chef, who is happy to have found his next meal. -")
        print("Pro Tip: If only you had some kind of weapon, or a way to distract it...")
        sleep()

    if ribs_death:
        print("- Your ribs give in and collapse, you feel them puncture all your organs. -")
        print("Pro Tip: Maybe if you weren't so aggressive while you had BROKEN RIBS...")
        sleep()

    if duck_death:
        print("- As you try to walk through the final door, you hit your head hard on the top of it. So hard, in fact, that you're decapitated -")
        print("Pro Tip: If only you had remembered all the commands...")
        sleep()

    if batter_death:
        print("-you get sucked into outer space and die a quick death-")
        print("Pro Tip: WHY WOULD YOU THROW IT AGAINST THE WINDOW, WHAT, WHY?!?!??!?!")
        sleep()

    if lever_death:
        print("-you died, taking the whole ship with you-")
        print("Pro Tip: Never touch futuristic levers if you don't know what they do.")
        sleep()

    if starlight_death:
        print("-As the corpse catches fire from the starlight it give you a nice hug. You burn to death-")
        print("Pro Tip: It's a constitutional right to carry a gun, and actually makes america a lot safer.")
        sleep()

    if bridge_death:
        print("-Your shot ricochets around the room and hits you clean between the eyes-")
        print("Pro Tip: 'NO     SHOOTING      IN      THE      BRIDGE.' Idiot.")
        sleep()

    if space_aids_death:
        print("-All your motor functions fail, and you die drooling on the floor-")
        print("Pro Tip: It seems the space aids you got from sleeping in that bed was really dangerous...")
        sleep()

    if charge_death:
        print("-You feel the electricity running through your body, your dead.-")
        print("Pro Tip: Maybe don't do that next time, what the fuck is wrong with you.")
        sleep()
    # end game when not_finished == False!
    # this is the victory screen!
    if victory:
        print("You step outside The Dauntle.S.S, back onto the deck of your own docked-on ship.")
        print("Finally, the complete wind-stillness not in your hair... the freezing cold of outerspace on your skin...")
        print("Oh, how you've missed this!")
        print("You settle back into the comfort of your own ship, trying to ignore the itch in the back of your throat.")
        print("You're sure it's nothing.")
        sleep()