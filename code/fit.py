import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from world_coordinate import world_c
# 示例数据
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2.1, 3.9, 7.2, 9.8, 8])

x = np.array([550, 323, 3, 4, 5])
y = np.array([640, 740, 7.2, 9.8, 8])

line_point={'-2': [[793, 540], [712, 580], [630, 620], [547, 660], [465, 700]], '-1': [[933, 540], [896, 580], [860, 620], [823, 660], [787, 700]], '+1': [[1067, 540], [1074, 580], [1080, 620], [1087, 660], [1093, 700]], '+2': [[1224, 540], [1281, 580], [1337, 620], [1392, 660], [1447, 700]]}
print(len(line_point))
def cubic_polynomial(x, c2, c1, c0):
    return   c2 * x**2 + c1 * x + c0

def fix(v):
    x=[]
    y = []
    for i in range(len(v)):
        x.append(v[i][0])
        y.append(v[i][1])
    return x,y
def fit3(line_point):
    f_result = {'-2': [], '-1': [], '1': [], '2': []}
    for k,v in line_point.items():
        x,y=fix(v)
        #print(x,y)
        X = []
        Y = []
        Z = []
        for i in range(len(x)):
            x3, y3, z3 = world_c(x[i], y[i])
            X.append(x3)
            Y.append(y3)
            Z.append(z3)
        params, covariance = curve_fit(cubic_polynomial, X, Y)
        # params 包含了拟合的系数：a, b, c, d
        c2, c1, c0 = params
        print(params)
        #f_result[k]=[c3, c2, c1, c0]
        f_result[k] = [c0, c1, c2]
        #print(f_resule[k])
    #print(f_result)
    return f_result


fit3(line_point)
# x_fit = np.linspace(min(x), max(x), 100)
# y_fit = cubic_polynomial(x_fit, a, b, c, d)
#
# plt.scatter(x, y, label='Data')
# plt.plot(x_fit, y_fit, 'r', label='Fitted Curve')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend()
# plt.show()