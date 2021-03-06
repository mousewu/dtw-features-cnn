import dtw
import time
import numpy as np
import input_data
import network_settings as ns
import os
import csv


version = "1c"
# load settings
ns.load_settings_raw(version, "1d")
full_data_file = os.path.join("data", version + "-re-data.txt")
full_label_file = os.path.join("data", version + "-re-labels.txt")
# load data
data_sets = input_data.read_data_sets(full_data_file, full_label_file, ns.IMAGE_SHAPE, test_ratio=0.1,
                                      validation_ratio=0.0, pickle=False, boring=False)

no_classes = ns.NUM_CLASSES
# print(proto_number)

train_data = (data_sets.train.images.reshape((-1, 50, 2)) + 1.) * (127.5 / 127.)  # this input_data assumes images
train_labels = data_sets.train.labels

train_number = np.shape(train_labels)[0]
#dtw_matrix = np.zeros((train_number, train_number))
fileloc = os.path.join("data", version + "-dtw-matrix.txt")

with open(fileloc, 'w') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONE, delimiter=" ")
    for t1 in range(train_number):
        writeline = np.zeros((train_number))
        for t2 in range(train_number):
            writeline[t2] = dtw.dtw(train_data[t1], train_data[t2], extended=False)
        writer.writerow(writeline)
        print(t1)

#np.savetxt(os.path.join("data", "{}_dtw_matrix.txt".format(version)), dtw_matrix, delimiter=' ')