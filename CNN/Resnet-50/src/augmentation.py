#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:16:10 2020

@author: smg

This is module with image preprocessing utilities
"""

import os
import math
import random
from shutil import copyfile

from keras.preprocessing import image
from keras.preprocessing.image import  ImageDataGenerator
import matplotlib.pyplot as plt

# config
rotation_range      = 0
width_shift_range   = 0.2
height_shift_range  = 0.2
shear_range         = 0.2
zoom_range          = 0.2
img_reshape_flg     = False
img_reshape_w       = 224
img_reshape_h       = 224
target_class_cnt    = 1000
valid_ratio         = 0.2

class_lab_idx       = 0 # for class_label index
class_list          = ("ok","ng")
img_train_dir       = '../img/original'
img_gen_train_dir   = '../img/gen/train'
img_gen_valid_dir   = '../img/gen/valid'

random.seed(18)

# process by class
for class_lab in class_list:
    if(class_lab == ""): continue

    ''' pre-process '''
    # path define
    train_dir = '{}/{}'.format(img_train_dir, class_lab)        # training
    img_gen_train_saveas_dir = "{}/{}".format(img_gen_train_dir, class_lab) # genernate saveas
    img_gen_valid_saveas_dir = "{}/{}".format(img_gen_valid_dir, class_lab) # genernate saveas
    
    # chk folder exist
    if not os.path.isdir(img_gen_train_saveas_dir): os.makedirs(img_gen_train_saveas_dir)
    if not os.path.isdir(img_gen_valid_saveas_dir): os.makedirs(img_gen_valid_saveas_dir)
    
    # calculate image generate count
    fnames = [os.path.join(train_dir, fname) for fname in os.listdir(train_dir)] # file list
    img_gen_cnt = math.floor(target_class_cnt/len(fnames)) + 1
    valid_index = random.sample(range(len(fnames)-1), round(len(fnames)*valid_ratio))
    
    ''' Data augmentation '''
    # Data augmentation parameter
    datagen = ImageDataGenerator(rotation_range = 0, 		#角度值，表示图像随机旋转的角度
    							  width_shift_range = 0.2,	#图像在水平或者垂直方向上平移的范围
    							  height_shift_range = 0.2,
    							  shear_range = 0.2,		#随机错切变换的角度
    							  zoom_range = 0,			#图像随机缩放的范围  
    							  horizontal_flip = True, 	#随机将一般图像水平翻转   
    							  fill_mode = 'nearest') 	#用于填充新创建像素的方法
    
    
    # loop file
    img_idx = 0
    for img_name in os.listdir(train_dir):
        img_path = '{}/{}'.format(train_dir, img_name)
        
        # read image and reshape
        if(img_reshape_flg): img = image.load_img(img_path, target_size=(img_reshape_h, img_reshape_w)) # img(h, w)
        else: img = image.load_img(img_path)
            
        img = image.img_to_array(img) # reshape(x,x,3)
        img = img.reshape((1,) + img.shape) # reshape(1,x,x,3)
        
        if(img_idx in valid_index): img_gen_saveas_dir = img_gen_valid_saveas_dir # valid
        else: img_gen_saveas_dir = img_gen_train_saveas_dir # train
        
        # copy original image
        # copyfile(img_path, '{}/{}'.format(img_gen_saveas_dir, img_name))
        
        # image generate
        i = 0        
        for batch in datagen.flow(img, batch_size=10, save_to_dir=img_gen_saveas_dir, save_prefix=img_name[:-4], save_format='jpeg'): 
            if(i<img_gen_cnt-1): i+=1
            else: break
        
        img_idx += 1
        
    class_lab_idx += 1