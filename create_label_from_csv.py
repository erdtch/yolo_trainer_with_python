# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:01:33 2019

@author: SarachErudite
"""

import pandas as pd
import csv 
import os 

# format csv file columns = [filename, class_id, xmin, xmax, ymin, ymax]
label_csv = "label_boxes.csv"

label_df = pd.read_csv(label_csv)

label_dir = 'labels'

current_path = os.getcwd()

# format for text file <class> <x_center> <y_center> <width> <height>
for r in range(len(label_df)):
    row = label_df.iloc[r,:]
    img_name = row.filename
    
    file_path = os.path.join(current_path, label_dir, img_name).replace('.jpg', '.txt')
    
    clss = row.class_id
    xmin = row.xmin
    xmax = row.xmax
    ymin = row.ymin
    ymax = row.ymax

    x_cen = ((xmin + xmax)/2).values[0]
    y_cen = ((ymin + ymax)/2).values[0]
    width = (xmax-xmin).values[0]
    height = (ymax-ymin).values[0]
    
    with open(file_path, 'a') as csvFile:
        text_line = [clss, x_cen, y_cen, width, height]
        writer = csv.writer(csvFile, delimiter=' ')
        writer.writerow(text_line)
    csvFile.close()
    
print('Generate labels done, check your directory at :', os.path.join(current_path, label_dir))
    


