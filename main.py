import time
import sys
import world_map

def loading():
    for i in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)


def slow_print(text, delay):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


slow_print("=" * 29, 0.01)
slow_print("-----------WELCOME-----------", 0.02)
slow_print("=" * 29, 0.01)

player_name = input("\nEnter your name: ").strip()
if not player_name:
    player_name = "Rookie"

time.sleep(0.5)
input("\nPress ENTER to begin...")
time.sleep(0.5)
loading()

slow_print(f"\n\nWelcome to the force, Detective {player_name}.", 0.02)
slow_print("The city is bleeding rain, and a fresh body just dropped...", 0.02)
time.sleep(1)


current_room = "police_station"
inventory = []
visited_rooms = set()
game_flags = {"briefing_complete": False}


def show_help():
    room_data = world_map.rooms[current_room]
    actions = room_data.get("actions", {})

    slow_print("\n" + "=" * 75, 0.01)
    print("DETECTIVE HANDBOOK & CORE CORE SYSTEM CONTROLS")
    slow_print("═" * 75, 0.01)
    print("  go [direction]        -> Move between areas (e.g., 'go north')")
    print("  talk [person]         -> Interrogate a suspect or witness")
    print("  take [item]           -> Pick up a clue from the floor")
    print("  inspect [clue]        -> Closely examine room clues or inventory items")
    print("  investigate [action]  -> Execute a special story action / scenario choice")
    print("  inventory / inv       -> Open your trench coat to check your pockets")
    print("  help / ??             -> Open this handbook guide")
    print("  quit / exit           -> Abandon the active case file")

    if actions:
        print("\n CURRENT ROOM ACTION KEYS:")
        pretty_actions = [act.upper() for act in actions.keys()]
        print(
            f" >You can type: investigate [action] (or just type the action directly!)"
        )
        print(f" >Valid keys here: {', '.join(pretty_actions)}")
    slow_print("\n" + "=" * 75, 0.01)


def get_command():
    user_choice = input(
        "\nWhat is your move?\n(talk, take, inspect ,investigate, go, inventory or help)\n-> "
    ).strip()

    if not user_choice:
        return None

    input_parts = user_choice.split(maxsplit=1)
    verb = input_parts[0].lower()
    target = input_parts[1] if len(input_parts) > 1 else ""

    clean_target = target.strip().replace(" ", "_").lower()

    return {"verb": verb, "target": target, "clean_target": clean_target}


def printroom_details(room_name):
    room_data = world_map.rooms[room_name]
    first_line = room_data["description"].split("\n")[0]
    line_length = max(len(first_line), 30)

    if room_name in visited_rooms:
        description = room_data["short_desc"]
    else:
        description = room_data["description"]
        visited_rooms.add(room_name)


    slow_print("\n" + "=" * line_length, 0.03)
    slow_print(description, 0.03)
    slow_print("=" * line_length, 0.03)

    if room_data.get("items"):
        pretty_items = [item.replace("_", " ").title() for item in room_data["items"]]
        slow_print(f"📦 Items you see here: {', '.join(pretty_items)}", 0.02)

    if room_data.get("characters"):
        slow_print("\n👥 People present:", 0.02)
        for char_id in room_data["characters"]:
            slow_print(f" - {world_map.characters[char_id]['name']}", 0.02)

    if room_data.get("actions"):
        slow_print(f"\nInvestigation Action Available:", 0.02)
        for action_id in room_data["actions"]:
            clean_action_print = action_id.replace("_", " ").upper()
            slow_print(f" - {clean_action_print}", 0.02)

    if room_data.get("exits"):
        pretty_exits = [direction.upper() for direction in room_data["exits"].keys()]
        slow_print(f"\n🧭 Available directions to move: {', '.join(pretty_exits)}", 0.02)


