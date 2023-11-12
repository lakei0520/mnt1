import cv2
import numpy as np

# 加载原始图像
original_img = cv2.imread('output_image.png')  # 替换为你的原始图像路径
edge_img = cv2.imread('canny_img.png', cv2.IMREAD_GRAYSCALE)

# 使用霍夫变换检测线条
# 调整霍夫变换的参数，以减少监测到的直线
# 参数minLineLength控制线的最小长度，参数maxLineGap控制允许的最大间隙
lines = cv2.HoughLinesP(edge_img, 1, np.pi / 180, 10, minLineLength=300, maxLineGap=30)

# 定义延伸长度
extension_length = 500

# 循环遍历所有检测到的线，并在原始图像上绘制它们
for line in lines:
    x1, y1, x2, y2 = line[0]

    # 计算线段的方向
    dx, dy = x2 - x1, y2 - y1

    # 根据方向扩展线段
    extended_x1 = int(x1 - extension_length * dx / np.sqrt(dx**2 + dy**2))
    extended_y1 = int(y1 - extension_length * dy / np.sqrt(dx**2 + dy**2))
    extended_x2 = int(x2 + extension_length * dx / np.sqrt(dx**2 + dy**2))
    extended_y2 = int(y2 + extension_length * dy / np.sqrt(dx**2 + dy**2))

    # 在原始图像上绘制延伸后的线段
    cv2.line(original_img, (extended_x1, extended_y1), (extended_x2, extended_y2), (0, 255, 0), 2)

# 显示包含检测到的直线和延伸后线段的原始图像
cv2.imshow('Detected and Extended Lines', original_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
