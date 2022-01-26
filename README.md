### Batch merge image channels

Written for my gf's lab work. Batch merge a folder of red/green/blue stained cells (stained using PI/GFP/Hoechst/DAPI) like in ImageJ. Additionally, this repository contains ImageJ macros to adjust the contrast/brightness of a specific channel of the merged images.

#### Usage
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

Next, run the following command:
```
python merge.py input_folder [stain_order] [num_stains]
```

Example for 2 stains in folder G93A_0C:
```
python merge.py ../G93A_0C 012 2
```

For detailed help information:
```
python merge.py -h
```
