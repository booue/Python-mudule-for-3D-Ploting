# -*-coding = utf-8-*-

# Author:qyan.li
# Date:2022/7/1 10:35
# Topic:mayavi的基础用法
# Reference:

from numpy import pi, sin, cos, mgrid, ogrid
from mayavi import mlab # 引入mlab模块，mayavi中类似于matlab操作
import numpy as np


def BasicPlot():
    '''Mayavi模块基础使用学习
    :return: None
    '''
    # 给出待绘制图形的三维空间坐标(表达式)
    x, y = np.ogrid[-2:2:20j, -2:2:20j]
    z = x * np.exp(- x ** 2 - y ** 2)
    # 调用surf函数绘制三维空间中的曲面
    pl = mlab.surf(x, y, z, warp_scale="auto")
    # 借助于axes添加坐标变量，outline函数添加图形外框
    mlab.axes(xlabel='x', ylabel='y', zlabel='z')
    mlab.outline(pl)
    # 图形显示
    mlab.show()

def AdvancedPlot():
    '''csdn博客Mayavi测试用例
    :return: None
    '''

    # 建立数据(计算出三维空间坐标)
    dphi, dtheta = pi / 250.0, pi / 250.0
    [phi, theta] = mgrid[0:pi + dphi * 1.5:dphi, 0:2 * pi + dtheta * 1.5:dtheta]
    m0 = 4
    m1 = 3
    m2 = 2
    m3 = 3
    m4 = 6
    m5 = 2
    m6 = 6
    m7 = 4
    r = sin(m0 * phi) ** m1 + cos(m2 * phi) ** m3 + sin(m4 * theta) ** m5 + cos(m6 * theta) ** m7
    x = r * sin(phi) * cos(theta)
    y = r * cos(phi)
    z = r * sin(phi) * sin(theta)

    # 对该数据进行三维可视化
    # mesh函数representation参数可选(surface默认值绘制曲面，wireframe绘制边线)
    s = mlab.mesh(x, y, z,representation = 'wireframe',line_width = 1.0)
    mlab.outline(s) # 为图形添加边线
    mlab.show()

def Plot3dTest():
    '''测试mayavi中的plot3d，points3d函数
    :return: None
    '''
    x = np.arange(0,20,1)
    y = np.sin(x)
    z = y * np.sin(x)

    # plot3d和points3d参数传入一维坐标点，绘制三维空间中的一系列点或者曲线
    # mlab.plot3d(x,y,z,color = (1,0,0),tube_radius = 0.1) # 参数指明圆管的粗细
    mlab.points3d(x,y,z,color = (1,0,1)) # 颜色指定(可以取间隔大，方便观察区别)
    mlab.show()

def ImshowTest():
    '''测试mayavi中的imshow,surf,contour_surf函数
    :return: None
    '''
    x, y = np.ogrid[-2:2:20j, -2:2:20j]
    z = x * np.exp( - x**2 - y**2)
    # mlab.imshow(x,y,z) # 绘制二维平z面色彩图
    # mlab.surf(x,y,z) # 绘制三维空间曲z面
    mlab.contour_surf(x,y,z) # 绘制二维平面等高线
    mlab.show()

def barchartTest():
    '''barchart函数
    :return: None
    '''
    s = np.random.rand(3, 3)
    mlab.barchart(s) # 生成三维空间中的柱状图
    mlab.vectorbar() # 附颜色带
    mlab.show()

def contour3dTest():
    '''contour3d函数
    :return: None
    '''
    x, y, z = ogrid[-5:5:64j, -5:5:64j, -5:5:64j]
    scalars = x * x * 0.5 + y * y + z * z * 2.0
    mlab.contour3d(scalars, contours=6, transparent=True)
    mlab.colorbar()
    mlab.show()

def example():
    x, y = np.mgrid[-10:10:200j, -10:10:200j]
    z = 100 * np.sin(x * y) / (x * y)

    # Visualize it with mlab.surf
    mlab.figure(bgcolor=(1, 1, 1))
    surf = mlab.surf(z, colormap='cool')

    # Retrieve the LUT of the surf object.
    lut = surf.module_manager.scalar_lut_manager.lut.table.to_array()

    # The lut is a 255x4 array, with the columns representing RGBA
    # (red, green, blue, alpha) coded with integers going from 0 to 255.

    # We modify the alpha channel to add a transparency gradient
    lut[:, -1] = np.linspace(0, 255, 256)
    # and finally we put this LUT back in the surface object. We could have
    # added any 255*4 array rather than modifying an existing LUT.
    surf.module_manager.scalar_lut_manager.lut.table = lut

    # We need to force update of the figure now that we have changed the LUT.
    mlab.draw()
    mlab.view(40, 85)

    mlab.show()

def using():
    n_mer, n_long = 6, 11
    dphi = np.pi / 1000.0
    phi = np.arange(0.0, 2 * np.pi + 0.5 * dphi, dphi)
    mu = phi * n_mer
    x = np.cos(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
    y = np.sin(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
    z = np.sin(n_long * mu / n_mer) * 0.5
    mlab.plot3d(x, y, z, tube_radius=0.1, color=(1, 0, 0))
    mlab.show()

def main():
    # BasicPlot()
    # AdvancedPlot()
    # Plot3dTest()
    # ImshowTest()
    # barchartTest()
    contour3dTest()
    # example()
    # using()
    pass



if __name__ == '__main__':
    main()



