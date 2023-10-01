import os
import json
import dialog_trigger as dialog

# Get the directory where main.py is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to rooms.json
json_file_path = os.path.join(script_dir, 'rooms.json')

with open(json_file_path, 'r') as rooms_file:
    rooms = json.load(rooms_file)




current_room = "entrance"



# Debugging True or False
DEBUG_MODE = False

# Create our inventory
inv = list()

map = """
████████████████┼───┼███████████████N███
████████████████│   │█████████████W ┼ E█
████████████████│   │███████████████S███
████████████████┼───┼███████████████████
████┼──────┼██████║██████┼───────┼██████
████│      │█┼─────────┼█│       │██████
████│      │═│    A    │═│       │██████
████│      │█┼─────────┼█│       │██─███
████┼──────┼█████████████┼───────┼██─███
█████████║██████████████████████████─███
█┼───┼█┼───┼██┼────────────┼████████║███
█│   │█│   │██│            │█┼───────┼██
█│   │═│   │══│            │═│   B   │██
█│   │█│   │██│            │█┼─────┼ │██
█┼───┼█┼───┼██┼────────────┼███████│ │██
█████████║█████████████████████████│ │██
███████┼───┼███████████┼───┼█┼───┼█│ │██
███████│   │█┼───────┼█│   │█│   │█│ │██
███████│   │═│   C   │═│   │═│   │═│ │██
███████│   │█┼──┼ ┼──┼█│   │█│   │█┼─┼██
███████┼───┼████│ │████┼───┼█┼───┼██████
████████████████┼─┼█████████████████████
█████████████████║██████████████████████
████████████┼─────────┼█████████████████
████████████│         │█████████████████
████████████│         │█████████████████
████████████┼─────────┼█████████████████"""


if DEBUG_MODE:
    inv.append("wrench")

# Create a method so we can execute 'commands'


def command(cmd_arg, action_arg):
    action_doable = False

    global current_room
    # Lower the command and action
    cmd_arg = cmd_arg.lower()
    action_arg = action_arg.lower()

    # check for go command
    if cmd_arg == "go":
        # variables for possible directions and direction output (interchangeable between rooms)
        next_room = "no passage"
        # check if the direction is possible and give them individual output for ease of use
        if action_arg in ["west", "east", "north", "south"]:
            direction = action_arg

            if current_room == "entrance" and direction == "north":
                next_room = "exit"

            elif current_room == "hallway_b" and direction == "north":
                next_room = "stairs"

            elif direction not in (rooms[current_room]['exits']):
                print("You hit your head against the wall. It seems there is no exit here... maybe try a different direction?")

            else:
                next_room = (rooms[current_room]['exits'][direction])
                current_room = next_room

        elif action_arg not in ["west", "east", "north", "south"]:
            print("Use the wind directions to choose your next location")
        return next_room
        # extra print in case the user does not input a wind direction

    # If we are going to use an item
    if cmd_arg == "use":
        # Check if we have the item

        if action_arg in inv:
            # Print that we are using the item
            print("Using item: " + action_arg)
            # Remove the item from our inventory
            if action_arg in (rooms[current_room]["items"]):
                # Make us able to return the item we just used
                action_doable = "u_" + action_arg

            else:
                print(action_arg + " Is not usable in this room.")
        # If we don't have the item we are trying to use
        else:
            # Print that we don't have the item
            print("You don't have a(n) " + action_arg + " in your inventory")
            action_doable = "not_in_inv"
        return action_doable

    # check for the inspect command
    if cmd_arg == "inspect":

        if action_arg == "inv" or action_arg == "inventory":
            print(inv)

        elif action_arg == "map":
            print(map)

        elif action_arg.lower() in (rooms[current_room]["interact"]):
            action_doable = "i_" + action_arg

        else:
            print("There is nothing like that in this room.")

        return action_doable

    # If we want to talk
    if cmd_arg == "talk":
        if dialog.dialog_check(action_arg, "greeting", 0):
            action_doable = True
            dialog.dialog_trigger("user", "greeting", 0)
            dialog.dialog_trigger(action_arg, "greeting", 0)
        return action_doable

    return action_doable


def add_inv(item):
    inv.append(item)
def remove_inv(item):
    inv.remove(item)

if __name__ == '__main__':
    # Return room_name or "no passage"
    # Set "cmd_arg" as "go" and "action_arg" as the direction you want to walk in.
    go = command("go", "north")
    print("GO: " + go)

    # Return item used or prints not in inv
    # Set "cmd_arg" as "use" and "action_arg" as the item you want to use.
    use = command("use", "wrench")
    print("USE: " + str(use))

    # Return item which is inspected
    # Set "cmd_arg" as "inspect" and "action_arg" as the item you want to inspect.
    inspect = command("inspect", "chest")
    print("INSPECT: " + str(inspect))

    inspect = command("inspect", "inv")
    print("INSPECT: " + str(inspect))

    # Return True or False
    # Set "cmd_arg" as "talk" and "action_arg" as the person you want to talk to.
    talk = command("talk", "bob")
    print("TALK: " + str(talk))

