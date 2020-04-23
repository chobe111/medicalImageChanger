import argparse
from micg.solver import ImageTransfer



def get_args():
    parser = argparse.ArgumentParser("image_transfer")
    parser.add_argument("input_path")
    args = parser.parse_args()
    transfer = ImageTransfer(args.input_path)
    return args, transfer


def dicom_to_png():
    args, transfer = get_args()
    transfer.dcm_to_png(args.input_path)


def png_series_to_tf_records():
    args, transfer = get_args()
    transfer.png_series_to_tf_records()


def dicom_to_nifti():
    args, transfer = get_args()
    transfer.dcm_to_nii()


def combine_png():
    combine_parser = argparse.ArgumentParser("Combine parser")
    combine_parser.add_argument("output_path")
    combine_parser.add_argument("image1_dir_path")
    combine_parser.add_argument("image2_dir_path")

    args = combine_parser.parse_args()

    base_output_path = args.output_path
    img1_input_path = args.image1_dir_path
    img2_input_path = args.image2_dir_path
    transfer = ImageTransfer(None)
    transfer.combine_png(base_output_path, img1_input_path, img2_input_path)


def nii_to_dicom():
    args, transfer = get_args()
    transfer.nii_to_dcm()
