import cc_dat_utils
import os

#Part 1
file_path = os.path.dirname(os.path.abspath("pfgd_test.dat"))
input_dat_file = "data/pfgd_test.dat"

path = "/Users/naosw/OneDrive/Documents/Github/chips_tools/data/pfgd_test.dat"
# The path provided did not work so I had to manually enter the entire path

#Use cc_dat_utils.make_cc_level_pack_from_dat() to load the file specified by input_dat_file
#print the resulting data

print(cc_dat_utils.make_cc_level_pack_from_dat(path))
