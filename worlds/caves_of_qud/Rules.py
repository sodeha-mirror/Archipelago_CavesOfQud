from BaseClasses import CollectionState
from typing import TYPE_CHECKING
from .Locations import CoQLocation, location_table, get_locations_by_region

if TYPE_CHECKING:
    from . import CoQWorld


def has_reached_grit_gate(state: CollectionState, player: int) -> bool:
    return state.has("A Signal in the Noise", player)


def has_reached_bethesda_susa(state: CollectionState, player: int) -> bool:
    return state.has("Decoding the Signal", player)


def has_reached_brightsheol(state: CollectionState, player: int) -> bool:
    return state.has("Tomb of the Eaters", player)


# def has_defeated_dungeon(state: CollectionState, player: int) -> bool:
#     return state.has("Defeat Herodotus", player) or state.has("Defeat Astrodotus", player)


def set_rules(world: "CoQWorld", player: int):
    
    for location in get_locations_by_region("-> Bethesda Susa").keys():
        world.get_location(location).access_rule = lambda state: has_reached_grit_gate(state, player)
        
    for location in get_locations_by_region("-> Brightsheol").keys():
        world.get_location(location).access_rule = lambda state: has_reached_bethesda_susa(state, player)

    for location in get_locations_by_region("Late Game").keys():
        world.get_location(location).access_rule = lambda state: has_reached_brightsheol(state, player)

    # Region rules.
    world.get_entrance("-> Bethesda Susa").access_rule = \
        lambda state: has_reached_grit_gate(state, player)
    
    world.get_entrance("-> Brightsheol").access_rule = \
        lambda state: has_reached_bethesda_susa(state, player)
    
    world.get_entrance("Late Game").access_rule = \
        lambda state: has_reached_brightsheol(state, player)

    # Win condition.
    if world.options.game_length == 3:
        world.multiworld.completion_condition[player] = lambda state: state.has("Reclamation", player)
    elif world.options.game_length == 2:
        world.multiworld.completion_condition[player] = lambda state: has_reached_brightsheol(state, player)
    elif world.options.game_length == 1:
        world.multiworld.completion_condition[player] = lambda state: has_reached_bethesda_susa(state, player)
    else:
        world.multiworld.completion_condition[player] = lambda state: has_reached_grit_gate(state, player)