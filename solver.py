import os
import SimpleITK as sitk
import mritopng
import utils


class ImageSolver(object):
    def __init__(self, mode, input_path):
        self.mode = mode
        self.input_path = input_path

        return

    def process(self):
        print("current mode = {}".format(self.mode))
        if self.mode == 'dicom_to_nifti':
            self.dicom_to_nifti()

        elif self.mode == 'dicom_to_png':
            self.dicom_to_png()

        elif self.mode == 'nifti_to_dicom':
            self.nifti_to_dicom()

        elif self.mode == 'png_series_to_tfrecords':
            self.png_series_to_tfrecords()
        return

    def png_series_to_tfrecords(self):
        png_file_list = [os.path.join(self.input_path, file) for file in os.listdir(self.input_path) if
                         file.endswith(".png")]
        png_file_list.sort()
        # FIXME : update later

        base_tfrecords_name = os.path.join(self.input_path, "example.tfrecords")
        utils.png_to_tfrecords(png_file_list, base_tfrecords_name)

        print("Successfully make tfrecords in {}------------".format(base_tfrecords_name))
        return

    def dicom_to_nifti(self):
        print("current mode = {}".format(self.mode))
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
        print("current mode = {}".format(self.mode))
        # get dicom file list
        dcm_file_list = [file for file in os.listdir(self.input_path) if
                         file.endswith(".dcm")]

        dcm_file_list.sort()

        parent_path = self.input_path + "/../"

        png_dir_name = self.get_dir_name(self.input_path) + "toPng"

        # make new png dir with png name
        png_dir_path = os.path.join(parent_path, png_dir_name)
        utils.maybe_mkdir(png_dir_path)

        for dcm in dcm_file_list:
            dcm_name = dcm[:-4]

            png_name = dcm_name + ".png"

            # convert one dicom file to one png file
            mritopng.convert_file(os.path.join(self.input_path, dcm), os.path.join(png_dir_path, png_name),
                                  auto_contrast=True)

        return

    def nifti_to_dicom(self):
        print("current mode = {}".format(self.mode))
        pass

    def get_dir_name(self, dicom_path):
        split_path = dicom_path.split("/")

        if split_path[-1] == "":
            output_name = split_path[-2]
        else:
            output_name = split_path[-1]

        return output_name
