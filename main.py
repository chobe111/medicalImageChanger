import argparse
from solver import ImageSolver
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

parser = argparse.ArgumentParser(description="ImageChanger")

parser.add_argument("--mode",
                    help="choose change mode \n ex) dicom_to_nifti ,"
                         " dicom_to_png, nifti_to_dicom, png_series_to_tfrecords")

parser.add_argument("--input", help="input your file loaction")

args = parser.parse_args()


def main():
    mode = args.mode
    input_path = args.input

    image_solver = ImageSolver(mode, input_path)
    image_solver.process()

    return


if __name__ == '__main__':
    main()
