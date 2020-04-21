import argparse
from solver import ImageTransfer
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

parser = argparse.ArgumentParser(description="ImageChanger")
parser.add_argument("--mode", help="medical_image_divide, image_transfer")
parser.add_argument("--submode", help="choose change mode \n ex) dcm_to_nii ,"
                                      " dcm_to_png, nii_to_dcm, png_series_to_tf_records")
parser.add_argument("--input", help="input your file loaction")
args = parser.parse_args()


def main():
    mode = args.mode
    sub_mode = args.submode
    input_path = args.input

    image_solver = ImageTransfer(mode, input_path)

    return


if __name__ == '__main__':
    main()
