# This script is for creating csv files from the CURE-TSD Dataset

# The CSV file should have the following format: path/to/image.jpg,xmin,ymin,xmax,ymax,label

import pandas as pd
import os
import csv

real = 1
#seqs = list(range(1, 50))
src = 0
chg = 0
lvl = 0


test_seq = [4, 5, 6, 7, 8, 18, 19, 21, 24, 26, 31, 38, 39, 41, 47]
train_seq = list(range(1, 50))

for s in test_seq:
    train_seq.remove(s)

test = True

if not (test):
    seqs = train_seq
    csv_path = 'csvFiles\\train.csv'
else:
    seqs = test_seq
    csv_path = 'csvFiles\\test.csv'

labels_dict = {
    1:'speed_limit',
    2:'goods_vehicle',
    3:'no_overtaking',
    4:'no_stopping',
    5:'no_parking',
    6:'stop',
    7:'bicycle',
    8:'hump',
    9:'no_left',
    10:'no_right',
    11:'priority_to',
    12:'no_entry',
    13:'yield',
    14:'parking'
}


frames_path = 'C:\\Data\\CURE-TSD\\frames'
labels_path = 'C:\\Data\\CURE-TSD\\labels'

first = True

with open(csv_path, 'w', newline = '') as file:
    #writer = csv.writer(file)
    for seq in seqs:
        vid = '%02d_%02d_%02d_%02d_%02d'%(real, seq, src, chg, lvl)
        label = '%02d_%02d.txt'%(real, seq)

        folder_path = os.path.join(frames_path, vid)
        label_path = os.path.join(labels_path, label)
        
        label_df = pd.read_csv(label_path, delimiter = '_')

        for row in label_df.iterrows():
            #print(row[1])
            frameNo = row[1]['frameNumber']
            img_path = os.path.join(folder_path, '%03d.jpg'%frameNo)
            xmin = row[1]['llx']
            ymin = row[1]['lly']
            xmax = row[1]['urx']
            ymax = row[1]['ury']
            label = row[1]['signType']
            label = labels_dict[label]
            if(first):
                first = False
            else:
                file.write('\n')
            str_data = '%s,%d,%d,%d,%d,%s'%(img_path, xmin, ymin, xmax, ymax, label)
            file.write(str_data)
            #break

        #print(label_df.head())

        #break