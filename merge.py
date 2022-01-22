#!/usr/bin/env python3
# Author: Teun Mathijssen
# Link: https://github.com/teuncm/batch_merge_channels
#
# Instructions: 
# 1) Put this entire folder next to your lab folders.
# 
# 2) This program requires numpy and Pillow to run.
#
# 3) Run the following command:
# python merge.py lab_folder [reverse]

import sys
import os
from pathlib import Path

import numpy as np
from PIL import Image

# Check number of arguments.
if len(sys.argv) < 2:
    print("Usage: python processing.py lab_folder [reverse]"); exit(1)
elif len(sys.argv) > 3:
    print("Error: too many arguments!"); exit(1)

# Set directories to operate in.
LAB_DIR = Path(sys.argv[1]+"/")
MERGE_DIR = Path(sys.argv[1]+"_merged/")

def lab_id(file_name):
    """Return the lab id of the given file name."""
    return file_name.rsplit('_', 1)[0]

def merge(f_green, f_blue):
    """Merge green channel of f_green with blue channel of f_blue."""
    print("Merge -", f_green, "(green),", f_blue, "(blue)")

    # Color channel indices.
    CHANNEL_R = 0; CHANNEL_G = 1; CHANNEL_B = 2

    # Open both lab images.
    lab_green = np.array(Image.open(LAB_DIR/f_green))
    lab_blue = np.array(Image.open(LAB_DIR/f_blue))

    # Merge greens of lab_green with blues of lab_blue. Discard reds.
    lab_merged = np.zeros(lab_green.shape, dtype=np.uint8)
    lab_merged[:, :, CHANNEL_G] = lab_green[:, :, CHANNEL_G]
    lab_merged[:, :, CHANNEL_B] = lab_blue[:, :, CHANNEL_B]

    f_merged = lab_id(f_green)+"_merged.jpg"

    print("Result -", f_merged)
    print("")

    # Save the merged image.
    Image.fromarray(lab_merged).save(Path(MERGE_DIR/f_merged))

def main():
    # Go back to the root folder.
    os.chdir(Path(".."))

    # Proceed only if the lab directory exists.
    if not os.path.isdir(LAB_DIR):
        print("Error: lab directory not found!"); exit(1)

    # Check if we need to reverse the sorting order.
    reverse = False
    if len(sys.argv) == 3:
        reverse = (sys.argv[2].lower() in ["reverse", "r"])

    # Sort everything. All lab pairs will end up next to eachother.
    lab_files = sorted([f for f in os.listdir(LAB_DIR) if os.path.isfile(LAB_DIR/f)], reverse=reverse)

    # We will make steps of two, so the total number of files needs to be even.
    if len(lab_files) % 2 != 0:
        print("Error: incorrect number of lab images!"); exit(1)

    # Make the merge directory.
    os.makedirs(MERGE_DIR, exist_ok=True)

    # Go through all lab pairs and merge the image channels.
    for i in range(0, len(lab_files), 2):
        f1 = lab_files[i]; f2 = lab_files[i+1]
        
        if not lab_id(f1) == lab_id(f2):
            print("Error: lab names don't match!", f1, f2); exit(1)

        merge(f1, f2)

    print("Done merge from", LAB_DIR, "to", MERGE_DIR)

if __name__ == '__main__':
    main()
