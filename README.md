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
* **Hybrid Fast Travel System:** Tracks your exploration footprint automatically using a Python cache set (`visited_rooms`). Once you discover a room, you can bypass repetitive cardinal directions and instantly warp back by typing `go [room_name]`.
* **Look-Ahead Lock Protection:** A smart validation layer built directly into the fast travel mechanic. Before teleporting you across town, the engine scans the destination's rules—if story configurations or item locks have changed, it blocks the shortcut to preserve the game's logical puzzle boundaries.
* **Modular Multi-State Progression:** Special room action hooks completely morph environmental scenes, spawning hidden elements on the fly or shifting characters from cooperative to hostile based entirely on your approach.

---

## 🎮 How to Play & Case Controls

The parser engine dynamically filters your typed inputs into executable core verbs and lowercase target arguments:

| Action | Command Syntax | Example | Description |
| :--- | :--- | :--- | :--- |
| **Move & Navigation** | `go [direction]` | `go north` | Walk between adjacent areas manually. |
| **Instant Shortcut Warp** | `go [room_name]` | `go police_station` | Fast travel directly to any area you have previously uncovered. |
| **Interrogation** | `talk [suspect/witness]` | `talk butler` | Grill entities. Character matching handles loose names seamlessly. |
| **Evidence Gathering** | `take [item]` | `take vial` | Secure a clue from the floor and add it to your case file. |
| **Forensic Inspection** | `inspect [item]` / `look [object]` | `inspect desk` | Deeply examine clues in your inventory, or static objects in the room. |
| **Open Case File** | `inventory` / `inv` | `inventory` | Pull open your trench coat pockets and inspect your gathered evidence array. |
| **Field Guide & Exit** | `help` / `quit` | `help` | Open the full field guide framework inside the console, or resign from the force. |

---

## ⚖️ Case File Resolutions (The Endings Checklist)

Your thoroughness as an investigator determines your ultimate fate at the climax. Can you find all three paths?

* **🏆 The True Ending:** Connect the dots, secure the definitive forensic proof, and force a brilliant killer's final confession.
* **🌧️ The Bad Ending:** Fail to collect ironclad proof and confront the killer with empty pockets, allowing corporate defense teams to tear your case to pieces.
* **🚨 The Secret Path:** Unearth a hidden thread of systemic betrayal that shifts the entire focus of the case and takes you directly to the top.