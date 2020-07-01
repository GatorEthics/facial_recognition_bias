"""File for sorting the data"""

import os
import cv2
from glob import glob

path = "../data/crop_part1"


def preprocess_filenames(path):
    data = os.listdir(path)
    files = []
    for file_name in data:
        files.append(file_name.split('_'))
    return files

processed_files  = preprocess_filenames(path)

def filter_file_names(age, gender, ethnicity):
    filtered = []
    for file_name in processed_files:
        if age != '-' and gender != '-' and ethnicity != '-':
            if file_name[0] == age and file_name[1] == gender and file_name[2] == ethnicity:
                filtered.append('_'.join(file_name))
        if age == '-' and gender == '-':
            if file_name[2] == ethnicity :
                filtered.append('_'.join(file_name))
        if age == '-' and ethnicity == '-':
            if file_name[1] == gender :
                filtered.append('_'.join(file_name))
        if gender == '-' and ethnicity == '-':
            if file_name[0] == age :
                filtered.append('_'.join(file_name))
        if age == '-':
            if file_name[1] == gender and file_name[2] == ethnicity :
                filtered.append('_'.join(file_name))
        if gender == '-':
            if file_name[0] == age and file_name[2] == ethnicity :
                filtered.append('_'.join(file_name))
        if ethnicity == '-':
            if file_name[0] == age and file_name[1] == gender :
                filtered.append('_'.join(file_name))
    return filtered

# Please refer the labels in README.md, if you don't want to use label put dash
#instead of a number
filtered  = filter_file_names('-','1', '-')


# 
# def filter_images(filtered_names,path):
#     image_list = []
#     data_path = os.path.join(path,"*.jpg")
#     filenames = glob(data_path)
#     for name in filtered_names:
#         for file_name in filenames:
#             if name in file_name:
#                 img = cv2.imread( file_name)
#                 image_list.append((img,name))
#
#     return image_list
#     #return image_list
#
#
# filtered_images = (filter_images(filtered,path))
#
# path_to_classified = '../data/female'
# for i in filtered_images:
#     print(i)
#     for img,name in i:
#         cv2.imwrite(os.path.join(path_to_classified , "{}".format(name)), img)