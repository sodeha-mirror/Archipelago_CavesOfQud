from typing import List

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import CoQItem, CoQItemData, event_item_table, get_items_by_category, item_table
from .Locations import location_table, event_location_table
from .Options import CoQOptions
# from .Presets import rl_options_presets
from .Regions import create_regions
from .Rules import set_rules


class CoQWeb(WebWorld):
    theme = "jungle"
    # tutorials = [Tutorial(
    #     "Multiworld Setup Guide",
    #     "A guide to setting up the Rogue Legacy Randomizer software on your computer. This guide covers single-player, "
    #     "multiworld, and related software.",
    #     "English",
    #     "rogue-legacy_en.md",
    #     "rogue-legacy/en",
    #     ["Phar"]
    # )]
    # bug_report_page = "none"
    # options_presets = rl_options_presets


class CoQWorld(World):
    # """
    # Rogue Legacy is a genealogical rogue-"LITE" where anyone can be a hero. Each time you die, your child will succeed
    # you. Every child is unique. One child might be colorblind, another might have vertigo-- they could even be a dwarf.
    # But that's OK, because no one is perfect, and you don't have to be to succeed.
    # """
    game = "Caves of Qud"
    options_dataclass = CoQOptions
    options: CoQOptions
    topology_present = True
    required_client_version = (0, 3, 5)
    web = CoQWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items() if data.code is not None}
    location_name_to_id = {name: data.code for name, data in location_table.items() if data.code is not None}

    def fill_slot_data(self) -> dict:
        return self.options.as_dict(*[name for name in self.options_dataclass.type_hints.keys()])

    # def generate_early(self):
    #     # Check validation of names.
    #     additional_lady_names = len(self.options.additional_lady_names.value)
    #     additional_sir_names = len(self.options.additional_sir_names.value)
    #     if not self.options.allow_default_names:
    #         if additional_lady_names < int(self.options.number_of_children):
    #             raise Exception(
    #                 f"allow_default_names is off, but not enough names are defined in additional_lady_names. "
    #                 f"Expected {int(self.options.number_of_children)}, Got {additional_lady_names}")

    #         if additional_sir_names < int(self.options.number_of_children):
    #             raise Exception(
    #                 f"allow_default_names is off, but not enough names are defined in additional_sir_names. "
    #                 f"Expected {int(self.options.number_of_children)}, Got {additional_sir_names}")

    def create_items(self):
        item_pool: List[CoQItem] = []
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        for name, data in item_table.items():
            quantity = data.max_quantity

            # Ignore filler, it will be added in a later stage.
            if data.category == "Filler":
                continue

            item_pool += [self.create_item(name) for _ in range(0, quantity)]

        # Fill any empty locations with filler items.
        while len(item_pool) < total_locations:
            item_pool.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += item_pool

    def get_filler_item_name(self) -> str:
        fillers = get_items_by_category("Filler")
        weights = [data.weight for data in fillers.values()]
        return self.random.choices([filler for filler in fillers.keys()], weights, k=1)[0]

    def create_item(self, name: str) -> CoQItem:
        data = item_table[name]
        return CoQItem(name, data.classification, data.code, self.player)

    def create_event(self, name: str) -> CoQItem:
        data = event_item_table[name]
        return CoQItem(name, data.classification, data.code, self.player)

    def set_rules(self):
        set_rules(self, self.player)

    def create_regions(self):
        create_regions(self)
        self._place_events()

    def _place_events(self):
        for name, item in event_location_table:
            self.multiworld.get_location(name, self.player).place_locked_item(self.create_event(name))
        # Fountain
        # self.multiworld.get_location("Fountain Room", self.player).place_locked_item(
        #     self.create_event("Defeat The Fountain"))

        # # Khidr / Neo Khidr
        # if self.options.khidr == "vanilla":
        #     self.multiworld.get_location("Castle Hamson Boss Room", self.player).place_locked_item(
        #         self.create_event("Defeat Khidr"))
        # else:
        #     self.multiworld.get_location("Castle Hamson Boss Room", self.player).place_locked_item(
        #         self.create_event("Defeat Neo Khidr"))

        # # Alexander / Alexander IV
        # if self.options.alexander == "vanilla":
        #     self.multiworld.get_location("Forest Abkhazia Boss Room", self.player).place_locked_item(
        #         self.create_event("Defeat Alexander"))
        # else:
        #     self.multiworld.get_location("Forest Abkhazia Boss Room", self.player).place_locked_item(
        #         self.create_event("Defeat Alexander IV"))

        # # Ponce de Leon / Ponce de Freon
        # if self.options.leon == "vanilla":
        #     self.multiworld.get_location("The Maya Boss Room", self.player).place_locked_item(
        #         self.create_event("Defeat Ponce de Leon"))
        # else:
        #     self.multiworld.get_location("The Maya Boss Room", self.player).place_locked_item(
        #         self.create_event("Defeat Ponce de Freon"))

        # # Herodotus / Astrodotus
        # if self.options.herodotus == "vanilla":
        #     self.multiworld.get_location("Land of Darkness Boss Room", self.player).place_locked_item(
        #         self.create_event("Defeat Herodotus"))
        # else:
        #     self.multiworld.get_location("Land of Darkness Boss Room", self.player).place_locked_item(
        #         self.create_event("Defeat Astrodotus"))