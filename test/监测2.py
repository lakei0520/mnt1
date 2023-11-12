import cv2
import numpy as np

# 加载原始图像
original_img = cv2.imread('output_image.png')  # 替换为你的原始图像路径
edge_img = cv2.imread('canny_img.png', cv2.IMREAD_GRAYSCALE)

# 使用霍夫变换检测线条
# 调整霍夫变换的参数，以减少监测到的直线
# 参数minLineLength控制线的最小长度，参数maxLineGap控制允许的最大间隙
lines = cv2.HoughLinesP(edge_img, 1, np.pi / 180, 10, minLineLength=300, maxLineGap=50)

# 定义延伸长度
extension_length = 500

# 定义图像中心点坐标
height, width = original_img.shape[:2]
center_x = width // 2

# 存储距离中心点左侧最近的一条直线和距离中心点右侧最近的一条直线
closest_left_line = None
closest_right_line = None
min_left_distance = float('inf')
min_right_distance = float('inf')

# 循环遍历所有检测到的线，并找到距离中心点左侧最近和右侧最近的两条直线
for line in lines:
    x1, y1, x2, y2 = line[0]

    # 计算线段的中心点
    line_center_x = (x1 + x2) // 2

    # 计算线段中心点到图像中心的距离
    distance_to_center = abs(line_center_x - center_x)

    # 更新最近左侧直线的信息
    if line_center_x < center_x and distance_to_center < min_left_distance:
        min_left_distance = distance_to_center
        closest_left_line = line

    # 更新最近右侧直线的信息
    elif line_center_x > center_x and distance_to_center < min_right_distance:
        min_right_distance = distance_to_center
        closest_right_line = line

# 绘制最近左侧的直线
if closest_left_line is not None:
    x1, y1, x2, y2 = closest_left_line[0]
    dx, dy = x2 - x1, y2 - y1
    extended_x1 = int(x1 - extension_length * dx / np.sqrt(dx**2 + dy**2))
    extended_y1 = int(y1 - extension_length * dy / np.sqrt(dx**2 + dy**2))
    extended_x2 = int(x2 + extension_length * dx / np.sqrt(dx**2 + dy**2))
    extended_y2 = int(y2 + extension_length * dy / np.sqrt(dx**2 + dy**2))
    cv2.line(original_img, (extended_x1, extended_y1), (extended_x2, extended_y2), (0, 255, 0), 2)

# 绘制最近右侧的直线
if closest_right_line is not None:
    x1, y1, x2, y2 = closest_right_line[0]
    dx, dy = x2 - x1, y2 - y1
    extended_x1 = int(x1 - extension_length * dx / np.sqrt(dx**2 + dy**2))
    extended_y1 = int(y1 - extension_length * dy / np.sqrt(dx**2 + dy**2))
    extended_x2 = int(x2 + extension_length * dx / np.sqrt(dx**2 + dy**2))
    extended_y2 = int(y2 + extension_length * dy / np.sqrt(dx**2 + dy**2))
    cv2.line(original_img, (extended_x1, extended_y1), (extended_x2, extended_y2), (0, 255, 0), 2)

# 显示包含检测到的直线和延伸后线段的原始图像
cv2.imshow('Closest Lines and Extended Lines', original_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
