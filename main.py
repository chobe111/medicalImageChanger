import argparse
from solver import ImageSolver

parser = argparse.ArgumentParser(description="ImageChanger")

parser.add_argument("--mode", help="choose change mode \n ex) dicom_to_nifti , dicom_to_png, 'nifti_to_dicom' ")
parser.add_argument("--input_path", help=" path/to/you/want/input ")

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
