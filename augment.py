from PIL import Image, ImageOps
import sys
import os
import ntpath


def augment_image(__img_file, __img, __horiz, __vert, __rot, __rot_angle):
    print(__img_file, __horiz, __vert, __rot, __rot_angle)

    file_path = ntpath.basename(__img_file)
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
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def validate_opt(opt_name):
    in_msg = opt_name + " [y/n]?: "
    opt = input(in_msg)
    while opt != 'y' and opt != 'Y' and opt != 'n' and opt != 'N':
        print("Please enter a valid option.")
        opt = input(in_msg)
    return opt


img_file = str(sys.argv[1])
horiz = validate_opt("horizontal flip")
vert = validate_opt("vertical_flip")
rot = validate_opt("rotation")
rot_angle = 0
if rot == 'y' or rot == 'Y':
    rot_angle = input("Enter amount of rotation in degrees: ")


img = Image.open(img_file)
augment_image(img_file, img, horiz, vert, rot, rot_angle)

# TODO:
#  Implement multi-photo augmentation
#  Implement program execution on any directory
