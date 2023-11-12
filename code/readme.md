# 样例数据说明
images为原始图像
segmentresults为语义分割的结果，本任务的输入
calib.yaml为相机内外参数
labels为供参考的真值结果

语义分割的结果为.png图像，图像上的像素值对应该像素在原始图像的分类label,label和像素值的对应关系如下：
0: 背景
1: 单实线
2: 单虚线
3: 双线
