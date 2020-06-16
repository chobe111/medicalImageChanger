from micg.solver import ImageTransfer


def main():
    nii_data_path = "../sampleData/sample.nii.gz"
    transfer = ImageTransfer(nii_data_path)
    transfer.nii_to_dcm()


if __name__ == '__main__':
    main()
