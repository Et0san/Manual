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


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class AmountOfTokensNeeded(Range):
    """Amount of Delivery Tokens needed to win. Please take in consideration that if you select a high number of Tokens without any of the other options, the majority of items will be progression items."""
    display_name = "Amount of Delivery Tokens needed to win"
    range_start = 10
    range_end = 50
    default = 15

class RandomizeStartingCountry(Toggle):
    """Randomizes the starting country. Default starting country is Germany; if this option is enabled, you will instead get a random Country Key at start, which will define your starting country."""
    display_name = "Randomize Starting Country"
    default = 0

class DLC_GoingEast(Toggle):
    """Enables Going East DLC content."""
    display_name = "DLC: Going East"
    default = 0

class DLC_Scandinavia(Toggle):
    """Enables Scandinavia DLC content."""
    display_name = "DLC: Scandinavia"
    default = 0

class DLC_France(Toggle):
    """Enables Vive la France ! DLC content."""
    display_name = "DLC: France"
    default = 0

class DLC_Italia(Toggle):
    """Enables Vive la France ! DLC content."""
    display_name = "DLC: Italia"
    default = 0

class DLC_BalticSea(Toggle):
    """Enables Beyond the Baltic Sea DLC content."""
    display_name = "DLC: Baltic Sea"
    default = 0

class DLC_BlackSea(Toggle):
    """Enables Road to the Black Sea DLC content."""
    display_name = "DLC: Black Sea"
    default = 0

class DLC_Iberia(Toggle):
    """Enables Iberia DLC content."""
    display_name = "DLC: Iberia"
    default = 0

class DLC_WestBalkans(Toggle):
    """Enables West Balkans DLC content."""
    display_name = "DLC: West Balkans"
    default = 0

class DLC_Greece(Toggle):
    """Enables Greece DLC content."""
    display_name = "DLC: Greece"
    default = 0

class DLC_NordicHorizons(Toggle):
    """Enables Nordic Horizons DLC content."""
    display_name = "DLC: Nordic Horizons"
    default = 0

class MOD_PromodsEurope(Toggle):
    """Enables Promods Europe content."""
    display_name = "MOD: Promods Europe"
    default = 0

class Photosanity(Toggle):
    """Enables Photo Trophy content as locations."""
    display_name = "Photo Trophy"
    default = 0

class Viewpointsanity(Toggle):
    """Enables Viewpoint content as locations."""
    display_name = "Viewpoint"
    default = 0

class LocationScouts(Toggle):
    """Enables scouting any location."""
    display_name = "Location Scouts"
    default = 0

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["amount_to_win"] = AmountOfTokensNeeded
    options["randomize_starting_country"] = RandomizeStartingCountry
    options["enable_going_east"] = DLC_GoingEast
    options["enable_scandinavia"] = DLC_Scandinavia
    options["enable_vive_la_france"] = DLC_France
    options["enable_italia"] = DLC_Italia
    options["enable_beyond_the_baltic_sea"] = DLC_BalticSea
    options["enable_road_to_the_black_sea"] = DLC_BlackSea
    options["enable_iberia"] = DLC_Iberia
    options["enable_west_balkans"] = DLC_WestBalkans
    options["enable_greece"] = DLC_Greece
    options["enable_nordic_horizons"] = DLC_NordicHorizons
    options["enable_promods_europe"] = MOD_PromodsEurope
    options["enable_photosanity"] = Photosanity
    options["enable_viewpointsanity"] = Viewpointsanity
    options["enable_location_scouts"] = LocationScouts
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
