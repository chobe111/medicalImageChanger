import numpy as np
import nibabel as nib
import os
import SimpleITK as sitk
import mritopng


class ImageSolver(object):
    def __init__(self, mode, input_path):
        self.mode = mode
        self.input_path = input_path

        return

    def process(self):
        if self.mode == 'dicom_to_nifti':
            self.dicom_to_nifti()

        elif self.mode == 'dicom_to_png':
            self.dicom_to_png()

        elif self.mode == 'nifti_to_dicom':
            self.nifti_to_dicom()

        return

    def dicom_to_nifti(self):
        reader = sitk.ImageSeriesReader()

        dicom_names = reader.GetGDCMSeriesFileNames(self.input_path)
        reader.SetFileNames(dicom_names)
        image = reader.Execute()

        writer = sitk.ImageFileWriter()
        writer.SetImageIO("NiftiImageIO")

        output_path = self.get_nifti_output_path(self.input_path)

        writer.SetFileName(output_path)
        writer.Execute()

        print(" --- Successfully make new nifti file!! --- ")
        pass

    def dicom_to_png(self):
        dcm_file_list = [file for file in os.listdir(self.input_path) if file.endswith(".dcm")]
        dcm_file_list.sort()

        for dcm in dcm_file_list:
            dcm_name = dcm[:-4]

            if os.path.isfile(os.path.join(self.input_path, dcm_name + ".png")):
                continue
            mritopng.convert_file(os.path.join(self.input_path, dcm), os.path.join(self.input_path, dcm_name + ".png"),
                                  auto_contrast=True)

        pass

    def nifti_to_dicom(self):
        pass

    def get_nifti_output_path(self, dicom_path):

        split_path = dicom_path.split("/")

        if split_path[-1] == "":
            output_name = split_path[-2]
        else:
            output_name = split_path[-1]

        print("--- Try Make new {}.nii.gz file in nifti_data folder ---".format(output_name))

        return os.path.join("nifti_data", output_name + ".nii.gz")
