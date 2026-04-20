# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################

class Goal(Choice):
    """Choose goal type.
     ship_win_count: Goal when winning with a certain number of ship layouts.
     ship_win_selection: Goal when selected ship layouts each won a run."""
    display_name = "Victory condition"
    option_ship_win_count = 0
    option_ship_win_selection = 1
    default = 0

class ShipWinSelection(OptionSet):
    """Select which ship layouts must win for the goal to be achieved. Only used if Victory condition is set to 'Selected ship layouts each won a run'."""
    display_name = "Victory condition: Ship layout selection"
    valid_keys = ["Kestrel A", "Kestrel B", "Kestrel C", "Engi A", "Engi B", "Engi C", "Federation A", "Federation B", "Federation C", "Mantis A", "Mantis B", "Mantis C", "Zoltan A", "Zoltan B", "Zoltan C", "Slug A", "Slug B", "Slug C", "Rock A", "Rock B", "Rock C", "Stealth A", "Stealth B", "Stealth C", "Lanius A", "Lanius B", "Crystal A", "Crystal B"]

class ShipWinCount(Range):
    """Select how many ship layouts must win for the goal to be achieved. Only used if Victory condition is set to 'Win with a certain number of ship layouts'."""
    display_name = "Victory condition: Number of ship layouts"
    range_start = 1
    range_end = 28
    default = 3

class StartingShip(Choice):
    """Choose the starting ship."""
    display_name = "Starting ship"
    option_random = 0
    option_kestrel = 1
    option_engi = 2
    option_federation = 3
    option_mantis = 4
    option_zoltan = 5
    option_slug = 6
    option_rock = 7
    option_stealth = 8
    option_lanius = 9
    option_crystal = 10
    default = 1

class SectorSanity(Choice):
    """Enables checks for sectors reached.
     all: Every sector reached is a check.
     five_and_eight: Only sectors 5 and 8 are checks.
     none: Sectors are not checks."""
    display_name = "Sectorsanity"
    option_all = 0
    option_five_and_eight = 1
    option_none = 2
    default = 1

class ShipAchievements(Toggle):
    """Whether ship achievements are checks."""
    display_name = "Ship achievements checks"
    default = True

class GeneralAchievements(Toggle):
    """Whether general achievements are checks."""
    display_name = "General achievements checks"
    default = True

class GoingTheDistance(Choice):
    """Second row of general achievements are harder. Set the type of items that can be sent if they do send checks, and whether they are checks at all.
     off: Going the distance achievements are not checks.
     unprioritized: Going the distance achievements are checks, but may not contain progression items.
     normal: Going the distance achievements may contain progression items."""
    display_name = "Going the distance achievements checks"
    option_off = 0
    option_unprioritized = 1
    option_normal = 2
    default = 1

class ShipAndEquipmentFeats(Choice):
    """Third row of general achievements are harder. Set the type of items that can be sent if they do send checks, and whether they are checks at all.
     off: Ship and equipment feats are not checks.
     unprioritized: Ship and equipment feats are checks, but may not contain progression items.
     normal: Ship and equipment feats may contain progression items."""
    display_name = "Ship and equipment feats checks"
    option_off = 0
    option_unprioritized = 1
    option_normal = 2
    default = 1

class ShieldsBlueprintProgression(Choice):
    """Shields blueprint logic.
     required: The Shields blueprint is required to play a ship with Shields and upgrade the Shields system. While unobtained, you can only play with Stealth.
     upgrade_only: The Shields blueprint is not required to play a ship with Shields, but is required to upgrade the Shields system.
     start_with: Start with the blueprint."""
    display_name = "Shields blueprint logic"
    option_required = 0
    option_upgrade_only = 1
    option_start_with = 2
    default = 1

class SensorsBlueprintProgression(Choice):
    """Sensors blueprint logic.
     required: The Sensors blueprint is required to play a ship with Sensors and upgrade the Sensors system. While unobtained, you can only play with Slug or Mantis.
     upgrade_only: The Sensors blueprint is not required to play a ship with Sensors, but is required to upgrade the Sensors system.
     start_with: Start with the blueprint."""
    display_name = "Sensors blueprint logic"
    option_required = 0
    option_upgrade_only = 1
    option_start_with = 2
    default = 1

class MedbayBlueprintProgression(Choice):
    """Medbay blueprint logic.
     required: The Medbay blueprint is required to play a ship with Medbay and upgrade the Medbay system. While unobtained, you can only play with Lanius.
     upgrade_only: The Medbay blueprint is not required to play a ship with Medbay, but is required to upgrade the Medbay system.
     start_with: Start with the blueprint."""
    display_name = "Medbay blueprint logic"
    option_required = 0
    option_upgrade_only = 1
    option_start_with = 2
    default = 1

class EnginesBlueprintLogic(Choice):
    """Engines blueprint logic. The Engines blueprint isn't required to play a ship with Engines, but is required to upgrade the Engines system.
     anywhere: no restrictions on where the Engines blueprint is placed.
     early: Place the blueprint in early spheres.
     start_with: Start with the blueprint."""
    display_name = "Engines blueprint logic"
    option_anywhere = 0
    option_early = 1
    option_start_with = 2
    default = 1

class WeaponsBlueprintLogic(Choice):
    """Weapons blueprint logic. The Weapons blueprint isn't required to play a ship with Weapons, but is required to upgrade the Weapons system.
     anywhere: no restrictions on where the Weapons blueprint is placed.
     early: Place the blueprint in early spheres.
     start_with: Start with the blueprint."""
    display_name = "Weapons blueprint logic"
    option_anywhere = 0
    option_early = 1
    option_start_with = 2
    default = 1

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["goal"] = Goal
    options["ship_win_selection"] = ShipWinSelection
    options["ship_win_count"] = ShipWinCount
    options["starting_ship"] = StartingShip
    options["sector_sanity"] = SectorSanity
    options["ship_achievements"] = ShipAchievements
    options["general_achievements"] = GeneralAchievements
    options["going_the_distance"] = GoingTheDistance
    options["ship_and_equipment_feats"] = ShipAndEquipmentFeats
    options["shields_blueprint_progression"] = ShieldsBlueprintProgression
    options["sensors_blueprint_progression"] = SensorsBlueprintProgression
    options["medbay_blueprint_logic"] = MedbayBlueprintLogic
    options["engines_blueprint_logic"] = EnginesBlueprintLogic
    options["weapons_blueprint_logic"] = WeaponsBlueprintLogic
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
