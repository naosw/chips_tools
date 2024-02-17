import cc_dat_utils
import cc_classes
import json

#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file

#load
input_json_file = "data/naoswell_cc1.json"
with open(input_json_file, "r") as reader:
    level_json_data = json.load(reader)


def make_level_pack_from_json( json_data ):
    level_pack = cc_classes.CCLevelPack()
    levels = json_data["levels"]
    for level in levels:
        new_level = (cc_classes.CCLevel())
        new_level.level_number = level["level_number"]
        new_level.time = level["time"]
        new_level.num_chips = level["num_chips"]
        new_level.upper_layer = level["upper_layer"]
        new_level.lower_layer = level["lower_layer"]
        new_level.optional_fields = level["optional_fields"]
        level_pack.add_level(new_level)
    return level_pack

#convert
cc_dat_utils.write_cc_level_pack_to_dat(make_level_pack_from_json( level_json_data ),"naoswell_cc1.dat")