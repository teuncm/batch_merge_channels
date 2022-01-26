### Batch merge image channels

Written for my gf's lab work. Batch merge a folder of green/blue colored cells (stained using GFP/Hoechst/DAPI) like in ImageJ. Additionally, this repository contains an ImageJ macro to adjust the green channel (GFP) contrast/brightness of the merged images.

#### Usage
Download this repository and put it next to your lab folders.

Files in lab folders need to be named in pairs for the program to run successfully. Example:
```
W1_G93A_D4_1_GFP.jpg
W1_G93A_D4_1_H.jpg

W1_G93A_D5_3_GFP.jpg
W1_G93A_D5_3_H.jpg
```

Run the following command:
```
python merge.py lab_folder [reverse]
```
