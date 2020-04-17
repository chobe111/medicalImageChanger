import argparse
from solver import ImageSolver

parser = argparse.ArgumentParser(description="ImageChanger")

parser.add_argument("--mode",
                    help="choose change mode \n ex) dicom_to_nifti ,"
                         " dicom_to_png, nifti_to_dicom, png_series_to_tfrecords")
parser.add_argument("--dicom_series_folder_path", help="input your dicom series folder loaction")

parser.add_argument("--nifti_file_path", help="input your nifti file loaction")

parser.add_argument("--png_series_folder_path", help="input your png series folder location")

args = parser.parse_args()


def main():
    mode = args.mode
    input_path = args.input_path
    output_path = args.output_path

    image_solver = ImageSolver(mode, input_path)
    image_solver.process()

    return


if __name__ == '__main__':
    main()
