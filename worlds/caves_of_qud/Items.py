from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification


class CoQItem(Item):
    game: str = "Caves of Qud"


class CoQItemData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler
    max_quantity: int = 1
    weight: int = 1


def get_items_by_category(category: str) -> Dict[str, CoQItemData]:
    item_dict: Dict[str, CoQItemData] = {}
    for name, data in item_table.items():
        if data.category == category:
            item_dict.setdefault(name, data)

    return item_dict


item_table: Dict[str, CoQItemData] = {
    # Quest Items
    "Stamped Data Disk":        CoQItemData("Quest Item", 660_000, ItemClassification.progression),
    "Droid Scrambler":          CoQItemData("Quest Item", 660_001, ItemClassification.useful),
    "Q-Girl Blueprints":        CoQItemData("Quest Item", 660_002, ItemClassification.progression),
    "Quantum Mote":             CoQItemData("Quest Item", 660_003, ItemClassification.useful),
    "Tattoo Gun":               CoQItemData("Quest Item", 660_004, ItemClassification.progression),

    # Sidequest Items
    "Amaranthine Prism":        CoQItemData("Sidequest",  660_005, ItemClassification.useful),
    "Repulsive Device":         CoQItemData("Sidequest",  660_006, ItemClassification.useful),
    "Tau's Chime":              CoQItemData("Sidequest",  660_007, ItemClassification.useful),

    # Items
    "Mid-Tier Armor":           CoQItemData("Items",      660_017, ItemClassification.useful, 4), # Armor 4, 25% mod chance
    "High-Tier Armor":          CoQItemData("Items",      660_018, ItemClassification.useful, 2), # Armor 7, 50% mod chance
    "Mid-Tier Melee":           CoQItemData("Items",      660_019, ItemClassification.useful, 4), # Melee 4, 25% mod chance
    "High-Tier Melee":          CoQItemData("Items",      660_020, ItemClassification.useful, 2), # Melee 7, 50% mod chance
    "Mid-Tier Ranged":          CoQItemData("Items",      660_021, ItemClassification.useful, 4), # Missile 4, 25% mod chance
    "High-Tier Ranged":         CoQItemData("Items",      660_022, ItemClassification.useful, 2), # Missile 7, 50% mod chance
    "Mid-Tier Artifact":        CoQItemData("Items",      660_023, ItemClassification.useful, 8), # Artifact 4
    "High-Tier Artifact":       CoQItemData("Items",      660_024, ItemClassification.useful, 4), # Artifact 7
    "Relic":                    CoQItemData("Items",      660_025, ItemClassification.useful, 2), # Extradimensional Relic

    # Junk
    "Low-Tier Junk":            CoQItemData("Filler",     660_100, weight=15), # 1d4 Junk 2
    "Mid-Tier Junk":            CoQItemData("Filler",     660_101, weight=10), # 1d3 Junk 4
    "High-Tier Junk":           CoQItemData("Filler",     660_102, weight=5), # 1d2 Junk 6
    "Waterskin":                CoQItemData("Filler",     660_103, weight=5), # Waterskin with 32 drams of water
    "Some Cells":               CoQItemData("Filler",     660_104, weight=5), # 1d3 Cells
    "Some Books":               CoQItemData("Filler",     660_105, weight=2), # 1d3 Books
    "1000 XP":                  CoQItemData("Filler",     660_106, weight=5),
}

event_item_table: Dict[str, CoQItemData] = {
    "A Signal in the Noise":        CoQItemData("Event", classification=ItemClassification.progression),
    "More Than a Willing Spirit":   CoQItemData("Event", classification=ItemClassification.progression),
    "Decoding the Signal":          CoQItemData("Event", classification=ItemClassification.progression),
    "The Earl of Omonporch":        CoQItemData("Event", classification=ItemClassification.progression),
    "Grave Thoughts":               CoQItemData("Event", classification=ItemClassification.progression),
    "Pax Klanq, I Presume?":        CoQItemData("Event", classification=ItemClassification.progression),
    "Tomb of the Eaters":           CoQItemData("Event", classification=ItemClassification.progression),
    "The Golem":                    CoQItemData("Event", classification=ItemClassification.progression),
    "Reclamation":                  CoQItemData("Event", classification=ItemClassification.progression),
    # "We Are Starfreight":           CoQItemData("Event", classification=ItemClassification.progression),
    "O Glorious Shekhinah!":        CoQItemData("Event", classification=ItemClassification.useful),
    "Raising Indrix":               CoQItemData("Event", classification=ItemClassification.useful),
    "Spread Klanq":                 CoQItemData("Event", classification=ItemClassification.useful),
    "Kith and Kin":                 CoQItemData("Event", classification=ItemClassification.useful),
    "Love and Fear":                CoQItemData("Event", classification=ItemClassification.useful),
    "Fraying Favorites":            CoQItemData("Event", classification=ItemClassification.useful),
    "Return to the Hydropon":       CoQItemData("Event", classification=ItemClassification.useful),
    "If, Then, Else":               CoQItemData("Event", classification=ItemClassification.useful),
}