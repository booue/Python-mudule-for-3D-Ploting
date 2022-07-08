from numpy import pi, sin, cos, mgrid, ogrid
from mayavi import mlab
import numpy as np
    
def AdvancedPlot():
    # 建立数据(计算出三维空间坐标)
    dphi, dtheta = pi / 250.0, pi / 250.0 # 类似于plot中间隔值，间隔值较大会变为线图而非面图
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
    s = mlab.mesh(x, y, z,representation = 'surface',line_width = 1.0)
    mlab.outline(s)
    mlab.show()

AdvancedPlot()