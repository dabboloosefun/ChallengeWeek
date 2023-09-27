import json
import commands as c


# Add item to library
c.add_inv("key")


def setup_room(my_room_name):
    with open('rooms.json') as f:
        rooms = json.load(f)

    # Set starting room
    current_room = my_room_name.lower()

    # Print current room description
    print(rooms[current_room]['description'])

    return rooms, current_room


def room(rooms, current_room):
    stop_loop = False

    i = input("What do you want to do?").split(" ")

    if len(i) < 2:
        print("You didn't specify an action")
        stop_loop = False
        return stop_loop
    else:
        # Call GO c.command
        action = c.command(i[0], i[1])

        commands = ["go", "use", "inspect", "talk", "duck"]
        if i[0].lower() in commands:
            if action[0:2] == "u_":
                if action == "u_key":
                    print("You unlocked the chest")

            elif action[0:2] == "i_":
                if action == "i_chest":
                    print("You take a closer look at the chest in the room, there seems to be a heavy lock on it")
                if action == "i_key":
                    print("You find a key which is somewhat heavy")
                    c.add_inv("key")
                    c.command("inspect", "inv")

            elif action in ["west", "east", "north", "south"]:
                direction = action
                print(direction)

                if direction not in rooms[current_room]['exits']:
                    print("There is no exit here. Maybe use your compass?")

                if direction in rooms[current_room]['exits']:
                    current_room = rooms[current_room]['exits'][direction]
                    print(rooms[current_room]['description'])
                    stop_loop = True

        else:
            print("What the fuck are you doing?!")


        # if i[0].lower() == "go":
        #     go = c.command("go", i[1])
        #     if go == ("N" or "E" or "S" or "W"):
        #         current_room = rooms[current_room]['exits']['north']
        #         print(rooms[current_room]['description'])
        #         stop_loop = True
        #
        # # Call INSPECT c.command on chest
        # if i[0].lower() == "inspect":
        #     inspect = c.command("inspect", i[1])
        #     print("INSPECT: " + str(inspect))
        #
        #     if inspect == "room":
        #         print(rooms[current_room]['inspect_description'])
        #
        #     if inspect == "exit" or inspect == "exits":
        #         d = rooms[current_room]['exits']
        #         print("You see exits on the following sides:")
        #         print(', '.join(d.keys()))
        #
        # # Call USE c.command on key
        # if i[0].lower() == "use":
        #     use = c.command("use", i[1])
        #     print("USE: " + str(use))
        #
        #     if use == "chest":
        #         print("Unlocked chest.")
        #         print(use)
        #
        # # Call TALK c.command
        # if i[0].lower() == "talk":
        #     talk = c.command("talk", i[1])
        #     print("TALK: " + str(talk))
        #
        #     if i[0].lower() == "talk" and talk is True:
        #         print("Dialog with Bob")

        print("\n")
        return stop_loop

stop_loop_ = False
room_json, room_name = setup_room("Dungeon")

while True:
    stop_loop_ = room(room_json, room_name)

# current_room = any_room >
# if current_room == desired_room >
# run room code > if go(direction) >
# update current_room