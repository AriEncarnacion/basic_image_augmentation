# Baic Image Augmentation with PILLOW (PIL)
This script transforms images. Options include horizontal flip, vertical flip, and rotation.

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


## Running the script
Run the script with Python interpreter 3.7.6 or later.
Pass the desired image as an argument.

Example usage:
```
$Python3 augment.py myImage.jpg
```

The program will then prompt you for the desired augmentations.
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
```

The augmented image will then be saved in the `augmented_photos` directory. The image name will have the augmentations appended to the filename. In the above example, the saved image would be `myImage_h_v_r90.jpg`.