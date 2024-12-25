from Options import Choice, Range, Toggle, DeathLink, DefaultOnToggle, OptionSet, PerGameCommonOptions

from dataclasses import dataclass

class GameLength(Choice):
    """
    Determines which tiers of play are included.
    """
    display_name = "Use Content Through __"
    option_gritgate = 0
    option_bethesda = 1
    option_brightsheol = 2
    option_fullgame = 3
    default = 2

# class NumberOfDrops(Range):
#     """
#     Determines approximately how many checks are included as enemy drops (including via merchants).
#     """
#     display_name = "Checks Via Drops"
#     range_start = 0
#     range_end = 120
#     default = 42


# class UniversalChests(Toggle):
#     """
#     Determines if non-fairy chests should be combined into one pool instead of per zone, similar to Risk of Rain 2.
#     """
#     display_name = "Universal Non-Fairy Chests"


# class RequirePurchasing(DefaultOnToggle):
#     """
#     Determines where you will be required to purchase equipment and runes from the Blacksmith and Enchantress before
#     equipping them. If you disable require purchasing, Manor Renovations are scaled to take this into account.
#     """
#     display_name = "Require Purchasing"


# class AdditionalLadyNames(OptionSet):
#     """
#     Set of additional names your potential offspring can have. If Allow Default Names is disabled, this is the only list
#     of names your children can have. The first value will also be your initial character's name depending on Starting
#     Gender.
#     """
#     display_name = "Additional Lady Names"

# class AdditionalSirNames(OptionSet):
#     """
#     Set of additional names your potential offspring can have. If Allow Default Names is disabled, this is the only list
#     of names your children can have. The first value will also be your initial character's name depending on Starting
#     Gender.
#     """
#     display_name = "Additional Sir Names"


# class AllowDefaultNames(DefaultOnToggle):
#     """
#     Determines if the default names defined in the vanilla game are allowed to be used. Warning: Your world will not
#     generate if the number of Additional Names defined is less than the Number of Children value.
#     """
#     display_name = "Allow Default Names"


# class HealthUpPool(Range):
#     """
#     Determines the number of Health Ups in the item pool.
#     """
#     display_name = "Health Up Pool"
#     range_start = 0
#     range_end = 15
#     default = 15


# class ManaUpPool(Range):
#     """
#     Determines the number of Mana Ups in the item pool.
#     """
#     display_name = "Mana Up Pool"
#     range_start = 0
#     range_end = 15
#     default = 15


# class AttackUpPool(Range):
#     """
#     Determines the number of Attack Ups in the item pool.
#     """
#     display_name = "Attack Up Pool"
#     range_start = 0
#     range_end = 15
#     default = 15


# class MagicDamageUpPool(Range):
#     """
#     Determines the number of Magic Damage Ups in the item pool.
#     """
#     display_name = "Magic Damage Up Pool"
#     range_start = 0
#     range_end = 15
#     default = 15


# class ArmorUpPool(Range):
#     """
#     Determines the number of Armor Ups in the item pool.
#     """
#     display_name = "Armor Up Pool"
#     range_start = 0
#     range_end = 10
#     default = 10


# class EquipUpPool(Range):
#     """
#     Determines the number of Equip Ups in the item pool.
#     """
#     display_name = "Equip Up Pool"
#     range_start = 0
#     range_end = 10
#     default = 10


# class CritChanceUpPool(Range):
#     """
#     Determines the number of Crit Chance Ups in the item pool.
#     """
#     display_name = "Crit Chance Up Pool"
#     range_start = 0
#     range_end = 5
#     default = 5


# class CritDamageUpPool(Range):
#     """
#     Determines the number of Crit Damage Ups in the item pool.
#     """
#     display_name = "Crit Damage Up Pool"
#     range_start = 0
#     range_end = 5
#     default = 5


# class FreeDiaryOnGeneration(DefaultOnToggle):
#     """
#     Allows the player to get a free diary check every time they regenerate the castle in the starting room.
#     """
#     display_name = "Free Diary On Generation"


# class AvailableClasses(OptionSet):
#     """
#     List of classes that will be in the item pool to find. The upgraded form of the class will be added with it.
#     The upgraded form of your starting class will be available regardless.
#     """
#     display_name = "Available Classes"
#     default = frozenset(
#         {"Knight", "Mage", "Barbarian", "Knave", "Shinobi", "Miner", "Spellthief", "Lich", "Dragon", "Traitor"}
#     )
#     valid_keys = {"Knight", "Mage", "Barbarian", "Knave", "Shinobi", "Miner", "Spellthief", "Lich", "Dragon", "Traitor"}


@dataclass
class CoQOptions(PerGameCommonOptions):
    game_length: GameLength
    # starting_gender: StartingGender
    # starting_class: StartingClass
    # available_classes: AvailableClasses
    # new_game_plus: NewGamePlus
    # fairy_chests_per_zone: FairyChestsPerZone
    # chests_per_zone: ChestsPerZone
    # universal_fairy_chests: UniversalFairyChests
    # universal_chests: UniversalChests
    # vendors: Vendors
    # architect: Architect
    # architect_fee: ArchitectFee
    # disable_charon: DisableCharon
    # require_purchasing: RequirePurchasing
    # progressive_blueprints: ProgressiveBlueprints
    # gold_gain_multiplier: GoldGainMultiplier
    # number_of_children: NumberOfChildren
    # free_diary_on_generation: FreeDiaryOnGeneration
    # khidr: ChallengeBossKhidr
    # alexander: ChallengeBossAlexander
    # leon: ChallengeBossLeon
    # herodotus: ChallengeBossHerodotus
    # health_pool: HealthUpPool
    # mana_pool: ManaUpPool
    # attack_pool: AttackUpPool
    # magic_damage_pool: MagicDamageUpPool
    # armor_pool: ArmorUpPool
    # equip_pool: EquipUpPool
    # crit_chance_pool: CritChanceUpPool
    # crit_damage_pool: CritDamageUpPool
    # allow_default_names: AllowDefaultNames
    # additional_lady_names: AdditionalLadyNames
    # additional_sir_names: AdditionalSirNames
    death_link: DeathLink