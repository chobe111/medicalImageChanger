import tensorflow as tf

import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def _float_feature(value):
    """Returns a float_list from a float / double."""
    return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))


def png_to_tfrecords(file_path_list, output_records_name):
    print("Try to make {} file....".format(output_records_name))

    writer = tf.python_io.TFRecordWriter(output_records_name)

    with tf.Session() as sess:
        save_file_name = output_records_name
        writer = tf.python_io.TFRecordWriter(save_file_name)

        for file in file_path_list:
            img = tf.read_file(file)
            img_bytes = sess.run(img)

            height = img.shape[0]
            width = img.shape[1]

            filename = file.split("/")
            filename = filename[-1][:-4]

            example = tf.train.Example(features=tf.train.Features(feature={
                'image/filename': _bytes_feature(filename),
                'image/encoded_image': _bytes_feature(img_bytes)
            }))

            writer.write(example.SerializeToString())

        writer.close()

    return
