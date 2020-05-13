# -*-coding: utf-8 -*-
"""
    @Project: python-learning-notes
    @File   : rename_tool.py
    @Author : panjq
    @E-mail : pan_jinquan@163.com
    @Date   : 2019-08-09 18:14:37
"""
import os
import shutil
import os.path
from utils import file_processing


def rename_image_dir(dataset_dir, prefix="ID", add_sub=False):
    image_list = file_processing.get_files_list(dataset_dir, postfix=['*.jpg', "*.png"])
    for image_path in image_list:
        format = os.path.basename(image_path).split(".")[-1]
        dirname = os.path.dirname(image_path)
        sub = image_path.split(os.sep)[-2]
        # basename=os.path.basename(image_path)
        index = 0
        newName = [prefix]
        if add_sub:
            newName += [sub]
        newName += ['{:0=5}.{}'.format(index, format)]
        newName = "_".join(newName)
        newpath = os.path.join(dirname, newName)
        while os.path.exists(newpath):
            index += 1
            newName += ['{:0=5}.{}'.format(index, format)]
            newName = "_".join(newName)
            newpath = os.path.join(dirname, newName)

        print(image_path)
        print(newName)
        os.rename(image_path, newpath)


def rename_sub_directory(dir, postfix=""):
    image_id = file_processing.get_sub_directory_list(dir)
    for id in image_id:
        # new_name = id + "_{}".format(postfix)
        new_name = "{}_".format(postfix) + id
        src = os.path.join(dir, id)
        dst = os.path.join(dir, new_name)
        os.rename(src, dst)


def synch_rename_image_dir(src_dir1, src_dir2, dest_dir):
    '''
    synchronize rename image_dict directory
    :param src_dir1:
    :param src_dir2:
    :param dest_dir:
    :return:
    '''
    image_list, image_id = file_processing.get_files_labels(src_dir1, postfix=['*.jpg', "*.png"])
    class_set = list(set(image_id))
    class_set.sort()
    print(class_set)
    for cls_name in class_set:
        id = class_set.index(cls_name) + 1
        s1 = os.path.join(src_dir1, str(cls_name))
        s2 = os.path.join(src_dir2, str(cls_name))
        if not os.path.exists(s1):
            print("no s1 dir:{}".format(s1))
            continue
        if not os.path.exists(s2):
            print("no s2 dir:{}".format(s2))
            continue
        d1 = file_processing.create_dir(dest_dir, 'val')
        # shutil.copytree(s1, os.path.join(d1,str(id)+"_{}".format(cls_name)))
        shutil.copytree(s1, os.path.join(d1, str(id)))

        d2 = file_processing.create_dir(dest_dir, 'facebank')
        # shutil.copytree(s2, os.path.join(d2,str(id)+"_{}".format(cls_name)))
        shutil.copytree(s2, os.path.join(d2, str(id)))





if __name__ == '__main__':
    # src_dir1='/media/dm/dm1/FaceDataset/lexue/lexue2/val'
    # src_dir2='/media/dm/dm1/FaceDataset/lexue/lexue2/facebank'
    # dest_dir='/media/dm/dm1/FaceDataset/lexue/lexue2/dest'
    # synch_rename_image_dir(src_dir1,src_dir2,dest_dir)

    # # dir = '/media/dm/dm/project/dataset/face_recognition/NVR/face/NVRS/trainval'
    # # dataset_dir='F:/clear_data_bzl/val'
    # # dataset_dir='/media/dm/dm/XMC/FaceData/X4/X4_Face132/val'
    # # dataset_dir = '/media/dm/dm1/FaceDataset/lexue/lexue/facebank'
    # dataset_dir = '/media/dm/dm2/FaceRecognition/anti-spoofing/dataset/orig/fake_part'
    dataset_dir = '/media/dm/dm2/FaceRecognition/anti-spoofing/dataset/rgb_ir_dataset/fake_part'
    rename_image_dir(dataset_dir, prefix="monitor")  # # ["paper(纸)","monitor(显示屏)","mask(面具)"]
    # dir="/media/dm/dm1/FaceDataset/X4/CASIA-FaceV5/trainval"
    # rename_sub_directory(dir, postfix="CASIA")
    # image_dir="/media/dm/dm/FaceRecognition/face_recognition_system/framework/data/facebank"
    image_dir = "/media/dm/dm/FaceRecognition/face_recognition_system/framework/data/dmai/facebank"
    # rename_sub_directory(image_dir,postfix="x4")
