# 2018-9-14
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
# from skimage import transform
# import math

# # 图像裁剪
# img = cv2.imread("image/m3.png", 0)
# print(img.shape)
# # img = cv2.imread("image/m3.png") # 0表示以对读入图像灰度处理
# w, h= img.shape
# # print(img.shape)
# img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# s = min(w, h)  # 取最小值裁剪成sxs大小
# # np.c_[a,b]
# # img=np.zeros([400,400,3],np.uint8)  
# # 修改通道值  
# # img[:,:,0]=np.ones([400,400])*255  
# # img[:, :, 2] = np.ones([400, 400]) * 255
  
# pre = dummy = img
# # dummy = cv2.resize(dummy, (200, 200,3), interpolation=cv2.INTER_LINEAR)
# # plt.subplot(121)
# # plt.imshow(dummy)
# # cv2.imshow("0", dummy[:,:,0])
# # cv2.imshow("1", dummy[:,:,1])
# # cv2.imshow("2", dummy[:,:,2])
# # size = [z,w,h]
# # k=np.zeros(size, np.uint8)
# # print(k)
# # k[:,:,0] = img[:,:,0]
# # k[:,:,1] = img[:,:,1]
# # k[:,:,2] = img[:,:,2]

# cv2.imshow("IMG", img)
# cv2.imwrite("img.png", np.asarray(img, np.uint8))
# print(dummy[:,:,1].shape)
# # print(img)
# img = img[:s, :s]

# img = cv2.resize(img, (200, 200), interpolation=cv2.INTER_LINEAR)
# cv2.imwrite("xx.jpg", np.asarray(img, np.uint8))
# # plt.subplot(122)
# # plt.imshow(img)
# # plt.show()
# cv2.imshow("new", img)
# cv2.waitKey()
# cv2.destroyAllWindows()



# n = [[1,2,3,5,65,7], [55,233,44,66,8798,2], [55444,233,44,66,8798,2]]
# p = np.asarray(n)
# t = [0, 2,2]
# r = p[t[:2]]
# print(math.abs(-1))

# print(os.path.dirname(__file__))
# print(np.array((2.2,1), np.float32))


# img = cv2.pyrDown(cv2.imread("image/m_L.png", 0))
# cv2.imshow("orignal", img)
# w, h= img.shape
# # print(img.shape)
# s = min(w, h)  # 取最小值裁剪成sxs大小
# pre = dummy = img

# dummy = cv2.resize(dummy, (200, 200), interpolation=cv2.INTER_LINEAR)
# img = img[:s, :s]


# ret, thresh = cv2.threshold(img.copy() , 127, 255, cv2.THRESH_BINARY)

# black = cv2.cvtColor(np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8), cv2.COLOR_GRAY2BGR)
# image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# for cnt in contours:
#   	epsilon = 0.01 * cv2.arcLength(cnt,True) # 获得轮廓周长
#   	approx = cv2.approxPolyDP(cnt,epsilon,True)
#   	# cv2.approxPolyDP(cnt,epsilon,True)
# 	# 第一个参数为轮廓
# 	# 第二个参数为 e 值， 表示原轮廓与近似多边形的最大差值(值越小近似多边形与原轮廓越接近)
# 	# 第三个参数为布尔值标记， 表示这个多边形是否合并
# 	# 也被称为弧长。可以使用函数cv2.arcLength()计算得到。这个函数的第二参数可以用来指定对象的形状是闭合的（True），还是打开的（一条曲线）。
#   	hull = cv2.convexHull(cnt) # 凸包
# 	# hull = cv2.convexHull(cnt,hull,clockwise,returnPoints)
# 	# 参数：
# 	# cnt我们要传入的轮廓
# 	# hull输出，通常不需要
# 	# clockwise方向标志，如果设置为True，输出的凸包是顺时针方向的，否则为逆时针方向。
# 	# returnPoints默认值为True。它会返回凸包上点的坐标，如果设置为False，就会返回与凸包点对应的轮廓上的点。
# 	# 但是如果你想获得凸性缺陷，需要把returnPoints设置为False。以上面矩形为例，首先我们找到他的轮廓从cnt。现在把returnPoints设置为True查找凸包，得到的就是矩形的四个角点。把returnPoints设置为False，得到的是轮廓点的索引
#   	cv2.drawContours(black, [cnt], -1, (0, 255, 0), 2)
#   	cv2.drawContours(black, [approx], -1, (255, 255, 0), 2)
#   	cv2.drawContours(black, [hull], -1, (0, 0, 255), 2)

# cv2.imshow("hull", black)
# cv2.waitKey()
# cv2.destroyAllWindows()