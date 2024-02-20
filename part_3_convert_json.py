import cc_dat_utils
import cc_classes
import json

# Part 3
# Load your custom JSON file
# Convert JSON data to CCLevelPack
# Save converted data to DAT file

# Load the JSON file
input_json_file = "data/naoswell_cc1.json"
with open(input_json_file, "r") as reader:
    level_json_data = json.load(reader)


def make_level_pack_from_json(json_data):
    level_pack = cc_classes.CCLevelPack()  # Make a blank level pack to put the levels into
    levels = json_data["levels"]
    for level in levels:  # Set the basic info for each level
        new_level = cc_classes.CCLevel()
        new_level.level_number = level["level_number"]
        new_level.time = level["time"]
        new_level.num_chips = level["num_chips"]
        new_level.upper_layer = level["upper_layer"]
        new_level.lower_layer = level["lower_layer"]

        optional_field_list = []
        for field in level["optional_fields"]:  # Determine which optional field is being seen
            if field["type_val"] == 3:
                title_field = cc_classes.CCMapTitleField(field["title"])
                optional_field_list.append(title_field)
            elif field["type_val"] == 6:
                password_field = cc_classes.CCEncodedPasswordField(field["password"])
                optional_field_list.append(password_field)
            elif field["type_val"] == 7:
                hint_field = cc_classes.CCMapHintField(field["hint"])
                optional_field_list.append(hint_field)
            elif field["type_val"] == 10:
                # This is made specifically for the list in json to be a 2D list of coordinates
                coord_field = []
                for coordinate in field["monsters"]:
                    monster_coordinate = cc_classes.CCCoordinate(coordinate[0], coordinate[1])
                    coord_field.append(monster_coordinate)
                monster_field = cc_classes.CCMonsterMovementField(coord_field)
                optional_field_list.append(monster_field)
        new_level.optional_fields = optional_field_list
        level_pack.add_level(new_level)
    return level_pack


# Convert level pack to actual DAT file
cc_dat_utils.write_cc_level_pack_to_dat(make_level_pack_from_json(level_json_data), "naoswell_cc1.dat")
