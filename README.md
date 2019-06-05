# yolo_trainer_with_python

# Quick Start

        git clone https://github.com/erdtch/yolo_trainer_with_python.git
        cd yolo_trainer_with_python

Create required directories(folders) :

        mkdir labels
        mkdir JPEGImages
        mkdir weights
    
Then put all images into folder : JPEGImages

Preprocessing Steps : 

edit init_config.py to match to your data ***required***
      
        python init_config.py 

It will generate two files, "darknet.data" and "classes.name".

Let's create label and bounding box files from your CSV file. Which you have to set the columns into the format 

    [filename, class_label, x, y, width, height]    


Note  
    
    - filename column is in format "image01.jpg" (image name only !) and all images are in labels folder. 
    - x, y, width, height are in range [0,1] . 
    - class_label is in integer. 
    - 1 image can have more than 1 bounding box and class. 
    
Then, run  
      
        python create_label_from_csv.py

It will create 'image_name.txt' file which contain class(es) and bounding box(es) of each image. All label_files are in folder "labels".

Now, we need to split training samples and test samples. we will create from runing 

        python create_split_train_test.py 

It will create "train_list_images.txt" and "test_list_images.txt" which contain image_file_names to training set and test set.

Ok. We have done preprocessing process. let's get start with Yolo on Darknet !. 

Install Darknet and compile it.

        git clone https://github.com/pjreddie/darknet
        cd darknet
    
for runing on GPU you need to change some config on "Makefile", if not skip this.
    
    1. edit GPU = 1 on top of the file 
    
        GPU=1
        CUDNN=0
        OPENCV=0
        OPENMP=0
        DEBUG=0 
    
    2. edit your cuda path 
    
        ifeq ($(GPU), 1) 
        COMMON+= -DGPU -I/usr/local/cuda/include/          # change to -/usr/local/cuda-10.0/include/
        CFLAGS+= -DGPU
        LDFLAGS+= -L/usr/local/cuda/lib64 -lcuda -lcudart -lcublas -lcurand  # change to -I/usr/local/cuda-10.0/include/
        endif
    
    3. save your "Makefile" and then run this command below
    
        export PATH=/usr/local/cuda-10.0/bin:$PATH

After edit "Makefile" follow the steps. 

If you don't have GPU and CUDA, you can skip to this step. (after clone darknet repo). 

        make 
        
Be sure that we are in "yolo_trainer_with_python/darknet". Now download pretained darknet network by running 
        
        wget https://pjreddie.com/media/files/darknet53.conv.74 -O darknet53.conv.74
        
On this step we are ready to train our model. 

# To be continue ..., I'm lazy to tell you more. Bye ! 

# References 
Tutorial : 

https://www.learnopencv.com/training-yolov3-deep-learning-based-custom-object-detector/

Repo : 

https://github.com/spmallick/learnopencv/tree/master/YOLOv3-Training-Snowman-Detector
        
 
YOLO Website : 

https://pjreddie.com/darknet/yolo/


    
