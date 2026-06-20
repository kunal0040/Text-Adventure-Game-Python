# ==========================================
# 1. THE CHARACTERS DICTIONARY
# ==========================================

characters = {
    "captain_morrison": {
        "name": "Captain Morrison 🚬",
        "description": "A cynical, chain-smoking precinct veteran with ash on his lapels.\nHe wants this wrapped up fast, quiet, and filed away before dawn!!!",
        "is_suspect": False
    },
    "mrs_chen": {
        "name": "Mrs. Chen 🧹",
        "description": "The jittery housekeeper who discovered the body. Her hands tremble violently!!\nShe keeps staring at the shadows like they're about to swallow her whole!!!",
        "is_suspect": True
    },
    "ray": {
        "name": "Ray 'The Wire' Malone 🕶️",
        "description": "A seasoned street-broker dripping with cheap pomade and bad intentions!\nHe sells secrets for a living.",
        "is_suspect": False
    },
    "daniel_harlow": {
        "name": "Daniel Harlow 👔",
        "description": "The victim's sharp-dressed, slick-talking son.\nHe plays the grieving family member beautifully!",
        "is_suspect": True
    },
    "dr_patel": {
        "name": "Dr. Aris Patel 🥼",
        "description": "The clinical, sleep-deprived chief pathologist down in the cold room.\nHe treats dead bodies like jigsaw puzzles!",
        "is_suspect": False
    }
}

# ==========================================
# 2. THE EXPANDED BRANCHING ROOMS DICTIONARY
# ==========================================

