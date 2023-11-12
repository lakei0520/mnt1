import numpy as np
import cv2
import matplotlib.pyplot as plt

def sliding_window(img):
    # 求取整幅图像纵向直方图
    histogram = np.sum(img, axis=0)
    plt.figure()
    plt.title('Vertical Projection Histogram')
    plt.plot(histogram)
    plt.show()
    # 根据直方图确定左右线起始点区域
    midpoint = histogram.shape[0] // 2
    leftx_base = np.argmax(histogram[:midpoint])
    leftx_range = histogram[max(leftx_base - 100, 0):leftx_base + 100]
    leftx_base = np.where(leftx_range == np.max(leftx_range))[0]
    print(leftx_base)
    rightx_base = np.argmax(histogram[midpoint:]) + midpoint
    rightx_range = histogram[rightx_base - 100:rightx_base + 100]
    rightx_base = np.where(rightx_range == np.max(rightx_range))[0]
    print(rightx_base)
    # 滑动窗口参数设置
    nwindows = 15
    margin = 50
    minpix = 5
    window_height = img.shape[0] // nwindows

    # 找到图像所有非零点
    nonzero = img.nonzero()
    nonzeroy = np.array(nonzero[0])
    nonzerox = np.array(nonzero[1])

    left_lane_inds = []
    right_lane_inds = []

    # 开始滑动窗口检测
    for window in range(nwindows):
        win_y_low = img.shape[0] - (window + 1) * window_height
        win_y_high = img.shape[0] - window * window_height
        win_xleft_low = leftx_base - margin
        win_xleft_high = leftx_base + margin
        win_xright_low = rightx_base - margin
        win_xright_high = rightx_base + margin

        good_left_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) &
                          (nonzerox >= win_xleft_low) & (nonzerox < win_xleft_high)).nonzero()[0]
        good_right_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) &
                           (nonzerox >= win_xright_low) &  (nonzerox < win_xright_high)).nonzero()[0]

        if len(good_left_inds) > minpix:
            leftx_base = np.int32(np.mean(nonzerox[good_left_inds]))
        if len(good_right_inds) > minpix:
            rightx_base = np.int32(np.mean(nonzerox[good_right_inds]))

        left_lane_inds.append(good_left_inds)
        right_lane_inds.append(good_right_inds)

    left_lane_inds = np.concatenate(left_lane_inds)
    right_lane_inds = np.concatenate(right_lane_inds)

    leftx = nonzerox[left_lane_inds]
    lefty = nonzeroy[left_lane_inds]
    rightx = nonzerox[right_lane_inds]
    righty = nonzeroy[right_lane_inds]

    left_fit = np.polyfit(lefty, leftx, 2)
    right_fit = np.polyfit(righty, rightx, 2)

    return left_fit, right_fit

binary='../data/image/f628438.png'
image = cv2.imread(binary, cv2.IMREAD_GRAYSCALE)
# 测试
left_fit, right_fit = sliding_window(image)
print(left_fit, right_fit)
# 绘图显示