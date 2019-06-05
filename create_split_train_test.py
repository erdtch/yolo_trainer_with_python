# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:41:24 2019

@author: SarachErudite
"""

import os 
import csv 
import numpy as np 

train_detail = 'train_list_images.txt'
valid_detail = 'test_list_images.txt'

split_train = 0.8 

img_dir = "JPEGImages"
list_img_name = os.listdir(img_dir)

list_img_name.append(1)
list_img_name = np.array(list_img_name)

train_list = list_img_name[:int(len(list_img_name)*split_train)]
valid_list = list_img_name[int(len(list_img_name)*split_train):]

img_dir_path = os.getcwd()

print("Create Training Set : ", len(train_list), 'samples. Saved at : ', train_detail)
with open(train_detail, 'a') as csvFile:
    writer = csv.writer(csvFile, delimiter=' ')
    for file in train_list : 
        img_path = os.join(img_dir_path, file)
        text_line = [img_path]
        writer.writerow(text_line)
csvFile.close()

print("Create Validate Set : ", len(valid_list), 'samples. Saved at : ', valid_detail)
with open(valid_list, 'a') as csvFile:
    writer = csv.writer(csvFile, delimiter=' ')
    for file in valid_list : 
        img_path = os.join(img_dir_path, file)
        text_line = [img_path]
        writer.writerow(text_line)
csvFile.close()


        