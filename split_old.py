# import numpy as np 
# import pandas as pd 
# from pathlib import Path
# from xml.dom.minidom import parse
# from shutil import copyfile
# import os
# from sklearn.model_selection import train_test_split

# classes = ['helmet','head','person']

# def convert_annot(size , box):
#     x1 = int(box[0])
#     y1 = int(box[1])
#     x2 = int(box[2])
#     y2 = int(box[3])

#     dw = np.float32(1. / int(size[0]))
#     dh = np.float32(1. / int(size[1]))

#     w = x2 - x1
#     h = y2 - y1
#     x = x1 + (w / 2)
#     y = y1 + (h / 2)

#     x = x * dw
#     w = w * dw
#     y = y * dh
#     h = h * dh
#     return [x, y, w, h]

# def save_txt_file(img_jpg_file_name, size, img_box):
#     save_file_name = './Dataset/labels/' +  img_jpg_file_name + '.txt'
    
#     #file_path = open(save_file_name, "a+")
#     with open(save_file_name ,'a+') as file_path:
#         for box in img_box:

#             cls_num = classes.index(box[0])

#             new_box = convert_annot(size, box[1:])

#             file_path.write(f"{cls_num} {new_box[0]} {new_box[1]} {new_box[2]} {new_box[3]}\n")

#         file_path.flush()
#         file_path.close()


# def get_xml_data(file_path, img_xml_file):
#     img_path = file_path + '/' + img_xml_file + '.xml'
#     #print(img_path)

#     dom = parse(img_path)
#     root = dom.documentElement
#     img_name = root.getElementsByTagName("filename")[0].childNodes[0].data
#     img_size = root.getElementsByTagName("size")[0]
#     objects = root.getElementsByTagName("object")
#     img_w = img_size.getElementsByTagName("width")[0].childNodes[0].data
#     img_h = img_size.getElementsByTagName("height")[0].childNodes[0].data
#     img_c = img_size.getElementsByTagName("depth")[0].childNodes[0].data
   
#     img_box = []
#     for box in objects:
#         cls_name = box.getElementsByTagName("name")[0].childNodes[0].data
#         x1 = int(box.getElementsByTagName("xmin")[0].childNodes[0].data)
#         y1 = int(box.getElementsByTagName("ymin")[0].childNodes[0].data)
#         x2 = int(box.getElementsByTagName("xmax")[0].childNodes[0].data)
#         y2 = int(box.getElementsByTagName("ymax")[0].childNodes[0].data)
        
#         img_jpg_file_name = img_xml_file + '.jpg'
#         img_box.append([cls_name, x1, y1, x2, y2])
  

#     # test_dataset_box_feature(img_jpg_file_name, img_box)
#     save_txt_file(img_xml_file, [img_w, img_h], img_box)

# files = os.listdir('./annotations')
# for file in files:
#     file_xml = file.split(".")
#     get_xml_data('./annotations', file_xml[0])

# image_list = os.listdir('./images')
# train_list, test_list = train_test_split(image_list, test_size=0.2, random_state=42)
# val_list, test_list = train_test_split(test_list, test_size=0.5, random_state=42)
# print('total =',len(image_list))
# print('train :',len(train_list))
# print('val   :',len(val_list))
# print('test  :',len(test_list))

# def copy_data(file_list, img_labels_root, imgs_source, mode):

#     root_file = Path( './Dataset/images/'+  mode)
#     if not root_file.exists():
#         print(f"Path {root_file} does not exit")
#         os.makedirs(root_file)

#     root_file = Path('./Dataset/labels/' + mode)
#     if not root_file.exists():
#         print(f"Path {root_file} does not exit")
#         os.makedirs(root_file)

#     for file in file_list:               
#         img_name = file.replace('.png', '')        
#         img_src_file = imgs_source + '/' + img_name + '.png'        
#         label_src_file = img_labels_root + '/' + img_name + '.txt'

#         #print(img_sor_file)
#         #print(label_sor_file)
#         # im = Image.open(rf"{img_sor_file}")
#         # im.show()

#         # Copy image
#         DICT_DIR = './Dataset/images/'  + mode
#         img_dict_file = DICT_DIR + '/' + img_name + '.png'

#         copyfile(img_src_file, img_dict_file)

#         # Copy label
#         DICT_DIR = './Dataset/labels/' + mode
#         img_dict_file = DICT_DIR + '/' + img_name + '.txt'
#         copyfile(label_src_file, img_dict_file)

# copy_data(train_list, './Dataset/labels', './images', "train")
# copy_data(val_list,   './Dataset/labels', './images', "val")
# copy_data(test_list,  './Dataset/labels', './images', "test")

import yaml

# Create configuration
config = {
   "path": "./Dataset/images",
   "train": "./Dataset/images/train",
   "val": "./Dataset/images/val",
   "test": "./Dataset/images/test",
   "nc": 3,
   "names": ['helmet','head','person']
}
with open("data.yaml", "w") as file:
   yaml.dump(config, file, default_flow_style=False)