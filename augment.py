from PIL import Image, ImageOps
import sys
import os
from pathlib import Path

def augment_image(__img_file, __img, __horiz, __vert, __rot, __rot_angle):
    print(__img_file, __horiz, __vert, __rot, __rot_angle)

    file_path = os.path.basename(__img_file)
    save_name = os.path.splitext(path_name(file_path))[0]
    augment_list = ''
    aug_img = __img

    if __horiz == 'y' or __horiz == 'Y':
        print("flipping horizontally...")
        augment_list += '_h'
        aug_img = ImageOps.mirror(aug_img)

    if __vert == 'y' or __vert == 'Y':
        print("flipping vertically...")
        augment_list += '_v'
        aug_img = ImageOps.flip(aug_img)

    if __rot == 'y' or __rot == 'Y':
        print("rotating", __rot_angle, "degrees...")
        rot_attb = '_r' + str(__rot_angle)
        augment_list += rot_attb
        aug_img = aug_img.rotate(int(__rot_angle)*-1, expand=True)

    save_path = 'augmented_photos/' + save_name + augment_list + '.jpg'
    aug_img.save(save_path, quality=95)


def path_name(path):
    head, tail = os.path.split(path)
    return tail or os.path.basename(head)


def validate_opt(opt_name):
    in_msg = opt_name + " [y/n]?: "
    opt = input(in_msg)
    while opt != 'y' and opt != 'Y' and opt != 'n' and opt != 'N':
        print("Please enter a valid option.")
        opt = input(in_msg)
    return opt


def process_imgs_in_dir(dir_path):
    files = Path(dir_path)
    for file in files.iterdir():
        if file.suffix == '.jpg' or file.suffix == '.JPG':
            print("Processing:",file.name)
            img = Image.open(file)
            augment_image(file.name, img, horiz, vert, rot, rot_angle)
        else:
            print(file.name, "was not an image file. Skipping...")
        

dir_path = str(sys.argv[1])
horiz = validate_opt("horizontal flip")
vert = validate_opt("vertical_flip")
rot = validate_opt("rotation")
rot_angle = 0
if rot == 'y' or rot == 'Y':
    rot_angle = input("Enter amount of rotation in degrees: ")

process_imgs_in_dir(dir_path)
