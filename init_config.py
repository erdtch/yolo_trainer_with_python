# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:55:29 2019

@author: SarachErudite
"""

import os
import csv

"""

Config Parameter

"""

# list class label sort by number 
class_number = 1 
class_label = ['snowman']
classes_file = 'classes.name'


# list images to training set and test set 
train_detail = 'train_list_images.txt'
valid_detail = 'test_list_images.txt'

# where to keep '.weights' files
weights_dir = 'weights'

"""

Process code 

"""

# Create class detail file
with open(classes_file, 'a') as csvFile:
    for name in class_label :
        row = [name]
        writer = csv.writer(csvFile, delimiter=' ')
        writer.writerow(row)
    csvFile.close()

current_path = os.getcwd()
train_path = os.path.join(current_path, train_detail)
test_path = os.path.join(current_path, valid_detail)
class_path = os.path.join(current_path, classes_file)
weights_path = os.path.join(current_path, weights_dir, '')

#Create darknet.data files
 
text = 'classes = ' + str(class_number) + '\n'
text += 'train = ' + train_path + '\n' 
text += 'valid = ' + test_path + '\n'
text += 'names = ' + class_path + '\n'
text += 'backup = ' + weights_path + '\n'

with open("darknet.data", 'w') as text_file:
    text_file.write(text)