def inspect_item(item_name):
    room_data = world_map.rooms[current_room]

    if item_name in room_data.get("examine", {}):
        slow_print("\n" + room_data["examine"][item_name], 0.01)
        return

    if item_name in inventory:
        for room in world_map.rooms.values():
            if item_name in room.get("examine", {}):
                slow_print("\n" + room["examine"][item_name], 0.01)
                return
    time.sleep(0.4)
    loading()
    print(f"\nThere is no info about '{item_name.replace('_', ' ').title()}'.")


def pickup_items(clean_target):
    room_data = world_map.rooms[current_room]
    actual_item = clean_target.replace("_", " ").upper()

    if clean_target in room_data.get("items", []):
        room_data["items"].remove(clean_target)
        if clean_target not in inventory:
            inventory.append(clean_target)
            slow_print(f"\nYou picked up the {actual_item}.", 0.02)

        while True:
            n = input(f"Do you want to inspect the {actual_item}? >").lower()
            if n in {"inspect", "yes", "y"}:
                inspect_item(clean_target)
                break
            elif n in {"no", "n"}:
                print(f"\nYou slip the {actual_item} safely away into your pockets.")
                break
            else:
                print("\nEnter 'inspect' to inspect the item or 'no' deny!")

    elif clean_target in ["items", "item", ""]:
        print("\nWhat exactly do you want to take?")
    else:
        print(f"\nThere is no '{clean_target.replace('_', ' ')}' here to take.")


def show_inventory():

    print("\n=========EVIDENCE & ITEMS=========")

    if not inventory:
        print("No items collected.")
        print("\n==================================")
        return

    for index, item in enumerate(inventory, start=1):
        pretty_item = item.replace("_", " ").title()
        print(f" {index}. {pretty_item}")
    print("\n==================================")


def execute_investigation(action_name):
    global current_room, game_flags
    room_data = world_map.rooms[current_room]
    actions = room_data.get("actions", {})

    if action_name in actions:
        action_node = actions[action_name]
        slow_print("\n" + action_node["text"], 0.02)

        flag_to_trigger = action_node.get("trigger_flag")
        if flag_to_trigger:
            game_flags[flag_to_trigger] = True

        new_state_room = action_node.get("change_room_state")
        if new_state_room:
            current_room = new_state_room
            time.sleep(0.5)
            printroom_details(current_room)
            return

        spawn_item = action_node.get("spawn_item")
        if spawn_item:
            if spawn_item not in room_data.get("items", []):
                room_data["items"].append(spawn_item)

                clue_name = spawn_item.replace("_", " ").upper()
                slow_print(f"\nClue uncovered: [{clue_name}]!", 0.03)
                time.sleep(0.4)
                pickup_items(spawn_item)
    else:
        print(f"\nYou can't use the investigate approach here!")


def talk_to_character(clean_target):
    global game_flags
    room_data = world_map.rooms[current_room]

    if clean_target in room_data.get("actions", {}):
        execute_investigation(clean_target)
        return

    matched_char_id = None
    for char_id in room_data.get("characters", []):
        char_name_lower = world_map.characters[char_id]["name"].lower()
        if (
            clean_target in char_id.lower()
            or clean_target in char_name_lower
            or char_id.lower() in clean_target
        ):
            matched_char_id = char_id
            break

    if not matched_char_id:
        print("\nThat person isn't here or you misspelled their name.")
        return

    speaker_name = world_map.characters[matched_char_id]["name"]
    dialogue_node = room_data["dialogue"][matched_char_id]
    raw_text = dialogue_node["text"]

    if "\n\n" in raw_text:
        action_text, spoken_text = raw_text.split("\n\n", 1)
        slow_print(f"\n{action_text}", 0.01)
        time.sleep(0.5)
        game_flags["briefing_complete"] = True
    else:
        spoken_text = raw_text

    slow_print(
        f"\n{speaker_name} » {spoken_text.format(player_name=player_name).replace('\"', '')}",
        0.02
    )

    flag_to_trigger = dialogue_node.get("trigger_flag")
    if flag_to_trigger:
        game_flags[flag_to_trigger] = True

    if game_flags.get("ready_for_judgment") or (
        current_room == "police_station" and "hidden_ledger" in inventory
    ):
        evaluate_final_endings()


