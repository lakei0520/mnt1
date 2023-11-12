import numpy as np
import cv2
import matplotlib.pyplot as plt

# def find_line_fit(img, nwindows=9, margin=100, minpix=50):
def find_line_fit(img, nwindows=15, margin=20, minpix=5):
    histogram = np.sum(img[img.shape[0]//2: ,:], axis=0)

    plt.figure()
    plt.title('Vertical Projection Histogram')
    plt.plot(histogram)
    plt.show()
    # Create an output image to draw on and  visualize the result
    # 创建输出图像以绘制并可视化结果
    out_img = np.dstack((img, img, img)) * 255
    # Find the peak of the left and right halves of the histogram
    # 找出直方图左右两半的峰值
    # These will be the starting point for the left and right lines
    # 这些将是左右线的起点
    midpoint = np.int_(histogram.shape[0] /2)
    print(midpoint)
    leftx_base = np.argmax(histogram[:midpoint])
    print(leftx_base)
    rightx_base = np.argmax(histogram[midpoint:]) + midpoint
    print(rightx_base)

    # Set height of windows
    # 设置窗框高度
    window_height = np.int_(img.shape[0 ] /nwindows)
    # Identify the x and y positions of all nonzero pixels in the image
    # 辨别所有非零像素的x和y的位置
    nonzero = img.nonzero() # 用于得到非零元素的位置
    nonzeroy = np.array(nonzero[0])
    nonzerox = np.array(nonzero[1])
    # Current positions to be updated for each window
    # 用当前的位置去更新每个窗口
    leftx_current = leftx_base
    rightx_current = rightx_base
    # Create empty lists to receive left and right lane pixel indices
    # 创建空的列表分别放入左右两天车道线像素合集
    left_lane_inds = []
    right_lane_inds = []

    # Step through the windows one by one
    # 一步一步滑动窗口检测
    '''

    '''
    for window in range(nwindows):
        # Identify window boundaries in x and y (and right and left)
        win_y_low = img.shape[0] - (window +1 ) *window_height
        win_y_high = img.shape[0] - window *window_height
        win_xleft_low = leftx_current - margin
        win_xleft_high = leftx_current + margin
        win_xright_low = rightx_current - margin
        win_xright_high = rightx_current + margin
        # Draw the windows on the visualization image
        cv2.rectangle(out_img,(win_xleft_low ,win_y_low) ,(win_xleft_high ,win_y_high),(0 ,255 ,0), 2)
        cv2.rectangle(out_img,(win_xright_low ,win_y_low) ,(win_xright_high ,win_y_high),(0 ,255 ,0), 2)
        # Identify the nonzero pixels in x and y within the window
        good_left_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) &
                          (nonzerox >= win_xleft_low) &  (nonzerox < win_xleft_high)).nonzero()[0]
        good_right_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) &
                           (nonzerox >= win_xright_low) &  (nonzerox < win_xright_high)).nonzero()[0]
        # Append these indices to the lists
        left_lane_inds.append(good_left_inds)
        right_lane_inds.append(good_right_inds)
        # If you found > minpix pixels, recenter next window on their mean position
        if len(good_left_inds) > minpix:
            leftx_current = np.int_(np.mean(nonzerox[good_left_inds]))
        if len(good_right_inds) > minpix:
            rightx_current = np.int_(np.mean(nonzerox[good_right_inds]))

    # Concatenate the arrays of indices
    #
    left_lane_inds = np.concatenate(left_lane_inds)
    right_lane_inds = np.concatenate(right_lane_inds)

    # Extract left and right line pixel positions
    leftx = nonzerox[left_lane_inds]
    lefty = nonzeroy[left_lane_inds]
    rightx = nonzerox[right_lane_inds]
    righty = nonzeroy[right_lane_inds]

    # to plot
    out_img[nonzeroy[left_lane_inds], nonzerox[left_lane_inds]] = [255, 0, 0]
    out_img[nonzeroy[right_lane_inds], nonzerox[right_lane_inds]] = [0, 0, 255]

    # Fit a second order polynomial to each
    left_fit = np.polyfit(lefty, leftx, 3)
    right_fit = np.polyfit(righty, rightx, 3)
    return left_fit, right_fit, out_img

# Generate x and y values for plotting
def get_fit_xy(img, left_fit, right_fit):
    ploty = np.linspace(0, img.shape[0] -1, img.shape[0])
    left_fitx = left_fit[0] *ploty**2 + left_fit[1] *ploty + left_fit[2]
    right_fitx = right_fit[0]  *ploty**2 + right_fit[1] *ploty + right_fit[2]
    return left_fitx, right_fitx, ploty
binary='../data/image/f628438.png'
binary = cv2.imread(binary, cv2.IMREAD_GRAYSCALE)
left_fit, right_fit, out_img = find_line_fit(binary, nwindows=15, margin=10, minpix=5)
print(right_fit)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', out_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#left_fitx, right_fitx, ploty = get_fit_xy(binary, left_fit, right_fit)
print(right_fit)

