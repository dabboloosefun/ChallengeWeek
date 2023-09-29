import json
import commands as c

"""
Setup/load a new room.
Usage: room_json, room_name = setup_room("ROOM_NAME")
Returns: tuple (the whole json and the room name)
Prints: room description from json 
"""


def setup_room(my_room_name):
    global current_room
    # Load json content from rooms.json
    with open('../dauntless/rooms.json') as f:
        rooms = json.load(f)

    # Set starting room
    current_room = my_room_name.lower()

    return rooms, current_room


def what_do():
    correct_format = "no"
    while correct_format == "no":
        print("Input command:")
        i = input().split(" ")

        if len(i) > 3 or len(i) < 2 or i[0] not in ["use", "go", "inspect", "talk"]:
            print("You didn't specify an action, and remember to use the command format")
        else:
            correct_format = "yes"

    return i


if __name__ == "__main__":

    current_room = "start"
    # Give win condition a name and True value
    not_finished = True

    while not_finished:

        if current_room == "start":

            print("You find yourself in the starting room")
            # Getting an input from the player
            while current_room == "start":
                print("Room contains: CHEST in the corner and a DOOR that seems to lead outside.")
                i = what_do()
                action = c.command(i[0], i[1])

                if action == "i_chest":
                    print("The seems CHEST to be locked, the LOCK has a blue tint.")

                if action == "u_blue_key":
                    print("you opened the chest, inside is a letter with the code 7839. It reads 'for the door!'")

                if action == "i_door":
                    print("the DOOR has a PINCODE lock, there seem to be four numbers required.")

                if action == "i_pincode":
                    print("Please input a 4-digit code:")
                    pincode = input()
                    if pincode == "7839":
                        not_finished = False
                        current_room = ""
                    else:
                        print("Ha ha ha wrong code dumb ass.")

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)

        elif current_room == "hallway":
            print("You move to a long and cold hallway, it's freezing, as if the VENTS are at -20 degrees.")
            # Getting an input from the player
            while current_room == "hallway":
                print("Room contains: VENTS")

                i = what_do()
                action = c.command(i[0], i[1])

                if action == "i_vents":
                    print("you take a closer look at the vents. It looks like there is a blue key lodged inside")
                    print("maybe you could take the vent of with a screwdriver?")
                if action == "u_screwdriver":
                    print("you opened the vent and got the BLUE_KEY")
                    c.add_inv("blue_key")

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)

        elif current_room == "dungeon":

            print("you find yourself in a dark and desolate dungeon. You can barely breath.")

            while current_room == "dungeon":
                print("Room contains: a single dimly lit CELL ")
                # Getting an input from the player
                i = what_do()
                action = c.command(i[0], i[1])

                if action == "i_cell":
                    print("you stumble into the cell and stub you toe against a SHARP_OBJECT")

                if action == "i_sharp_object":
                    print("you pick up the object: its a screwdriver, that really fucking hurt though.")
                    c.add_inv("screwdriver")

                if i[0] == "go":
                    if action != "no passage":
                        setup_room(action)

    print("You step outside the locked door. It seems your finally freed from the test_rooms.")
    print("VICTORY")
