from micg.solver import ImageTransfer
import SimpleITK as sitk


def dicom_info_():
    reader = sitk.ImageSeriesReader()
    dicom_files = reader.GetGDCMSeriesFileNames('../sampleData')

    print(dicom_files)


def main():
    nii_data_path = "../sampleData/041s.nii.gz"
    transfer = ImageTransfer(nii_data_path)
    transfer.nii_to_dcm()
    # dicom_info_()


if __name__ == '__main__':
    main()
