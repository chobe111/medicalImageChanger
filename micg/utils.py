import tensorflow as tf
import os
import warnings
import time

warnings.simplefilter(action='ignore', category=FutureWarning)


def get_folder_name(path: str) -> str:
    path = path.split("/")
    folder_name = path[-1]

    return folder_name


def get_name(path):
    name = path.split("/")
    return name[-1]


def get_dir_name(dcm_path):
    split_path = dcm_path.split("/")

    if split_path[-1] == "":
        output_name = split_path[-2]
    else:
        output_name = split_path[-1]

    return output_name


def _bytes_feature(value: str) -> bytearray:
    """
    :param value = string or byte
    :return byte list
    """
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def _int64_feature(value):
    """

    :param value: bool / enum / int / uint
    :return: int64 list
    """
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def get_series_tag_values(direction):
    modification_time = time.strftime("%H%M%S")
    modification_date = time.strftime("%Y%m%d")

    series_tag_values = [("0008|0031", modification_time),  # Series Time
                         ("0008|0021", modification_date),  # Series Date
                         ("0008|0008", "DERIVED\\SECONDARY"),  # Image Type
                         ("0020|000e", "1.2.826.0.1.3680043.2.1125." + modification_date + ".1" + modification_time),
                         # Series Instance UID
                         ("0020|0037",
                          '\\'.join(map(str, (direction[0], direction[3], direction[6],  # Image Orientation (Patient)
                                              direction[1], direction[4], direction[7])))),
                         ("0008|103e", "Created-SimpleITK")]  # Series Description

    return series_tag_values


def _float_feature(value):
    """

    :param value: float double
    :return: float list
    """

    return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))


def maybe_mkdir(path):
    if os.path.isdir(path):
        return

    os.mkdir(path)


def png_to_tf_records(file_path_list, output_records_name):
    """

    :param file_path_list: png file list
    :param output_records_name: output tensor flow records name
    :return:
    """
    print("Try to make {} file....".format(output_records_name))

    writer = tf.python_io.TFRecordWriter(output_records_name)

    with tf.Session() as sess:
        save_file_name = output_records_name
        writer = tf.python_io.TFRecordWriter(save_file_name)

        for file in file_path_list:
            img = tf.read_file(file)
            img_bytes = sess.run(img)
            filename = file.split("/")
            filename = filename[-1][:-4]

            example = tf.train.Example(features=tf.train.Features(feature={
                'image/file_name': _bytes_feature(filename.encode()),
                'image/encoded_image': _bytes_feature(img_bytes)
            }))

            writer.write(example.SerializeToString())

        writer.close()

    return
