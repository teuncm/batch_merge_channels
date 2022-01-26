### Batch merge image channels

Written for my gf's lab work. Batch merge a folder of red/green/blue stained cells (stained using PI/GFP/Hoechst/DAPI) like in ImageJ. Additionally, this repository contains ImageJ macros to adjust the contrast/brightness of a specific channel of the merged images.

#### Requirements
Works on Windows, macOS and Linux. Install numpy and Pillow, for example by using:
```
pip install numpy
pip install Pillow
```

#### Execution
Example for 2 stains in folder 'G93A_0C':
```
python merge.py ../G93A_0C 012 2
```

The following command is used:
```
python merge.py input_folder [stain_order] [num_stains]
```

For detailed help information:
```
python merge.py -h
```

#### Naming
Files in lab folders need to be named in groups for the program to run successfully.

Example for 2 stains:
```
D4_1_GFP.jpg
D4_1_H.jpg

D5_3_GFP.jpg
D5_3_H.jpg
```

Example for 3 stains:
```
D4_1_PI.jpg
D4_1_GFP.jpg
D4_1_H.jpg

D5_3_PI.jpg
D5_3_GFP.jpg
D5_3_H.jpg
```
