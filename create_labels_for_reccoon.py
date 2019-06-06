import pandas as pd
import csv 
import os 

# format csv file columns = [filename, class_id, xmin, xmax, ymin, ymax]
label_csv = "raccoon_labels.csv"

label_df = pd.read_csv(label_csv)

label_dir = 'labels'

current_path = os.getcwd()

label_df['xmin'] = label_df['xmin']/label_df['width'] 
label_df['xmax'] = label_df['xmax']/label_df['width']
label_df['ymin'] = label_df['ymin']/label_df['height']
label_df['ymax'] = label_df['ymax']/label_df['height']

label_df = label_df.replace("raccoon", 0)

# format for text file <class> <x_center> <y_center> <width> <height>
for r in range(len(label_df)):
    row = label_df.iloc[r,:]
    img_name = row.filename
    
    file_path = os.path.join(current_path, label_dir, img_name).replace('.jpg', '.txt')
    
    clss = row['class']
    xmin = row.xmin
    xmax = row.xmax
    ymin = row.ymin
    ymax = row.ymax

    x_cen = ((xmin + xmax)/2)
    y_cen = ((ymin + ymax)/2)
    width = (xmax-xmin)
    height = (ymax-ymin)
    
    with open(file_path, 'a', newline='') as csvFile:
        text_line = [clss, x_cen, y_cen, width, height]
        writer = csv.writer(csvFile, delimiter=' ', dialect= csv.unix_dialect, quoting=csv.QUOTE_NONE)
        writer.writerow(text_line)
    csvFile.close()
    
print('Generate labels done, check your directory at :', os.path.join(current_path, label_dir))

