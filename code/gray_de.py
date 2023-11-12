# -*- coding:utf-8 -*-
"""
作者：20916
日期：2023年10月12日
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_profile(gray_values):
    # 绘制左右两个方向的曲线
    for i, values in enumerate(gray_values):
        plt.plot(values, label='profile' + str(i))

    plt.legend()
    plt.xlabel('Distance')
    plt.ylabel('Pixel Grayscale Value')
    plt.title('Grayscale Profile')
    plt.show()



def detect(img_path):
    line_point={'-2':[[0,0],[0,0],[0,0],[0,0],[0,0]],'-1':[[0,0],[0,0],[0,0],[0,0],[0,0]],'+1':[[0,0],[0,0],[0,0],[0,0],[0,0]],'+2':[[0,0],[0,0],[0,0],[0,0],[0,0]]}
    result_ = {'-2': 0, '-1': 0, '+1': 0, '+2': 0}
    result = [result_.copy() for _ in range(5)]
    # 读取图像
    img = cv2.imread(img_path)

    # 获取图像中心点坐标
    h, w = img.shape[:2]
    #点1
    mid_x = [0, 0, 0, 0, 0]
    mid_y = [0, 0, 0, 0, 0]
    for i in range(5):
        mid_x[i]=w // 2
        mid_y[i]=h // 2+40*i
    image_size=[w,h]
    # 定义探测方向、长度
    directions = [(-1, 0), (1, 0)]
    length = int(w/2)
    #五个数
    f_n_1 = [0, 0, 0, 0, 0]
    f_p_1 = [0, 0, 0, 0, 0]

    for j in range(len(mid_y)):
        # 遍历每个方向
        for dx, dy in directions:
            # 从中心点开始迭代探测
            for i in range(length):
                x = mid_x[j] + dx * i
                y = mid_y[j] + dy * i
                # 防止索引越界
                if x < 0 or x >= w or y < 0 or y >= h:
                    break
                # 读取灰度值
                gray = img[y, x][0]
                #values.append(gray)
                #撰写result
                if (gray != 0):
                    if (dx == -1):
                        if (result[j]['-1'] == 0):
                            result[j]['-1'] = gray
                            line_point['-1'][j] = [x, y]
                            f_n_1[j] = x
                        elif (result[j]['-2'] == 0 and f_n_1[j] - x > 50):
                            result[j]['-2'] = gray
                            line_point['-2'][j] = [x, y]
                    elif (dx == 1):
                        if (result[j]['+1'] == 0):
                            result[j]['+1'] = gray
                            line_point['+1'][j] = [x, y]
                            f_p_1[j] = x
                        elif (result[j]['+2'] == 0 and x - f_p_1[j] > 50):
                            result[j]['+2'] = gray
                            line_point['+2'][j] = [x, y]
        # 加入结果
        #gray_values.append(values)
    #将语义分割结果转换成车道线类型
    for i in range(len(mid_y)):
        for k, v in result[i].items():
            if v == 1:
                result[i][k] = 'solid'
            elif v == 2:
                result[i][k] = 'dash'
            elif v == 3:
                result[i][k] = 'double'
            elif v == 0:
                result[i][k] = 'null'

    # print(result)
    # print(image_size)
    # print(line_point)
    return result,image_size,line_point
    # 画图可视化
    #plot_profile(gray_values)

#img_path='f628438.png'
#detect(img_path)
