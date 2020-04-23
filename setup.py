from setuptools import setup, find_packages

setup(
    name='micg',
    version="1.1.0",
    description="Medical Image Changer",
    author="Myung Ki Cho",
    author_email="chobe0719@gmail.com",
    url="https://github.com/chobe111/medicalImageChanger.git",
    install_requires=[
        "tensorflow>=1.14.0",
        "SimpleITK>=1.2.4",
        "Pillow>=7.1.1",
        "mritopng==2.2",
    ],
    entry_points={
        'console_scripts': [
            'micg_d2n = micg.image_transfer:dicom_to_nifti',
            'micg_n2d = micg.image_transfer:nii_to_dicom',
            'micg_combine_png = micg.image_transfer:combine_png',
            'micg_d2p = micg.image_transfer:dicom_to_png',
            'micg_png_to_tfrecords = micg.image_transfer:png_series_to_tf_records'
        ],
    },

    packages=find_packages(exclude=['test_jupyter/', 'venv/']),
    keywords=["medical image", "image change"],
    python_requires='>=3',
    zip_safe=False
)
