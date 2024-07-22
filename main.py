import json

import webcolors


def get_colour_name(rgb_triplet):

    with open('colors.json', 'r') as f:
      myColors = json.load(f)

    min_colours = {}
    for name, hex_val in myColors.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(hex_val)
        rd = (r_c - rgb_triplet[0]) ** 2
        gd = (g_c - rgb_triplet[1]) ** 2
        bd = (b_c - rgb_triplet[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


rgb = (174,100,127)
closest_colorname = get_colour_name(rgb)
print(f'the closest color for RGB value {rgb} is {closest_colorname}')