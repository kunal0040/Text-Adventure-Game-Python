# 🕵️‍♂️ Midnight in the Neon Rain: A Text-Adventure Mystery

A gritty, noir-lite text adventure game built in Python. Take on the role of a rookie detective assigned to your very first solo homicide case on a rain-swept night where nothing is as it seems.

---

## 📖 The Case File

* **Victim:** Victor Harlow (Ruthless billionaire tycoon)
* **Time of Death:** Approximately Midnight
* **Location:** The locked study of Harlow Manor
* **Initial Ruling:** Natural causes / Sudden heart failure

Because a massive storm has trapped the veteran detectives across town, the precinct has no choice but to send you. The medical examiners are ready to write it off as a tragic heart attack, but your gut tells you otherwise. The door was locked from the inside, the family is acting strange, and the shadows of this city hold deep secrets.

You have until dawn to explore the manor, hit the pavement, gather evidence, and uncover the truth. Drop the ball, and a killer walks free. Dig too deep, and you might just find a rotten core bigger than the murder itself...

---

## 🛠️ Engine Architecture & Features

* **Data-Driven Architecture:** Built using a completely modular structural dictionary system (`world_map.py`), cleanly decoupling story nodes from the main game engine (`main.py`) for seamless, endless scalability.
* **Atmospheric Pacing Engine:** Powered by custom text animation loops (`slow_print` and `loading`) that mimic retro detective computer terminals, preventing text dumping and drawing you deeper into the noir narrative.
* **Hybrid Fast Travel System:** Tracks explored rooms in the `visited_rooms` set. After visiting a room, you can return directly by typing `go [room_name]`.
* **Fast Travel Behavior:** Shortcuts check required story flags on the destination room's exits, but currently do not check required items. This means fast travel can bypass item-gated exits. Traveling by direction checks both flags and items.
* **Modular Multi-State Progression:** Special room action hooks completely morph environmental scenes, spawning hidden elements on the fly or shifting characters from cooperative to hostile based entirely on your approach.

---

## 🎮 How to Play & Case Controls

The parser engine dynamically filters your typed inputs into executable core verbs and lowercase target arguments:

| Action | Command Syntax | Example | Description |
| :--- | :--- | :--- | :--- |
| **Move & Navigation** | `go [direction]` | `go north` | Walk between adjacent areas manually. |
| **Instant Shortcut Warp** | `go [room_name]` | `go police_station` | Fast travel directly to any area you have previously uncovered. |
| **Interrogation** | `talk [suspect/witness]` | `talk mrs_chen` | Grill people in the current room. Character matching accepts partial names. |
| **Evidence Gathering** | `take [item]` | `take poison_vial` | Secure an item from the current room and add it to your inventory. |
| **Forensic Inspection** | `inspect [item]` / `look [object]` | `inspect desk` | Deeply examine clues in your inventory, or static objects in the room. |
| **Open Case File** | `inventory` / `inv` | `inventory` | Pull open your trench coat pockets and inspect your gathered evidence array. |
| **Field Guide & Exit** | `help` / `quit` | `help` | Open the full field guide framework inside the console, or resign from the force. |

---

## ⚖️ Case File Resolutions (The Endings Checklist)

Your thoroughness as an investigator determines your ultimate fate at the climax. Can you find all three paths?

* **🏆 The True Ending:** Collect both the poison report and threatening letter, then confront Daniel. You arrest him and solve the homicide.
* **🌧️ The Bad Ending:** Confront Daniel without both pieces of evidence. The case fails and is closed as a natural death.
* **🚨 The Secret Path:** Use the `use_kit` action in Daniel's apartment to uncover the hidden ledger. Return to the police station and confront Captain Morrison while carrying it.