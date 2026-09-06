from typing import Optional, Any
from BaseClasses import MultiWorld
MAP = {"Super Mario Kart":"SMK","Mario Kart 64":"MK64","Mario Kart Super Circuit":"MKSC","Mario Kart Double Dash!!":"MKDD","Mario Kart DS":"MKDS","Mario Kart Wii":"MKWii","Mario Kart 7":"MK7","Mario Kart 8":"MK8","Mario Kart World":"MKWld"}


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    from ..Helpers import get_option_value
    if "BCP" in item["category"] and not get_option_value(multiworld, player, "enable_booster_course_pass"):
        return False
    if any("MK" in i for i in item["category"]):
        enabled_games = list(get_option_value(multiworld, player, "enabled_games"))
        for i in range(len(enabled_games)):
            enabled_games[i] = MAP[enabled_games[i]]
        return any(games in i for i in item["category"] for games in enabled_games)  # True if they're in the yaml, false if they're not
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    from ..Helpers import get_option_value
    if "BCP" in location["category"] and not get_option_value(multiworld, player, "enable_booster_course_pass"):
        return False
    if "MK" in location["region"]:
        enabled_games = list(get_option_value(multiworld, player, "enabled_games"))
        for i in range(len(enabled_games)):
            enabled_games[i] = MAP[enabled_games[i]]
        return any(games in location["region"] for games in enabled_games)  # True if they're in the yaml, false if they're not
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
