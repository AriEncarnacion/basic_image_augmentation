# Baic Image Augmentation with PILLOW (PIL)
This script transforms JPEG images. Options include horizontal flip, vertical flip, and rotation.

## Setup
Please ensure you have Python interpreter version 3.7.6 or later installed on your system. You can check this via:
```
$Python3 --version
```
or
```
$Python --version
```
depending on your environment.

This script also requires the PILLOW Python package. Please see how to install the package here
https://pillow.readthedocs.io/en/stable/installation.html

Depending on your environment, you may need to install the following modules:
```
sys
os
Path (from the pathlib package)
```

## Running the script
Run the script with Python interpreter 3.7.6 or later.
Pass the desired directory as an argument.

Example usage:
```
$Python3 augment.py ./myDirectory/
```

**Important notes:** 
- This script only works on JPEG images with extensions `.jpg` or `.JPG`.
- Rotations should be done in increments of 90 degrees. Any other rotation aount will result in large black bars on the sides of the images. These bars can affect your model when training.

Example output:
```
horizontal flip [y/n]?: y
vertical_flip [y/n]?: y
rotation [y/n]?: y 
Enter amount of rotation in degrees: 90

PathToImage/myImage.jpg y y y 90
flipping horizontally...
flipping vertically...
rotating 90 degrees...
.
.
.
```

The augmented images will be saved in the `augmented_photos` directory. The image names will have the augmentations appended. In the above example, the saved image would be `myImage_h_v_r90.jpg`.
