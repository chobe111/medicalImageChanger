import os
import SimpleITK as sitk
import mritopng
from micg import utils
import time
import numpy as np
from medicallogger import MedicalLogger
import datetime
from PIL import Image


class ImageTransfer(object):
    def __init__(self, input_path):
        self.mode_info = dict()
        self.__init_logger()
        self.input_path = input_path

    def _set_itk_file_writer(self):
        self.writer = sitk.ImageFileWriter()
        self.writer.KeepOriginalImageUIDOn()

        return

    def __init_logger(self):
        self.logger = MedicalLogger(__name__)

        self.logger.add_stream_handler("INFO")

        current_time = datetime.datetime.today()
        file_name = current_time.strftime("%Y-%m-%d") + ".log"
        file_path = os.path.join(self.input_path, file_name)

        self.logger.add_file_handler(file_path, "w", "INFO")

        self.logger = self.logger()

    def png_series_to_tf_records(self):
        png_file_list = [os.path.join(self.input_path, file) for file in os.listdir(self.input_path) if
                         file.endswith(".png")]

        png_file_list.sort()

        tf_records_name = utils.get_folder_name(self.input_path)
        tf_records_name += ".tfrecords"

        base_tf_records_name = os.path.join(self.input_path, tf_records_name)
        utils.png_to_tf_records(png_file_list, base_tf_records_name)

        self.logger.info("Successfully make tf_records in {}------------".format(base_tf_records_name))

    def dcm_to_nii(self):
        reader = sitk.ImageSeriesReader()

        dcm_names = reader.GetGDCMSeriesFileNames(self.input_path)
        reader.SetFileNames(dcm_names)
        image = reader.Execute()

        writer = sitk.ImageFileWriter()
        writer.SetImageIO("NiftiImageIO")

        output_path = self._get_nii_output_path()

        writer.SetFileName(output_path)
        writer.Execute()

        self.logger.info(" --- Successfully make new nii file in {} --- ".format(output_path))

    def dcm_to_png(self, input_path):
        # get dcm file list
        dcm_file_list = [file for file in os.listdir(self.input_path) if
                         file.endswith(".dcm")]

        dcm_file_list.sort()

        parent_path = self.input_path + "/../"

        png_dir_name = utils.get_dir_name(self.input_path) + "toPng"

        # make new png dir with png name
        png_dir_path = os.path.join(parent_path, png_dir_name)

        utils.maybe_mkdir(png_dir_path)

        for dcm in dcm_file_list:
            dcm_name = dcm[:-4]
            png_name = dcm_name + ".png"
            # convert one dcm file to one png file
            dcm_path = os.path.join(input_path, dcm)
            png_path = os.path.join(png_dir_path, png_name)

            mritopng.convert_file(dcm_path, png_path, auto_contrast=True)

        self.logger.info("--- Successfully process dcm to png your new file created at {} ---".format(png_dir_path))

    def combine_png(self, output_path, img1_dir_path, img2_dir_path):
        img1_png_list = [os.path.join(img1_dir_path, file) for file in os.listdir(img1_dir_path) if
                         file.endswith(".png")]
        img2_png_list = [os.path.join(img2_dir_path, file) for file in os.listdir(img2_dir_path) if
                         file.endswith(".png")]

        img1_png_list.sort()
        img2_png_list.sort()

        assert len(img1_png_list) == len(img2_png_list)
        cnt = 0
        for ct, mri in zip(img1_png_list, img2_png_list):
            images = [Image.open(x) for x in [ct, mri]]
            widths, heights = zip(*(i.size for i in images))

            total_width = sum(widths)
            max_height = max(heights)

            new_im = Image.new('L', (total_width, max_height))

            x_offset = 0
            for im in images:
                new_im.paste(im, (x_offset, 0))
                x_offset += im.size[0]

            new_name = utils.get_name(ct)

            new_im.save(os.path.join(output_path, '{}.png').format(new_name))
            cnt += 1

    def nii_to_dcm(self):
        nii = sitk.ReadImage(self.input_path)
        img = sitk.GetArrayFromImage(nii)

        img = img.astype(np.int32)

        new_img = sitk.GetImageFromArray(img)
        img_depth = new_img.GetDepth()

        direction = new_img.GetDirection()
        series_tag_values = utils.get_series_tag_values(direction)

        nii_file_name = utils.get_folder_name(self.input_path)

        output_path = self.input_path + "/../"

        for i in range(new_img):
            self.writeSlices(series_tag_values, new_img, i, output_path, nii_file_name)

        self.logger.info(" --- Successfully make new dicom series!! in {} --- ".format(output_path))

    def writeSlices(self, series_tag_values, new_img, i, output_path, base_name):
        image_slice = new_img[:, :, i]
        #     Tags shared by the series.
        list(map(lambda tag_value: image_slice.SetMetaData(tag_value[0], tag_value[1]), series_tag_values))
        # Slice specific tags.
        image_slice.SetMetaData("0008|0012", time.strftime("%Y%m%d"))  # Instance Creation Date
        image_slice.SetMetaData("0008|0013", time.strftime("%H%M%S"))  # Instance Creation Time

        # Setting the type to CT preserves the slice location.
        image_slice.SetMetaData("0008|0060", "CT")  # set the type to CT so the thickness is carried over
        # (0020, 0032) image position patient determines the 3D spacing between slices.

        image_slice.SetMetaData("0020|0032", '\\'.join(
            map(str, new_img.TransformIndexToPhysicalPoint((0, 0, i)))))  # Image Position (Patient)
        image_slice.SetMetaData("0020,0013", str(i))  # Instance Number

        #     # Write to the output directory and add the extension dcm, to force writing in DICOM format.
        self.writer.SetFileName(os.path.join(output_path, base_name + str(i) + '.dcm'))
        self.writer.Execute(image_slice)

    def _get_nii_output_path(self):
        folder_name = utils.get_folder_name(self.input_path)

        nii_file_name = os.path.join(self.input_path, folder_name + "nii.gz")

        return nii_file_name
