from typing import Dict, NamedTuple, Optional

from BaseClasses import Location


class CoQLocation(Location):
    game: str = "Caves of Qud"


class CoQLocationData(NamedTuple):
    category: str
    region: Optional[str] = "-> Grit Gate"
    code: Optional[int] = None


def get_locations_by_category(category: str) -> Dict[str, CoQLocationData]:
    location_dict: Dict[str, CoQLocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict


def get_locations_by_region(region: str) -> Dict[str, CoQLocationData]:
    location_dict: Dict[str, CoQLocationData] = {}
    for name, data in location_table.items():
        if data.region == region:
            location_dict.setdefault(name, data)

    return location_dict


location_table: Dict[str, CoQLocationData] = {

    # Unique NPCs
    "Barathrum the Old":                        CoQLocationData("NPC", "-> Bethesda Susa",  660_200),
    "Mayor Nuntu of Kyakukya":                  CoQLocationData("NPC", "-> Bethesda Susa",  660_201),
    "Mayor Haddas of Ezra":                     CoQLocationData("NPC", "-> Brightsheol",    660_202),
    "0lam of Tzimtzlum":                        CoQLocationData("NPC", "Late Game",         660_203),
    "Asphodel, Earl of Omonporch":              CoQLocationData("NPC", "-> Brightsheol",    660_204),
    "Eschelstadt II, High Priest of the Stilt": CoQLocationData("NPC",                      660_205),
    "Hindriarch Keh of Bey Lah":                CoQLocationData("NPC",                      660_206),
    "Herododicus":                              CoQLocationData("NPC", "-> Brightsheol",    660_207),
    "Many Eyes of Yd Freehold":                 CoQLocationData("NPC", "Late Game",         660_208),
    "Pax Klanq":                                CoQLocationData("NPC", "-> Brightsheol",    660_209),
    **{f"Legendary Merchant Wares {i+1}":       CoQLocationData("NPC",                      660_250 + i) for i in range(0, 1)},
    **{f"Legendary Merchant Wares {i+1}":       CoQLocationData("NPC", "Late Game",         660_250 + i) for i in range(1, 3)},

    # Bosses
    "Mamon Souldrinker":                        CoQLocationData("Bosses", "-> Bethesda Susa",   661_060),
    "Oboroqoru, Ape God":                       CoQLocationData("Bosses", "-> Brightsheol",     661_060),
    **{f"Girsh Nephilim {i+1}":                 CoQLocationData("Bosses", "Late Game",          661_070 + i) for i in range(0, 2)},
    **{f"Legendary Troll {i+1}":                CoQLocationData("Bosses", "-> Bethesda Susa",   661_080 + i) for i in range(0, 3)},
    **{f"Legendary Lair {i+1}":                 CoQLocationData("Bosses", "-> Bethesda Susa",   661_090 + i) for i in range(0, 3)},
    **{f"Legendary Lair {i+1}":                 CoQLocationData("Bosses", "Late Game",          661_090 + i) for i in range(3, 6)},


    # Drops
    **{f"Snapjaw {i+1}":                        CoQLocationData("Drops",                        662_000 + i) for i in range(0, 8)},
    **{f"Baboon {i+1}":                         CoQLocationData("Drops",                        662_010 + i) for i in range(0, 4)},
    **{f"Issachari {i+1}":                      CoQLocationData("Drops",                        662_020 + i) for i in range(0, 4)},
    **{f"Goatfolk {i+1}":                       CoQLocationData("Drops", "-> Bethesda Susa",    662_030 + i) for i in range(0, 4)},
    **{f"Naphtaali {i+1}":                      CoQLocationData("Drops",                        662_040 + i) for i in range(0, 4)},
    **{f"Merchant Wares {i+1}":                 CoQLocationData("Drops",                        662_050 + i) for i in range(0, 8)},
    **{f"Cragmensch {i+1}":                     CoQLocationData("Drops", "-> Bethesda Susa",    662_060 + i) for i in range(0, 2)},
    **{f"Ooze {i+1}":                           CoQLocationData("Drops",                        662_070 + i) for i in range(0, 4)},
    **{f"Wanderer {i+1}":                       CoQLocationData("Drops",                        662_080 + i) for i in range(0, 4)}, # Hermits, Pariahs, and Mysterious Strangers

    # Locations
    **{f"Forgotten Ruin {i+1}":                 CoQLocationData("Locations",                    662_200 + i) for i in range(0, 4)},
    **{f"Forgotten Ruin {i+1}":                 CoQLocationData("Locations", "Late Game",       662_200 + i) for i in range(4, 8)},

    # Sidequests
    "Raising Indrix Reward":                    CoQLocationData("Sidequest", "-> Bethesda Susa",    662_500),
    **{f"Village Quest {i+1}":                  CoQLocationData("Sidequest",                        662_510 + i) for i in range(0,  2)},
    **{f"Village Quest {i+1}":                  CoQLocationData("Sidequest", "Late Game",           662_510 + i) for i in range(2,  4)},
    **{f"Visit Site {i+1}":                     CoQLocationData("Sidequest",                        662_520 + i) for i in range(0,  2)},
    **{f"Recover Relic {i+1}":                  CoQLocationData("Sidequest", "-> Brightsheol",      662_530 + i) for i in range(0,  1)},
}

event_location_table: Dict[str, CoQLocationData] = {
    "A Signal in the Noise":        CoQLocationData("Event"),
    "More Than a Willing Spirit":   CoQLocationData("Event"),
    "Decoding the Signal":          CoQLocationData("Event"),
    "The Earl of Omonporch":        CoQLocationData("Event"),
    "Grave Thoughts":               CoQLocationData("Event"),
    "Pax Klanq, I Presume?":        CoQLocationData("Event"),
    "Tomb of the Eaters":           CoQLocationData("Event"),
    "The Golem":                    CoQLocationData("Event"),
    "Reclamation":                  CoQLocationData("Event"),
    # "We Are Starfreight":           CoQLocationData("Event"),
    "O Glorious Shekhinah!":        CoQLocationData("Event"),
    "Raising Indrix":               CoQLocationData("Event"),
    "Spread Klanq":                 CoQLocationData("Event"),
    "Kith and Kin":                 CoQLocationData("Event"),
    "Love and Fear":                CoQLocationData("Event"),
    "Fraying Favorites":            CoQLocationData("Event"),
    "Return to the Hydropon":       CoQLocationData("Event"),
    "If, Then, Else":               CoQLocationData("Event"),
}