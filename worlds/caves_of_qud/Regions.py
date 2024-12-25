from typing import Dict, List, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import MultiWorld, Region, Entrance
from .Locations import CoQLocation, location_table, get_locations_by_region

if TYPE_CHECKING:
    from . import CoQWorld


class CoQRegionData(NamedTuple):
    locations: Optional[List[str]]
    region_exits: Optional[List[str]]


def create_regions(world: "CoQWorld"):
    regions: Dict[str, CoQRegionData] = {
        "Menu":              CoQRegionData(None, ["-> Grit Gate"]),
        "-> Grit Gate":      CoQRegionData([],   ["-> Bethesda Susa"]), # 47 locations, 1 main quest 12/24/24
        "-> Bethesda Susa":  CoQRegionData([],   ["-> Brightsheol"]), # +16 locations, +2 main quest 12/24/24
        "-> Brightsheol":    CoQRegionData([],   ["Late Game"]), # +13 locations, +4 main quest 12/24/24
        "Late Game":         CoQRegionData([],   []), # +15 locations, +2 main quest 12/24/24

        # "Menu":              CoQRegionData(None, ["-> Grit Gate"]),
        # "-> Grit Gate":      CoQRegionData([],   ["-> Bethesda Susa", "Indrix"]),
        # "-> Bethesda Susa":  CoQRegionData([],   ["-> Brightsheol", "Repulsive Device", "Tau"]),
        # "-> Brightsheol":    CoQRegionData([],   ["Late Game"]),
        # "Late Game":         CoQRegionData([],   []),
        # "Indrix":            CoQRegionData([],   []),
        # "Repulsive Device":  CoQRegionData([],   []),
        # "Tau":               CoQRegionData([],   []),
    }

    for name, data in regions:
        for location in get_locations_by_region(name).keys():
            regions[name].locations.append(location)
        # if world.options.game_length

    # # Artificially stagger diary spheres for progression.
    # for diary in range(0, 25):
    #     region: str
    #     if 0 <= diary < 6:
    #         region = "Castle Hamson"
    #     elif 6 <= diary < 12:
    #         region = "Forest Abkhazia"
    #     elif 12 <= diary < 18:
    #         region = "The Maya"
    #     elif 18 <= diary < 24:
    #         region = "Land of Darkness"
    #     else:
    #         region = "The Fountain Room"
    #     regions[region].locations.append(f"Diary {diary + 1}")

    # # Manor & Special
    # for manor in get_locations_by_category("Manor").keys():
    #     regions["The Manor"].locations.append(manor)
    # for special in get_locations_by_category("Special").keys():
    #     regions["Castle Hamson"].locations.append(special)

    # # Boss Rewards
    # regions["Castle Hamson"].locations.append("Castle Hamson Boss Reward")
    # regions["Forest Abkhazia"].locations.append("Forest Abkhazia Boss Reward")
    # regions["The Maya"].locations.append("The Maya Boss Reward")
    # regions["Land of Darkness"].locations.append("Land of Darkness Boss Reward")

    # # Events
    # regions["Castle Hamson"].locations.append("Castle Hamson Boss Room")
    # regions["Forest Abkhazia"].locations.append("Forest Abkhazia Boss Room")
    # regions["The Maya"].locations.append("The Maya Boss Room")
    # regions["Land of Darkness"].locations.append("Land of Darkness Boss Room")
    # regions["The Fountain Room"].locations.append("Fountain Room")

    # # Chests
    # chests = int(world.options.chests_per_zone)
    # for i in range(0, chests):
    #     if world.options.universal_chests:
    #         regions["Castle Hamson"].locations.append(f"Chest {i + 1}")
    #         regions["Forest Abkhazia"].locations.append(f"Chest {i + 1 + chests}")
    #         regions["The Maya"].locations.append(f"Chest {i + 1 + (chests * 2)}")
    #         regions["Land of Darkness"].locations.append(f"Chest {i + 1 + (chests * 3)}")
    #     else:
    #         regions["Castle Hamson"].locations.append(f"Castle Hamson - Chest {i + 1}")
    #         regions["Forest Abkhazia"].locations.append(f"Forest Abkhazia - Chest {i + 1}")
    #         regions["The Maya"].locations.append(f"The Maya - Chest {i + 1}")
    #         regions["Land of Darkness"].locations.append(f"Land of Darkness - Chest {i + 1}")

    # # Fairy Chests
    # chests = int(world.options.fairy_chests_per_zone)
    # for i in range(0, chests):
    #     if world.options.universal_fairy_chests:
    #         regions["Castle Hamson"].locations.append(f"Fairy Chest {i + 1}")
    #         regions["Forest Abkhazia"].locations.append(f"Fairy Chest {i + 1 + chests}")
    #         regions["The Maya"].locations.append(f"Fairy Chest {i + 1 + (chests * 2)}")
    #         regions["Land of Darkness"].locations.append(f"Fairy Chest {i + 1 + (chests * 3)}")
    #     else:
    #         regions["Castle Hamson"].locations.append(f"Castle Hamson - Fairy Chest {i + 1}")
    #         regions["Forest Abkhazia"].locations.append(f"Forest Abkhazia - Fairy Chest {i + 1}")
    #         regions["The Maya"].locations.append(f"The Maya - Fairy Chest {i + 1}")
    #         regions["Land of Darkness"].locations.append(f"Land of Darkness - Fairy Chest {i + 1}")

    # Set up the regions correctly.
    for name, data in regions.items():
        world.multiworld.regions.append(create_region(world.multiworld, world.player, name, data))

    for name, data in regions.items():
        world.get_entrance(name).connect(world.get_region(name))

    # world.get_entrance("-> Grit Gate").connect(world.get_region("-> Grit Gate"))
    # world.get_entrance("-> Bethesda Susa").connect(world.get_region("-> Bethesda Susa"))
    # world.get_entrance("-> Brightsheol").connect(world.get_region("-> Brightsheol"))
    # world.get_entrance("Late Game").connect(world.get_region("Late Game"))


def create_region(multiworld: MultiWorld, player: int, name: str, data: CoQRegionData):
    region = Region(name, player, multiworld)
    if data.locations:
        for loc_name in data.locations:
            loc_data = location_table.get(loc_name)
            location = CoQLocation(player, loc_name, loc_data.code if loc_data else None, region)
            region.locations.append(location)

    if data.region_exits:
        for exit in data.region_exits:
            entrance = Entrance(player, exit, region)
            region.exits.append(entrance)

    return region