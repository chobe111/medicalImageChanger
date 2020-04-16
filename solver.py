import numpy as np
import nibabel as nib
import os
import SimpleITK as sitk


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
        pass

    def dicom_to_png(self):
        pass

    def nifti_to_dicom(self):
        pass
