
#2.0
import yaml
import numpy as np
import os
def world_c(x,y):
    #工作路径

    # 用于读取YAML文件的文件路径
    yaml_file_path = '../data/parameter/calib.yaml'  # 将文件路径替换为实际文件路径

    # 打开YAML文件并解析为字典
    with open(yaml_file_path, 'r') as yaml_file:
        # 读取文件内容
        yaml_contents = yaml_file.read()

    # 从文件内容中查找 "config=" 字段，然后截取该字段后面的内容
    config_start = yaml_contents.find("config = ")
    if config_start != -1:
        config_start += len("config = ")
        config_data = yaml_contents[config_start:]

        # 解析截取的配置数据
        config = yaml.safe_load(config_data)
        lidar_to_cam_mix = config['lidar_to_cam']

        fx, fy = config['fx'], config['fy']
        u0, v0 = config['u0'], config['v0']
        u, v = x, y  # 以图像中心点为例

        # 从像素坐标转换到归一化相机坐标
        x_normalized = (u - u0) / fx
        y_normalized = (v - v0) / fy

        # 归一化坐标到相机坐标
        camera_coordinates = np.array([x_normalized, y_normalized, 1, 1])
        lidar_to_cam_mix_4 = np.array(lidar_to_cam_mix).reshape(4, 4)
        # 使用逆矩阵将相机坐标映射到世界坐标
        world_coordinates = np.linalg.inv(lidar_to_cam_mix_4).dot(camera_coordinates)
        # 提取世界坐标 (X, Y, Z)
        X = world_coordinates[0]
        Y = world_coordinates[1]
        Z = world_coordinates[2]
        return X,Y,Z
    else:
        print("No 'config=' field found in the YAML file.")


x,y,z=world_c(793,540)
print(x,y,z)
