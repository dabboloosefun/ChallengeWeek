import json


def dialog_trigger(who_is_talking, dialog_name, dialog_step):
    steps = ""
    action_doable = False

    with open('dialog.json') as f:
        dialogs = json.load(f)

    # Find dialog by name
    for dialog in dialogs['dialogs']:
        if dialog['name'] == dialog_name:
            steps = dialog['steps']
            break

    # If we say player instead of user it will now work as well
    if who_is_talking.lower() == "player":
        who_is_talking = "user"

    # Check if response is defined
    if who_is_talking in steps[dialog_step] and steps[dialog_step][who_is_talking]:
        action_doable = True

    # Print first step user utterance
    if action_doable:
        print(who_is_talking.capitalize() + ": " + steps[dialog_step][who_is_talking])

    return action_doable


def dialog_check(who_is_talking, dialog_name, dialog_step):
    action_doable = False

    with open('dialog.json') as f:
        dialogs = json.load(f)

    # Find dialog by name
    for dialog in dialogs['dialogs']:
        if dialog['name'] == dialog_name:
            steps = dialog['steps']
            break

    # Check if response is defined
    if who_is_talking in steps[dialog_step] and steps[dialog_step][who_is_talking]:
        action_doable = True

    return action_doable