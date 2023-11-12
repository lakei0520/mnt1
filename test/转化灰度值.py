from PIL import Image

# 打开PNG图片
image_path = "f628438.png"
img = Image.open(image_path)

# 转换为灰度图像
gray_img = img.convert('L')

# 获取图像数据
data = list(gray_img.getdata())

# 将每个像素的灰度值乘以50
data = [value * 50 for value in data]

# 创建新的图像对象
new_img = Image.new('L', gray_img.size)
new_img.putdata(data)

# 保存新图像
new_image_path = "output_image.png"
new_img.save(new_image_path)

print(f"图像已保存至 {new_image_path}")
