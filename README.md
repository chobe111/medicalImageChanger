

![title](./title.png)

 # Medical Image Changer
-  **medical image changer** is a tool designed to make transformation    between medical images easier for developers. This library will provide many functions including **dicom_series_to_png_series**,  **png_series_to_tf_records**, **combine_png**,  **dicom_series to nifit**, **nifti_to_dicom_series**


# Installation
- Use Pip install
	1. install migc using pip (current version is 1.1.0)
	```
	pip install micg
	```
	after installing migc you may use console scripts


# Console scripts
- Change Dicom series to png series
	```
	micg_d2p INPUT_DICOM_SERIES_PATH 
	```
	if your input dicom series path is  
	 **path/to/dicom/**
	then your output png seires path is 
	**path/to/dicomtoPng/**
	

- Change Png Series to tfrecords 
	```
	micg_png_to_tfrecords INPUT_PNG_SERIES_PATH
	```
	if your input png series path is 
	**path/to/png**/
	then your output tensorflow records will save in 
	**path/to/png/~.tfrecords**

- Change nifti file to Dicom Series
	```
	micg_n2d INPUT_NIFTI_FILE_PATH
	```
	if your input nifti file path is
	 **path/to/your/niftifile(file)**
	then your output dicomSeries folder will be generated in **path/to/your/niftifile_name(dir)/.dicom**

- Change Dicom series to nifti file
	```
	micg_d2n INPUT_DICOM_SERIES_DIR_PATH
	```
	if your input dicom series path is
	**path/to/your/dicom_series(dir)**
	then your output  nifti file will be generated in
	**path/to/your/dicom_sereis(dir)/dicom_series(dir)_name.nii.gz**

- Combine two png files to a paired png (same size)
	```
	micg_combine_png OUTPUT_DIR_PATH IMAGE1_INPUT_PATH IMAGE2_INPUT_PATH
	```
	Input Path : path to your png series dir
	Output Path : write path you wanted to save

### Directory Hierarchy
```
│   medicalImageChanger
│   ├── micg
│   │   ├── __init__.py
│   │   ├── image_transfer.py
│   │   ├── medicallogger.py
│   │   ├── solver.py
│   │   ├── utils.py
│   ├── setup.py
│   ├── requirements.txt
│   ├── LICENSE
```
