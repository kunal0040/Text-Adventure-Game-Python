import time
import world_map

def loading():
    for i in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)

print("=" * 29)
print("-----------WELCOME-----------")
print("=" * 29)

player_name = input("\nEnter your name: ").strip()
if not player_name:
    player_name = "Rookie"

current_room = "police_station"
inventory = []
game_flags = {} 

def printroom_details(room_name):
    room_data = world_map.rooms[room_name]
    first_line = room_data["description"].split("\n")[0]
    line_length = max(len(first_line), 30)

    print("\n" + "=" * line_length)
    print(room_data["description"])
    print("=" * line_length)

    if room_data.get("items"):
        pretty_items = [item.replace("_", " ").title() for item in room_data["items"]]
        print(f"📦 Items you see here: {', '.join(pretty_items)}")

    if room_data.get("characters"):
        print("\n👥 People present:")
        for char_id in room_data["characters"]:
            print(f" - {world_map.characters[char_id]['name']}")


def pickup_items(clean_target):
    room_data = world_map.rooms[current_room]
    actual_item = clean_target.replace('_', ' ').upper()
    
    if clean_target in room_data.get("items", []):
        room_data["items"].remove(clean_target)
        inventory.append(clean_target)
        print(f"\nYou picked up the {actual_item}.")
        
        n = input(f"Do you want to inspect the {actual_item}? >")
        if n == "inspect":
            pass

    elif clean_target in ["items", "item", ""]:
        print("\nWhat exactly do you want to take?")
    else:
        print(f"\nThere is no '{clean_target.replace('_', ' ')}' here to take.")


def talk_to_character(clean_target):
    global game_flags
    room_data = world_map.rooms[current_room]

    matched_char_id = None
    for char_id in room_data.get("characters", []):
        if clean_target in char_id or clean_target in world_map.characters[char_id]["name"].lower():
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
        print(f"\n{action_text}")
        time.sleep(0.5)
    else:
        spoken_text = raw_text

    print(f"\n{speaker_name} > {spoken_text.format(player_name=player_name).replace('\"', '')}")
    
    flag_to_trigger = dialogue_node.get("trigger_flag")
    if flag_to_trigger:
        game_flags[flag_to_trigger] = True


def move_room(direction):
    global current_room
    room_data = world_map.rooms[current_room]
    exits = room_data.get("exits", {})

    if direction in exits:
        exit_data = exits[direction]

        req_flags = exit_data.get("required_flags", [])
        for flag in req_flags:
            if not game_flags.get(flag):
                print(f"\n[LOCKED] You cannot go that way yet.")
                return

        req_items = exit_data.get("required_items", [])
        if not all(item in inventory for item in req_items):
            custom_msg = exit_data.get("lock_message", "You don't have the required items to go there.")
            print(f"\n{custom_msg}")
            return

        current_room = exit_data["destination"]
        print(f"\nMoving toward the {current_room.replace('_', ' ').title()}...")
        loading()
        printroom_details(current_room)
    else:
        print("\nYou can't go that way from here.")


printroom_details(current_room)

while True:
    user_choice = input("\nWhat is your move?\n(talk, take, go, inventory)\n-> ").strip()
    if not user_choice:
        continue

    input_parts = user_choice.split(maxsplit=1)
    verb = input_parts[0].lower()
    target = input_parts[1].strip() if len(input_parts) > 1 else ""
    clean_target = target.replace(" ", "_").lower()

    if verb == "talk":
        talk_to_character(clean_target)

    elif verb == "take":
        pickup_items(clean_target)

    elif verb in ["inventory", "inv"]:
        pretty_inv = [item.replace("_", " ").title() for item in inventory]
        print(f"\nYou have: {pretty_inv if pretty_inv else '[Empty]'}")

    elif verb == "go":
        if not clean_target:
            print("\nGo where? Specify a direction (e.g., 'go north').")
        else:
            move_room(clean_target)

    elif verb in ["quit", "exit"]:
        break

    else:
        print("\nUnknown command.")