rooms = {
    "police_station": {
        "description": "🚨 The 4th Precinct is a dim jungle of buzzing fluorescent tubes and desperate characters!\nRain punches hard against the high windows, washing grease tracks down the glass!!\nThe air is heavy with stale tobacco smoke and damp wool coats!",
        "short_desc": "🚨 The grim, rain-streaked bullpen of the 4th Precinct.",
        "exits": {"north": "crime_scene", "south": None, "east": "evidence_room", "west": None},
        # Engine keys are kept lowercase for simple coding checks
        "items": ["case_file", "badge", "wallet"],
        "characters": ["captain_morrison"],
        "locked": False,
        "requires": None,
        "dialogue": {
            "captain_morrison": (
                "Morrison doesn't lift his eyes from his whiskey-ringed desk. He slams a heavy fist down!!! 💥\n\n"
                "\"Listen up, rookie! Harlow is dead in his mansion up on the hill!!! 🏰\n"
                "The high-society doctors are calling it a heart attack, but my gut says they're covering up something ugly!!! 🤬\n\n"
                "You're the only investigator left in the bullpen tonight, {player_name}.\n"
                "Grab your BADGE, your WALLET, and that flimsy CASE FILE off the green cabinet!\n"
                "Get out there, play nice with the press, and don't make me look stupid!!!!!\" 🫵🔥"
            )
        },
        "examine": {
            "case_file": "📁 A manila folder marked 'HARLOW, V. — UNATTENDED DEATH'.\nInside is a photograph of a fierce, unsmiling old tycoon and a sharp handwritten note:\n'Natural causes, sudden cardiac arrest around midnight!'",
            "badge": "🛡️ A heavy shield of tarnished silver.\nIt's dented and scratched, but it still opens doors that normal people find locked!!!",
            "wallet": "💵 A frayed leather bifold stuffed with a handful of crumpled bills\njust large enough to buy a liar's cooperation!"
        },
        "actions": {}
    },

    "crime_scene": {
        "description": "🏰 Victor Harlow's private sanctuary is a heavy vault of dark mahogany and suffocating wealth!!\nThe multi-millionaire sits slumped back in his towering leather throne,\nstaring at the ceiling with sightless eyes frozen in absolute terror!!!!! 👁️👁️",
        "short_desc": "🏰 The grand, silent study where Victor Harlow's body sits cold.",
        "exits": {"north": "hallway", "south": "police_station", "east": None, "west": None},
        "items": ["broken_watch"],
        "characters": [],
        "locked": True,
        "requires": "badge",
        "dialogue": {},
        "examine": {
            "body": "🥶 Harlow's skin is deadly pale, but his lips have a strange, ghostly blue tint!!\nHis fingernails are dug deep into his own chest, as if he was trying to tear his own heart out before it stopped beating!!!!! 💔",
            "desk": "☕ The top of the desk is pristine, save for a delicate porcelain teacup sitting near the dead man's elbow.\nIt's empty, but a dry, sticky residue clings to the bottom...",
            "broken_watch": "⌚ A heavy, gold pocket watch lies on the rug, ripped clean away from Harlow's vest!!!\nThe crystalline face is shattered, and the delicate gold hands are locked immovably at 11:47 PM!!!!! ⏱️💥"
        },
        "actions": {}
    },

    "hallway": {
        "description": "🥀 The vast, cavernous corridor of the Harlow Manor feels like a graveyard for dead kings!\nGrim oil portraits line the walls, their painted eyes catching the moonlight.\nMrs. Chen stands shaking near an ornate marble vase!!",
        "short_desc": "🥀 The grand, echoing corridor of the Harlow estate.",
        "exits": {"north": "harlow_office", "south": "crime_scene", "east": "bar_neutral", "west": None},
        "items": [],
        "characters": ["mrs_chen"],
        "locked": False,
        "requires": None,
        "dialogue": {
            "mrs_chen": (
                "She shrieks loudly when you step into the light, twisting her lace handkerchief into tight knots!!! 😭💔\n\n"
                "\"I just brought him his midnight tea, officer!!! The door was locked from the inside like always!!!\n"
                "I used my spare key... and there he was!!! ☕💀 I didn't see anyone!!! I swear!!!!!\""
            )
        },
        "examine": {},
        "actions": {
            "comfort": "You speak softly to Mrs. Chen.\nShe calms down slightly and points toward the grandfather clock!\n'I heard a loud argument up here at 11:30 PM... it sounded exactly like Master Daniel!' 🗣️🕵️‍♂️\n(Path A unlocked!)",
            "threaten": "You step sharply into her personal space and demand answers! She bursts into hysterical tears!!! 😭\nIn her panic, she knocks over her cleaning tote, dropping a police-grade FINGERPRINT KIT on the rug before running away!!! 🏃‍♀️💨\n(Path B unlocked!)",
            "show_watch": "You dangle the broken watch in front of her face!\n'Wait... his watch stopped at 11:47?! ⏱️😱 Holy mother... but I didn't even come upstairs until midnight!!!\nSomeone else must have been in there!!!!!' She drops a FINGERPRINT KIT in sheer terror and flees!!! 🏃‍♀️💨"
        }
    },

    "harlow_office": {
        "description": "🏢 The downtown commercial office of Harlow Enterprises is an exercise in corporate coldness.\nFiling cabinets line the walls like iron soldiers, and giant glass windows offer a dizzying view of the city's neon skyline bleeding through the downpour!",
        "short_desc": "🏢 The cold, sterile penthouse office of Harlow Enterprises.",
        "exits": {"north": "suspects_apartment", "south": "hallway", "east": None, "west": None},
        "items": ["threatening_letter"],
        "characters": ["daniel_harlow"],
        "locked": False,
        "requires": None,
        "dialogue": {
            "daniel_harlow": (
                "Daniel turns smoothly from the window, swirling a glass of amber liquid with a cold smile. 🥃😏\n\n"
                "\"A terrible shock. My father's heart was a ticking time bomb!! 💣\n"
                "I'm just here ensuring our corporate transitions go smoothly.\n"
                "High finance waits for no man, not even the dead! ✨ Let me know when your little formality of an investigation is over, {player_name}...\" 👋👔"
            )
        },
        "examine": {
            "wastebasket": "🗑️ Inside the metal bin, hidden beneath a layer of discarded reports,\nis a crumpled piece of heavy, expensive parchment paper!!!",
            "threatening_letter": "✉️ A typed letter on custom stationery:\n'Pay out my share or the city finds out what you did!!! I won't let you ruin me, Victor!!!!!'\nIt is signed with a bold, aggressive letter 'D'!!! ✒️🔥"
        },
        "actions": {
            "accuse": "You flat out accuse Daniel of the crime based on the argument! He laughs coldly.\n'A bold claim!! Come back when you have actual science backing up your fairy tales, or my lawyers will take your shield!!!' ⚖️❌",
            "bluff": "You lie flatly and say a witness saw him leave the mansion at midnight!\nHis hand tightens violently around his whiskey glass until his knuckles turn stark white!!\n'Witnesses lie!! Especially poor ones!!' 🥃😬\n(You stealthily pocket the THREATENING LETTER from his desk during his momentary panic!)"
        }
    },

    "bar_neutral": {
        "description": "🎷 The Blue Neon Lounge is a dark dive bar where dreams go to die.\nA low-frequency jazz record plays scratchily from a cracked jukebox.\nRay 'The Wire' Malone sits silently in the back corner.",
        "short_desc": "🎷 The smoky, low-lit basement of the Blue Neon Lounge.",
        "exits": {"west": "hallway", "north": None, "south": None, "east": None},
        "items": [],
        "characters": ["ray"],
        "locked": False,
        "requires": None,
        "dialogue": {
            "ray": "Ray pulls his grease-stained fedora down, hiding his eyes in deep shadow. 🕶️🤫\n\n\"I don't talk to the law, pal. Bad for my health, worse for my reputation!! 🤐\""
        },
        "examine": {},
        "actions": {
            "bribe": "You slide your WALLET across the sticky counter!\n(Changes location to bar_bribed!)",
            "intimidate": "You flash your identification and violently slam him against the buzzing jukebox!!!\n(Changes location to bar_hostile!)"
        }
    },

    "bar_bribed": {
        "description": "🎷 The Blue Neon Lounge looks a bit warmer now that cold cash has changed hands!\nRay leans forward over the table, ready to spill everything.",
        "short_desc": "🎷 The Blue Neon Lounge (Bribed State).",
        "exits": {"west": "hallway", "north": "confrontation", "south": None, "east": None},
        "items": [],
        "characters": ["ray"],
        "locked": False,
        "requires": None,
        "dialogue": {
            "ray": "Ray counts the crumpled bills with a slick, greedy grin!! 💵🤩\n\n'Alright, let's talk business! Daniel Harlow is deep in debt with some very nasty lenders—he owes more than a million!!! 📉💥\nHe was bragging here last night that he found an untraceable way out... something about a rare poison called Cyanide-X that looks exactly like a heart attack!' 🧪💀"
        },
        "examine": {},
        "actions": {}
    },

    "bar_hostile": {
        "description": "🎷 The jukebox needle is broken! Patrons are actively glaring at you.\nRay completely refuses to look at you, staring straight ahead.",
        "short_desc": "🎷 The Blue Neon Lounge (Hostile State).",
        "exits": {"west": "hallway", "north": None, "south": None, "east": None},
        "items": [],
        "characters": ["ray"],
        "locked": False,
        "requires": None,
        "dialogue": {
            "ray": "Ray spits directly onto the floor.\n'Nice muscle! Too bad it doesn't scare me one bit.\nGet lost before you get hurt!!!' You got absolutely nothing!!! ❌"
        },
        "examine": {},
        "actions": {}
    },

    "suspects_apartment": {
        "description": "💎 Daniel Harlow's luxury apartment is a loud, vulgar exhibition of unearned wealth!\nExtravagant modern sculptures stand like grotesque sentinels in the corners.",
        "short_desc": "💎 Daniel Harlow's chaotic, high-priced downtown apartment.",
        "exits": {"north": "confrontation", "south": "harlow_office", "east": None, "west": None},
        "items": ["poison_vial"],
        "characters": [],
        "locked": True,
        "requires": "threatening_letter",
        "dialogue": {},
        "examine": {
            "poison_vial": "🧪 Hidden deep inside the toe of an exotic alligator boot in the closet is a tiny glass bottle!!!\nThe label has been roughly peeled away, but a crystalized film of clear liquid remains stuck to the dropper!!! ☠️",
            "desk": "🖤 A sleek, black lacquer writing desk sits against the wall, entirely clear of papers.\nThe surface looks completely immaculate...",
            "hidden_ledger": "📂 *CLICK!!!*\nUsing the FINGERPRINT KIT on the desk reveals a hidden latch!!! A secret drawer pops open, revealing a black ledger book!\nIts pages detail systematic kickbacks routed directly to a private account owned by CAPTAIN MORRISON!!!!! 🚨😱"
        },
        "actions": {}
    },

    "evidence_room": {
        "description": "🥼 The precinct crime lab and morgue is a freezing vault of blinding white tile and gleaming stainless steel.\nThe harsh glare of fluorescent tubes bounces off chemical flasks and specimen jars.",
        "short_desc": "🥼 The bright, freezing vault of the precinct morgue.",
        "exits": {"west": "police_station", "north": None, "south": None, "east": None},
        "items": [],
        "characters": ["dr_patel"],
        "locked": False,
        "requires": None,
        "dialogue": {
            "dr_patel": (
                "Dr. Patel adjusts his spectacles, typing furiously on a mechanical keyboard. 🧪🔬\n\n"
                "\"I'm a scientist, not a magician!!! ☕ Autopsies take time!\n"
                "If you want me to declare a billionaire's heart attack a murder, you need to bring me real, physical proof to analyze!!!\""
            )
        },
        "examine": {
            "poison_report": "📄 An official forensic certification bearing the city seal and Dr. Patel's signature.\nIt lists the cause of death explicitly as forced chemical assassination via Cyanide-X!!!"
        },
        "actions": {
            "test_vial": "You hand over the poison_vial. Patel's eyes instantly widen!!! He runs the residue through a centrifuge!! 🧬🌀\n\n'Incredible... This is highly concentrated Cyanide-X!!! It paralyzes the heart muscle instantly while leaving almost no trace!\nThis report proves Victor Harlow was intentionally poisoned at exactly 11:47 PM!!!!! Take it. You've got your homicide!!!' 📄🔥"
        }
    },

    "confrontation": {
        "description": "🌧️ The penthouse terrace hangs over the edge of the city like an iron balcony over an abyss.\nRain drives down in sheets, turning the distant neon street signs into blurry smears of pink and blue light!!",
        "short_desc": "🌧️ The rain-swept penthouse terrace hanging over the dark city.",
        "exits": {"south": "suspects_apartment", "north": None, "east": None, "west": None},
        "items": [],
        "characters": ["daniel_harlow"],
        "locked": False,
        "requires": None,
        "dialogue": {
            "daniel_harlow": (
                "Daniel turns around, his eyes flashing like sharp ice under the storm clouds!! ⛈️🚬\n\n"
                "\"Quite a storm, isn't it?! You've been scurrying all over town pulling on loose threads!!! 🫵😏\n"
                "I hope for your sake you've found something actually worth my time!\n"
                "Because if you've come up here without ironclad proof, I'm going to ensure you spend the rest of your short career directing traffic in the slums!!!!!\" 🥶🔥"
            )
        },
        "examine": {},
        "actions": {}
    }
}

