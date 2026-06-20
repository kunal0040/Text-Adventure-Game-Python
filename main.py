import time
import world_map


def loading():
    for i in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)


print("=" * 29)
print("-----------WELCOME-----------")
print("=" * 29)
time.sleep(0.8)

player_name = input("\nEnter your name: ").strip()
if not player_name:
    player_name = "Rookie"

time.sleep(0.5)
input("\nPress ENTER to begin...")
time.sleep(0.5)
loading()

print(f"\n\nWelcome to the force, Detective {player_name}.")
print("The city is bleeding rain, and a fresh body just dropped...")
time.sleep(1)

current_room = "police_station"
inventory = []
game_flags = {
    "bar_state": "bar_neutral",
    "path_a_unlocked": False,
    "path_b_unlocked": False,
}


def printroom_details(room_name):
    room_data = world_map.rooms[room_name]

    first_line = room_data["description"].split("\n")[0]
    line_length = len(first_line)

    time.sleep(0.5)
    print("\n" + "=" * line_length)
    print(room_data["description"])
    print("=" * line_length)
    time.sleep(0.5)

    if room_data["items"]:
        pretty_items = [item.replace("_", " ").title() for item in room_data["items"]]
        print(f"\n📦 Items you see here: {', '.join(pretty_items)}")

    if room_data["characters"]:
        print("\n👥 People present:")
        for char_id in room_data["characters"]:
            char = world_map.characters[char_id]
            print(f" - {char['name']}")
    time.sleep(1)


def pickup_items(item_name):
    room_data = world_map.rooms[current_room]

    if item_name in room_data["items"]:
        room_data["items"].remove(item_name)
        inventory.append(item_name)
        print(f"\n You picked up the {item_name.upper()}.")
    elif item_name == "items" or item_name == "item":
        print("\nWhat exactly do you want to take?")
    else:
        print(f"\n There is no '{item_name}' here to take.")


printroom_details(current_room)

print(f"\n[MISSION LOG]: You are standing in the middle of the chaotic bullpen.")
print(f"Captain Morrison is glaring at you from his desk, waving a smoking cigarette.")
print(f"You need to step up and speak to him.\n(Type: talk captain)")

briefing_complete = False
while current_room == "police_station":

    user_choice = input("\nWhat is your move?\ntalk|take|go|inventory\n->").strip()

    if not user_choice:
        print("\nPlease enter a command.")
        continue

    input_parts = user_choice.split(maxsplit=1)
    verb = input_parts[0].lower()
    target = input_parts[1].strip() if len(input_parts) > 1 else ""
    clean_target = target.replace(" ", "_").lower()

    if verb == "talk":
        if not target:
            print("\nWho exactly do you want to talk to?\n(e.g., 'talk captain')->")
        elif clean_target in {"captain_morrison", "captain"}:
            speaker_name = world_map.characters["captain_morrison"]["name"]
            raw_text = world_map.rooms["police_station"]["dialogue"]["captain_morrison"]

            text_part = raw_text.split("\n\n")
            action_text = text_part[0]
            spoken_text = text_part[1]
            clean_dialogue = spoken_text.replace('"', "")

            print(f"\n{action_text}")
            time.sleep(0.8)

            print(f"\n{speaker_name} > ", end="")
            print(clean_dialogue.format(player_name=player_name))
            briefing_complete = True
            time.sleep(0.4)

            print(
                f"\n[STRATEGY]: The Captain gave you your clearance. Look around and gather your items."
            )
            print(f"Commands unlocked: take [item], inventory, go north")
        else:
            print("\nThat person isn't here or you misspelled their name.")

    elif not briefing_complete:
        print(
            f"\nMorrison shouts across the room: 'Hey! Rookie! Get over to my desk before you touch anything!'"
        )
        print("(Try typing: talk captain morrison or talk captain)")

    elif verb == "take":
        if clean_target in ["item", "items"]:
            print("\nWhat exactly do you want to take?")
        elif clean_target:
            pickup_items(clean_target)
        elif target == "items" or target == "item":
            print("\nWhat exactly do you want to take?")

    elif verb == "inventory" or verb == "inv":
        preety_inv = [item.replace("_", " ").title() for item in inventory]
        print(f"\nYou have: {preety_inv if preety_inv else '[Empty]'}")

    elif verb == "go":
        if clean_target != "north":
            print("\nYou can't go that way from here.")
        elif (
            "badge" in inventory and "wallet" in inventory and "case_file" in inventory
        ):
            current_room = "crime_scene"
            print(
                "\nYou walk out into the pouring rain and head towards Harlow Mansion..."
            )
            time.sleep(1.5)
        else:
            print(
                f"\nMorrison barks: 'Where do you think you're going without your gear, {player_name}!!? Grab your BADGE, WALLET, and CASE FILE! You Rookie!!!'"
            )

    else:
        print(
            "\nUnknown command. Try using keywords like 'take', 'inventory', or 'go'."
        )

