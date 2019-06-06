# yolo_trainer_with_python

We created python scripts to generate all required files for training yolo with darknet.

# Quick Start

        git clone https://github.com/erdtch/yolo_trainer_with_python.git
        cd yolo_trainer_with_python

Create required directories(folders) :

        mkdir labels
        mkdir JPEGImages
        mkdir weights
    
Then put all images into folder : JPEGImages

Preprocessing Steps : 

Edit init_config.py to match to your data ***required***
      
        python init_config.py 

It will generate two files, ***"darknet.data"*** and ***"classes.name"***.

Let's create label and bounding box files from your CSV file. Which you have to set the columns into the format 

        [filename, class_id, xmin, xmax, ymin, ymax]    


Note  
    
    - filename column is in format "image01.jpg" (image name only !) and all images are in labels folder. 
    - x, y, width, height are in range [0,1] . 
    - class_label is in integer. 
    - 1 image can have more than 1 bounding box and class. 
    
Then, run  
      
        python create_label_from_csv.py

It will create 'image_name.txt' file which contain class(es) and bounding box(es) of each image. All label_files are in folder "labels".

Text files format :  
 
        [class_id, x_center, y_center, width, height]

Now, we need to split training samples and test samples. we will create from runing 

        python create_split_train_test.py 

It will create "train_list_images.txt" and "test_list_images.txt" which contain image_file_names to training set and test set.

Ok. We have done preprocessing process. let's get start with Yolo on Darknet !. 

Install Darknet and compile it.

        git clone https://github.com/pjreddie/darknet
        cd darknet
    
For runing on GPU you need to change some config on "Makefile", if not skip this.
    
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
        
Be sure that we are in ***"yolo_trainer_with_python/darknet"***. Now download pretained darknet network by running 
        
        wget https://pjreddie.com/media/files/darknet53.conv.74 -O darknet53.conv.74
        
On this step we are ready to train our model. Let's go back to ***"yolo_trainer_with_python"*** 
        
        cd ../

Edit some codes generator on ***"train_command_generator.py"*** which you can choose

        GPU = False / True      # False = CPU , True = GPU 
        GPU_Card = [0,1,2,3]    # Add number of GPU-Cards which you want to train model.

Before training choose your YOLO model by using ".cfg" you can see all .cfg files on  ***"yolo_trainer_with_python/cfg_data"*** and edit ***".cfg"*** file for some configurations.

        classes = 1     # number of your classes 

        Edit all lines about classes in ".cfg" file.

Choose your yolo version to train by change parameter on ***"train_command_generator.py"***

        yolo_cfg = 'yolov3.cfg'        # your Yolo version. this file must be in "yolo_trainer_with_python/cfg_data"


Then save it and run. 
        
        python train_command_generator.py 

Copy a command form the output and then run that command.

# Edit configurations on YOLO 

On the project we copied all cfg files into ***"yolo_trainer_with_python/cfg_data"***. In this folder you will see all ***".cfg"*** files which you can edit some configuration for training your model. 

        These are what you can edit on .cfg file for training your model.
                1. Batch hyper-parameter
                2. Subdivisions configuration
                3. Width , Height and Channels 
                4. Momentum and decay 
                5. Learning Rate, Steps, Scales, Burn In 
                6. Data augmentation
                7. Number of iterations
        Note : You have to edit class number on parameter "classes" in cfg file to match your classes.

You can see more details about YOLO configurations at ***TOPIC 6*** on this website: 

https://www.learnopencv.com/training-yolov3-deep-learning-based-custom-object-detector/  

Update and download new ***".cfg"*** files on this website :
https://pjreddie.com/darknet/yolo/

If you download new ".cfg" file, you have to put it in ***"yolo_trainer_with_python/cfg_data"***.

Save your edited cfg file at ***"yolo_trainer_with_python/cfg_data"*** and edit ***"train_command_generator.py"*** to choose tour cfg file then run 

        python train_command_generator.py 

Copy a command form the output and then run that command.

# Good Luck ! 

My power supplies just blow up while training on 2 GPUs 1080-Ti. Make sure that your have a warranty for your computer before training. 

# References 

Tutorial : 
https://www.learnopencv.com/training-yolov3-deep-learning-based-custom-object-detector/

Repo : 
https://github.com/spmallick/learnopencv/tree/master/YOLOv3-Training-Snowman-Detector
        


See more training detail on YOLO Website : 
https://pjreddie.com/darknet/yolo/

Darknet with improvements :
https://github.com/AlexeyAB/darknet

Label bounding box by yourself YOLO Mark GUI :
https://github.com/AlexeyAB/Yolo_mark

    
