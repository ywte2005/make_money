"""
@Author  : 亚博
@Time    : 2021/9/1 10:09 上午
@introduction ：
    1. OpenCV图片读取
"""
import numpy as np
from cv2 import cv2 as cv
from matplotlib import pyplot as plt


# ---------------------------显示图像--------------------
# 0：灰度图         1: 彩图       -1：加载图像，包括alpha通道
img = cv.imread('./img/mn.jpeg', 1)
# 创建一个空白窗口,可调节窗口大小，默认：cv.WINDOW_AUTOSIZE
cv.namedWindow('image',cv.WINDOW_NORMAL)
# 显示图片
cv.imshow('image', img)
# 绑定键
# cv.waitKey(0)
# 销毁所有创建的窗口
# cv.destroyAllWindows()
# 销毁特定的窗口传参，指定窗口名称
# cv.destroyWindow()

# -------------------------写入图像---------------------
# img = cv.imread("./img/mn.jpeg", 0)
# cv.imshow("img", img)
# # 检测键盘输入
# k = cv.waitKey(0)
# if k == 27:
#     cv.destroyAllWindows()
# elif k == ord("s"):  # 等待关键词保存退出
#     cv.imwrite("./img/hdmn.jpeg", img)
#     cv.destroyAllWindows()

# ----------------------使用Matplotlib-----------------
# img = cv.imread("./img/mn.jpeg", 0)
# plt.imshow(img,cmap="gray",interpolation="bicubic")
# plt.xticks([]),plt.yticks([])
# plt.show()

