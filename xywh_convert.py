import os
import cv2
import numpy as np

classes = ["Text", "Equation", "Figure", "Table"]  # 类别

img_path = 'D:\\TextAnalysis\\Newfolder\\'
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def convert_annotation(image_id):
  with open('./labels\%s.txt' % (image_id), "r", encoding = 'UTF-8') as in_file:
    with open('./Label_ALL.txt', 'a') as out_file:

      image = cv2.imread(img_path + '%s.jpg' % (image_id))
      size = image.shape
      wide = size[1] #宽度
      height = size[0] #高度

      lines = in_file.readlines()     #读取全部内容 ，并以列表方式返回
      print(len(lines)) 
      for line in lines:
        line_split = line.split()
        cls = line_split[0]
        x = np.float32(line_split[1])
        y = np.float32(line_split[2])
        wp = np.float32(line_split[3])
        hp = np.float32(line_split[4])
        xmin = int(wide * (x - (wp / 2.0)))
        ymin = int(height * (y - (hp / 2.0)))
        xmax = int(wide * (x + (wp / 2.0)))
        ymax = int(height * (y + (hp / 2.0)))
        out_file.writelines(image_id + '.jpg ' + classes[int(cls)] + ' ' + str(xmin )+ ' ' + str(ymin) + ' ' + str(xmax) + ' ' + str(ymax) + '\n')
# 指定文件夹路径
folder_path = 'D:\\TextAnalysis\\yolov5\\runs\\detect\\exp\\labels'

# 获取文件夹下所有文件的名称
files = os.listdir(folder_path)

# 循环处理每个文件的名称
for file in files:
    # 获取文件的完整路径
    file_path = os.path.join(folder_path, file)
    # 判断是否为文件
    if os.path.isfile(file_path):
        # 获取文件名（不带后缀）
        file_name = os.path.splitext(file)[0]
        convert_annotation(file_name)
        print(file_name)

