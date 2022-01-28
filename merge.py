# Author: Teun Mathijssen
# Link: https://github.com/teuncm/batch_merge_channels
#
# Instructions: python merge.py -h

import sys
import argparse
import itertools
from pathlib import Path

import numpy as np
from PIL import Image

def lab_id(path):
    """Return lab id of file path."""
    return path.name.rsplit("_", 1)[0]

def merge(args, files_to_merge):
    """Merge stain channels into a new image."""
    print("MERGE")

    # Retrieve stain data.
    stain_data = []
    for stain_idx, f in enumerate(files_to_merge):
        stain_data.append(np.array(Image.open(f)))
        print(f"index {stain_idx+1}: {f.name}")

    print("")

    # Verify stain correctness.
    for a, b in itertools.combinations(files_to_merge, 2):
        if lab_id(a) != lab_id(b):
            print(f"IDs don't match!", file=sys.stderr); exit(1)

    # Merge channels in user indicated order.
    merged_data = np.zeros(stain_data[0].shape, dtype=np.uint8)
    for channel, stain_idx in enumerate(args.stain_order):
        stain_idx = int(stain_idx)

        if stain_idx > args.num_stains:
            print(f"Stain index {stain_idx} not found (max {args.num_stains})!", file=sys.stderr); exit(1)
        if stain_idx != 0:
            merged_data[:, :, channel] = stain_data[stain_idx-1][:, :, channel]

    # Save the merged stains.
    f_merged = lab_id(files_to_merge[0])+"_merged.jpg"
    Image.fromarray(merged_data).save(Path(args.merge_dir/f_merged))

def main():
    parser = argparse.ArgumentParser(
        description="Batch merge staining images like in ImageJ. Requires numpy and Pillow.")
    parser.add_argument("input_folder", type=str,
        help="Location of folder with lab images")
    parser.add_argument("stain_order", type=str, default="012", nargs="?",
        help="Stain RGB order (default 012) (0 here means: don't use the red channel)")
    parser.add_argument("num_stains", type=int, default=2, nargs="?",
        help="Number of stains used in lab (default 2)")
    args = parser.parse_args()

    # Create full path to lab folder and merge folder.
    args.lab_dir = Path.cwd()/Path(args.input_folder)
    args.merge_dir = Path.cwd()/Path(args.input_folder.rstrip("/").rstrip("\\")+"_merged")

    # Proceed only if lab folder exists.
    if not args.lab_dir.is_dir():
        print(f"Lab folder {args.input_folder} not found!", file=sys.stderr); exit(1)

    # Sort files in lab folder. All lab pairs will end up next to eachother by name.
    lab_files = [f for f in args.lab_dir.iterdir() if (args.lab_dir/f).is_file()]
    lab_files.sort(key=lambda p: str(p).casefold())

    # Verify number of files in lab folder.
    if len(lab_files) % args.num_stains != 0:
        print(f"Number of lab images needs to be a multiple of {args.num_stains}!", file=sys.stderr); exit(1)

    # Create merge folder.
    args.merge_dir.mkdir(exist_ok=True)

    # Go through all lab file groups and merge stain channels.
    for i in range(0, len(lab_files), args.num_stains):
        # Gather files to merge.
        files_to_merge = []
        for j in range(0, args.num_stains):
            files_to_merge.append(lab_files[i+j])

        merge(args, files_to_merge)

    print(f"Done merging! Merged images can be found in '{args.merge_dir.name}'.")

if __name__ == "__main__":
    main()