# ==========================================
# 3. THE ENDINGS DICTIONARY
# ==========================================

endings = {
    "true_ending": {
        "title": "THE COMPASS OF JUSTICE 🧭✨",
        "text": "You draw the POISON REPORT and the THREATENING LETTER from your wet trench coat!\nDaniel's calm demeanor instantly cracks; his face drains of color, and his cigarette drops into a puddle with a faint hiss!!\nHe stammers, trying to weave another desperate lie, but the paperwork is completely ironclad!!!\n\nYou snap the heavy steel handcuffs tightly over his wrists, securing your first solo homicide conviction!!!\nThe city below is still a corrupt, rain-soaked concrete jungle, but tonight, you proved that some monsters don't get away with it!!!!"
    },
    "bad_ending": {
        "title": "A COLD NIGHT IN THE GUTTER 🌧️🥃",
        "text": "You attempt to accuse Daniel based on mere suspicion, or perhaps you pointed your finger at the frantic housekeeper back at the manor!\nWithout the certified POISON REPORT, Daniel's high-priced corporate attorneys reduce your amateur theories to absolute dust within seconds!!!!!\n\nThe police department issues an immediate, sweeping public apology to the Harlow estate, and the case is permanently closed as a natural heart attack!!\nYou are stripped of your gun and badge for gross incompetence, leaving you to spend your remaining years drinking cheap whiskey at Ray's bar, staring miserably into the bottom of a glass!"
    },
    "secret_ending": {
        "title": "A DEEPER SHADE OF NOIR 🚨💀",
        "text": "You bypass the penthouse terrace entirely! Instead, you slip through the rainy night back to the police_station, silently entering the Captain's office and slamming the HIDDEN LEDGER heavily onto his desk!!!\n\nMorrison stares at the open pages detailing his years of bribery, his cigar smoke curling lazily around his face. He doesn't panic at all!!\nInstead, he slowly smiles, sliding his right hand beneath his jacket toward his shoulder holster!!!\n\nYou realize with sickening clarity why this impossible, locked-room murder case was handed to an inexperienced investigator like you!!!\nThe rain beats heavily against the glass, ready to wash away yet another inconvenient truth!!!!"
    }
}