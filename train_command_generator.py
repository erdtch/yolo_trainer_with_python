# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:25:58 2019

@author: SarachErudite
"""

import os 


"""
Config Training on GPU or Not. 
"""

GPU = True  # Set Training False = CPU, True = GPU
GPU_Card = [0,1]  # Number of your GPU [0,1,2,3]

"""
Select yolo version to train your can see at 'darknet/cfg'
"""
is_tiny = True 

yolo_cfg = 'custom_yolov3.cfg' # file are contain in 'darknet/cfg' 

tiny_yolo_weights = 'yolov3-tiny.weights'

"""
Where to store training-log 
"""
train_log = "train.log"

"""

Process code

""" 

current_path = os.getcwd() 

darknet_dir_path = os.path.join(current_path, 'darknet', '')
darknet_data_path = os.path.join(current_path, 'darknet.data')
pretained_net_path = "./darknet/darknet53.conv.74"
if is_tiny : 
    pretained_net_path = "./darknet/darknet53.conv.74"

cfg_path = os.path.join(current_path, 'cfg_data', yolo_cfg)
log_path = os.path.join(current_path, train_log)

command = "./darknet/darknet detector train "
command += darknet_data_path + " "
command += cfg_path + " "
command += pretained_net_path 
command += " > " + log_path

if GPU : 
    command += " -gpus " + str(GPU_Card).replace('[','').replace(']','').replace(' ','')

if is_tiny : 
    tiny_yolo_weights = os.path.join(current_path, 'darknet', tiny_yolo_weights)

    tiny_gen_command = "./darknet/darknet detector partial "
    tiny_gen_command += cfg_path + " "
    tiny_gen_command += tiny_yolo_weights + " "
    tiny_gen_command += "yolov3-tiny.conv.15 15"
    print('\n'*2+'*'*20)
    print('*'*20)
    print("Run this command to generate conv weights for tiny YOLO")
    print('*'*20 + '\n')

    print(tiny_gen_command)

print('\n'*2+'*'*20)
print("Run this command ")
print('*'*20 + '\n')

print(command)

print('\n'+'*'*20 + '\n')
print("Copy and run ...")

