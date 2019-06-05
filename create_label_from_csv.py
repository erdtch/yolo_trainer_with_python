# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:01:33 2019

@author: SarachErudite
"""

import pandas as pd
import csv 
import os 

# format csv file columns = [filename, class_label, x, y, width, height]
label_csv = "label_boxes.csv"

label_df = pd.read_csv(label_csv)

label_dir = 'labels'

current_path = os.getcwd()

# format for text file <class> <x> <y> <width> <height>
for r in range(len(label_df)):
    row = label_df.iloc[r,:]
    img_name = row.filename
    
    file_path = os.path.join(current_path, label_dir, img_name).replace('.jpg', '.txt')
    
    clss = row.class_label
    x = row.x
    y = row.y
    w = row.width
    h = row.heigth
    
    with open(file_path, 'a') as csvFile:
        text_line = [clss, x, y, w, h]
        writer = csv.writer(csvFile, delimiter=' ')
        writer.writerow(text_line)
    csvFile.close()
    
print('Generate labels done, check your directory at :', os.path.join(current_path, label_dir))
    