def move_room(target_location):
    global current_room
    room_data = world_map.rooms[current_room]
    exits = room_data.get("exits", {})

    if target_location in visited_rooms:
        if target_location == current_room:
            print(f"\nYou are already standing inside the {target_location.replace('_', ' ').title()}")
            return
        
        current_room = target_location
        print(f"\nGoing to {current_room.replace('_', ' ').title()}...")
        loading()
        time.sleep(0.6)
        printroom_details(current_room)
        return

    if target_location in exits:
        exit_data = exits[target_location]

        req_flags = exit_data.get("required_flags", [])
        for flag in req_flags:
            if not game_flags.get(flag):
                print(f"\n[LOCKED] You cannot go that way yet.")
                return

        req_items = exit_data.get("required_items", [])
        if not all(item in inventory for item in req_items):
            custom_msg = exit_data.get(
                "lock_message", "You don't have the required items to go there."
            )
            print(f"\n{custom_msg}")
            return

        current_room = exit_data["destination"]
        print(f"\nMoving toward the {current_room.replace('_', ' ').title()}...")
        loading()
        time.sleep(0.4)
        printroom_details(current_room)
    else:
        print("\nYou can't go that way from here.")


def evaluate_final_endings():

    if current_room == "police_station" and "hidden_ledger" in inventory:
        end_node = world_map.endings["secret_ending"]

    elif "poison_report" in inventory and "threatening_letter" in inventory:
        end_node = world_map.endings["true_ending"]

    else:
        end_node = world_map.endings["bad_ending"]

    title = end_node["title"]
    length = len(title)

    time.sleep(1)
    print("\n\n")
    for i in range(length):
        time.sleep(0.03)
        print("=", end="", flush=True)

    slow_print(f"\n{title}", 0.04)
    slow_print("=" * length, 0.02)
    slow_print(f"\n{end_node['text']}", 0.03)
    slow_print(f"\n[CASE ARCHIVED]: Goodbye! Detective {player_name}.\n", 0.05)

    for i in range(length):
        time.sleep(0.05)
        print("=", end="", flush=True)
    sys.exit()


printroom_details(current_room)

while True:

    if current_room == "police_station" and "hidden_ledger" in inventory:
        slow_print(
            f"\nALERT Detective {player_name}! You have returned to the Precinct with the HIDDEN LEDGER.",
            0.01,
        )
        slow_print("Type: 'talk captain' to confront Morrison with the file!", 0.01)

    command = get_command()
    if command is None:
        continue

    verb = command["verb"]
    clean_target = command["clean_target"]
    current_room_actions = world_map.rooms[current_room].get("actions", {})
    current_room_exit = world_map.rooms[current_room].get("exits", {})

    if verb == "help":
        show_help()

    elif verb == "talk":
        talk_to_character(clean_target)

    elif verb == "take":
        if game_flags.get("briefing_complete") == True:
            pickup_items(clean_target)
        else:
            print(f"\nYou should investigate more to take the item!!")

    elif verb in {"inspect", "examine", "look"}:
        if not clean_target:
            print("\nWhat do you want to inspect?")
        else:
            inspect_item(clean_target)

    elif verb in ["inventory", "inv"]:
        show_inventory()

    elif verb in {"investigate", "actions", "show", "use"}:

        combined_action = f"{verb}_{clean_target}" if clean_target else verb
        if clean_target in current_room_actions:
            execute_investigation(clean_target)
        elif combined_action in current_room_actions:
            execute_investigation(combined_action)
        else:
            execute_investigation(clean_target)

    elif verb in current_room_actions:
        execute_investigation(verb)

    elif verb == "go":
        if not clean_target:
            print("\nGo where? Specify a direction or covered room.")
        else:
            move_room(clean_target)
    elif verb in current_room_exit:
        move_room(verb)

    elif verb in {"exit", "quit"}:
        time.sleep(1)
        loading()
        slow_print("Exiting the game!!", 0.02)
        sys.exit()

    else:
        print("\nUnknown command.")
