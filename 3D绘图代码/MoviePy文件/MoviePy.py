# Author:qyan.li
# Date:2022.3.11
# Topic:借助于python制作3D动画
# Reference : https://zhuanlan.zhihu.com/p/36727011

# # 知乎示例：
# # 借助于Moviepy和mayavi实现3D动态图
# import numpy as np
# import mayavi.mlab as mlab
# import  moviepy.editor as mpy

# duration= 2 # duration of the animation in seconds (it will loop)

# # 用Mayavi制作一个图形
# fig_myv = mlab.figure(size=(220,220), bgcolor=(1,1,1))
# X, Y = np.linspace(-2,2,200), np.linspace(-2,2,200)
# XX, YY = np.meshgrid(X,Y)
# ZZ = lambda d: np.sinc(XX**2+YY**2)+np.sin(XX+d)

# # 用MoviePy将图形转换为动画，编写动画GIF

# def make_frame(t):
#     mlab.clf() # 清掉图形（重设颜色）
#     mlab.mesh(YY,XX,ZZ(2*np.pi*t/duration), figure=fig_myv)
#     return mlab.screenshot(antialiased=True)

# animation = mpy.VideoClip(make_frame, duration=duration)
# animation.write_gif("sinc.gif", fps=20)



## 借助于Moviepy和matplotlib生成3D动态图
## 官方文档参考：http://doc.moviepy.com.cn/index.html#document-3_%E4%BD%9C%E5%93%81%E5%B1%95%E7%A4%BA/index

'''选择MoviePy理由：
你想将从别的Python库里（如Matplotlib、Mayavi、Gizeh、scikit-images等）生成的图片制作成动画。
'''

import matplotlib.pyplot as plt
import numpy as np
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

x = np.linspace(-2, 2, 200)

duration = 2 # 定义图像的变化速度(值越小，图像切换越快，对应图像的变化速度越快)

fig, ax = plt.subplots()
def make_frame(t):
    ax.clear()
    ax.plot(x, np.sinc(x**2) + np.sin(x + 2*np.pi/duration * t), lw=2) # lw参数定义绘图线条的粗细
    ax.set_ylim(-1.5, 2.5)
    return mplfig_to_npimage(fig)

animation = VideoClip(make_frame, duration=duration) # 生成gif或者mp4
animation.write_gif('matplotlib.gif', fps=20) # 生成gif文件
# animation.write_videofile('matplotlib.mp4',fps = 24) # 生成mp4文件


# ## MoviePy和Mayavi
# import numpy as np
# import mayavi.mlab as mlab
# import  moviepy.editor as mpy

# duration = 2 # duration of the animation in seconds (it will loop)

# # 用Mayavi制作一个图形

# fig = mlab.figure(size=(500, 500), bgcolor=(1,1,1))

# u = np.linspace(0,2*np.pi,100)
# xx,yy,zz = np.cos(u), np.sin(3*u), np.sin(u) # 点
# l = mlab.plot3d(xx,yy,zz, representation="wireframe", tube_sides=5,
#                 line_width=.5, tube_radius=0.2, figure=fig)

# # 用MoviePy将图形转换为动画，编写动画GIF

# def make_frame(t):
#     """ Generates and returns the frame for time t. """
#     y = np.sin(3*u)*(0.2+0.5*np.cos(2*np.pi*t/duration))
#     l.mlab_source.set(y = y) # change y-coordinates of the mesh
#     mlab.view(azimuth= 360*t/duration, distance=9) # 相机视角
#     return mlab.screenshot(antialiased=True) # 返回RGB图形

# animation = mpy.VideoClip(make_frame, duration=duration).resize(0.5)
# # 视频生成花费10秒, GIF 生成花费25秒
# animation.write_videofile("wireframe.mp4", fps=20)
# animation.write_gif("wireframe.gif", fps=20)



# ## 个人测试文件
# import matplotlib.pyplot as plt
# import numpy as np
# from moviepy.editor import VideoClip
# from moviepy.video.io.bindings import mplfig_to_npimage

# x = np.linspace(-2, 2, 200)

# duration = 2 # 定义图像的变化速度(值越小，图像切换越快，对应图像的变化速度越快)

# fig, ax = plt.subplots()
# def make_frame(t):
#     ax.clear()
#     # plot内部函数定义函数
#     ax.plot(x,np.sin(x + 2*np.pi/duration * t), lw=2) # lw参数定义绘图线条的粗细
#     ax.set_ylim(-1.5, 2.5)
#     return mplfig_to_npimage(fig)

# animation = VideoClip(make_frame, duration=duration) # 生成gif或者mp4
# animation.write_gif('matplotlib.gif', fps=20) # 生成gif文件
# # animation.write_videofile('matplotlib.mp4',fps = 24) # 生成mp4文件