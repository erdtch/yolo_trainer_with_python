# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:41:24 2019

@author: SarachErudite
"""

import os 
import csv 
import numpy as np 
import init_config 

train_detail = init_config.train_detail
valid_detail = init_config.valid_detail

split_train = 0.8 

img_dir = "JPEGImages"
list_img_name = os.listdir(img_dir)

list_img_name.append(1)
list_img_name = np.array(list_img_name)

train_list = list_img_name[:int(len(list_img_name)*split_train)]
valid_list = list_img_name[int(len(list_img_name)*split_train):]

img_dir_path = os.getcwd()
img_dir_path = os.path.join(img_dir_path, "JPEGImages")


print("Create Training Set : ", len(train_list), 'samples. Saved at : ', train_detail)
with open(train_detail, 'a', newline='') as csvFile:
    writer = csv.writer(csvFile, delimiter=' ', dialect= csv.unix_dialect, quoting=csv.QUOTE_NONE)
    for file in train_list : 
        img_path = os.path.join(img_dir_path, file)
        text_line = [img_path]
        writer.writerow(text_line)
csvFile.close()

print("Create Validate Set : ", len(valid_list), 'samples. Saved at : ', valid_detail)
with open(valid_detail, 'a', newline='') as csvFile:
    writer = csv.writer(csvFile, delimiter=' ', dialect= csv.unix_dialect, quoting=csv.QUOTE_NONE)
    for file in valid_list : 
        img_path = os.path.join(img_dir_path, file)
        text_line = [img_path]
        writer.writerow(text_line)
csvFile.close()

# txt_file = open(train_detail, "w+")
# for file in train_list : 
#     img_path = os.path.join(img_dir_path, file)
#     txt = img_path
#     txt_file.write(txt)
# txt_file.close()

# txt_file = open(valid_detail, "w+")
# for file in valid_list : 
#     img_path = os.path.join(img_dir_path, file)
#     txt = img_path
#     txt_file.write(txt)
# txt_file.close()
