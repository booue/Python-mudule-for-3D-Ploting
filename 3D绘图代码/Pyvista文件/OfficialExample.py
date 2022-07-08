# -*-coding = utf-8-*-

# Author:qyan.li
# Date:2022/6/22 10:28
# Topic:pyvista绘图模块学习，官方文档示例
# Reference:https://docs.pyvista.org/examples/index.html

import pyvista as pv
import numpy as np
from pyvista import examples

'''
小Tips：
1. 下述绘制的图形均可以借助于鼠标进行拖动和旋转
2. 拖动和旋转过程中似乎考虑光照影响，不同表面的明暗程度在拖动过程中有变化
'''
def OfficialExample():
    '''调用pyvista模块内置的class，绘制基本图形
    :return: None
    '''
    cyl = pv.Cylinder()
    arrow = pv.Arrow()
    sphere = pv.Sphere()
    plane = pv.Plane()
    line = pv.Line()
    box = pv.Box()
    cone = pv.Cone()
    poly = pv.Polygon()
    disc = pv.Disc()

    p = pv.Plotter(shape=(3, 3)) # 设置3*3的矩阵格，上述图形在统一显示平面显示
    # Top row
    p.subplot(0, 0) # 坐标值
    p.add_mesh(cyl, color="tan", show_edges=True)
    p.subplot(0, 1)
    p.add_mesh(arrow, color="tan", show_edges=True)
    p.subplot(0, 2)
    p.add_mesh(sphere, color="tan", show_edges=False)
    # Middle row
    p.subplot(1, 0)
    p.add_mesh(plane, color="tan", show_edges=True)
    p.subplot(1, 1)
    p.add_mesh(line, color="tan", line_width=3)
    p.subplot(1, 2)
    p.add_mesh(box, color="tan", show_edges=True)
    # Bottom row
    p.subplot(2, 0)
    p.add_mesh(cone, color="tan", show_edges=True)
    p.subplot(2, 1)
    p.add_mesh(poly, color="tan", show_edges=True)
    p.subplot(2, 2)
    p.add_mesh(disc, color="tan", show_edges=True)
    # Render all of them
    p.show()

'''
小Tips：
random模块的rand生成的默认范围为0-1，因此点数越多，越接近于正方体
'''
def PointCloud():
    '''pyvista借助PolyData绘制三维空间点云
    :return:None 
    '''
    points = np.random.rand(100000, 3) # 生成1000个xyz坐标
    mesh = pv.PolyData(points) # PolyData对象的实例化
    mesh.plot(point_size=2, style='points')

# # 平面绘制
# # most meshes have some sort of connectivity between points

def HexbeamPlot():
    '''pyvista的example中六角梁绘制
    :return: None
    '''
    mesh = examples.load_hexbeam() # 导入模型
    print(mesh)
    cpos = [(6.20, 3.00, 7.50),
            (0.16, 0.13, 2.65),
            (-0.28, 0.94, -0.21)]

    pl = pv.Plotter() # Plotter class 实例化
    pl.add_mesh(mesh, show_edges=True, color='white') # 绘制图像
    pl.add_points(mesh.points, color='red',
                  point_size=5) # 标明红色点
    pl.camera_position = cpos # 指明观察的位置和角度
    pl.show()


'''
小Tips：
模型下载需要连接外网，必须科学上网，才能正确绘制图形
否则报错：TimeoutError: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。
'''
def BunnyCoarsePlot():
    '''pyviata复杂的兔子模型绘制
    :return: None
    '''
    mesh1 = examples.download_bunny_coarse()
    mesh = pv.PolyData(mesh1.points)
    print(mesh)
    print('-----------------------')
    print(mesh.points)

    pl = pv.Plotter()
    pl.add_mesh(mesh, show_edges=True, color='white')
    pl.add_points(mesh.points, color='red',
                  point_size=2)
    pl.camera_position = [(0.02, 0.30, 0.73),
                          (0.02, 0.03, -0.022),
                          (-0.03, 0.94, -0.34)]
    pl.show()

'''
PolyData (0x2e685813d00)
  N Cells:	872
  N Points:	872
  X Bounds:	-1.316e-01, 1.802e-01
  Y Bounds:	-1.205e-01, 1.877e-01
  Z Bounds:	-1.430e-01, 9.851e-02
  N Arrays:	0
  
PolyData (0x21948e57340)
  N Cells:	1000
  N Points:	872
  X Bounds:	-1.316e-01, 1.802e-01
  Y Bounds:	-1.205e-01, 1.877e-01
  Z Bounds:	-1.430e-01, 9.851e-02
  N Arrays:	1 

'''



def CellPlot():
    '''绘制六角梁并突出其中的一个Cell
    :return: None
    '''
    mesh = examples.load_hexbeam()
    # 模型六角梁绘制
    pl = pv.Plotter() # 类的实例化(做画图前的准备)
    pl.add_mesh(mesh, show_edges=True, color='white')
    pl.add_points(mesh.points, color='red', point_size=20)
    # 六角梁上描述特定的某一个cell
    single_cell = mesh.extract_cells(mesh.n_cells - 1) # 指定哪一个具体的cell
    pl.add_mesh(single_cell, color='pink', edge_color='blue',
                line_width=5, show_edges=True)

    pl.camera_position = [(6.20, 3.00, 7.50),
                          (0.16, 0.13, 2.65),
                          (-0.28, 0.94, -0.21)]

    pl.show()

'''
cube.cell_data中包含诸多有关于pyvista DataSetAttributes的参数
应该是可以进行一些绘图参数的调整和设置
'''
def CubePlot():
    cube = pv.Cube()
    cube.cell_data['myscalars'] = range(6)
    print(cube.cell_data)

    other_cube = cube.copy()
    other_cube.point_data['myscalars'] = range(8)

    pl = pv.Plotter(shape=(1, 2), border_width=1)
    pl.add_mesh(cube, cmap='coolwarm')
    pl.subplot(0, 1)
    pl.add_mesh(other_cube, cmap='coolwarm')
    pl.show()

'''
与上述兔子的绘制相同，同样需要科学上网才能成功下载模型
'''
def PlotDragon():
    mesh = examples.download_dragon()
    mesh['scalars'] = mesh.points[:, 1]
    mesh.plot(cpos='xy', cmap='plasma', pbr=True, metallic=1.0, roughness=0.6,
              zoom=1.7)

'''
借助于pyvista绘制甜甜圈
'''
def SuperToroid():
    supertoroid = pv.ParametricSuperToroid(n1=0.5)
    supertoroid.plot(color="tan", smooth_shading=True)

'''
高阶点云绘制，点云绘制完成后赋值赋予不同的颜色
'''
def AdvancedPointCloud():
    '''点云赋值
    :return: None
    '''
    ## 生成一组点云的坐标，然后构建点云的mesh
    points = np.random.rand(30000, 3)
    point_cloud = pv.PolyData(points)
    print(np.allclose(points, point_cloud.points))  # 检测是否一致
    # 画点云
    # point_cloud.plot(eye_dome_lighting=True)
    ## 给点云赋值，这里就把z轴坐标的值赋值给点云
    data = points[:, -1]
    point_cloud["value"] = data
    point_cloud.plot(render_points_as_spheres=True)


'''
借助于pyvista绘制多面体
'''
def PlotTest():
    '''多面体
        :return:None 
        '''
    # mesh points
    vertices = np.array([[0, 0, 0],
                         [1, 0, 0],
                         [1, 1, 0],
                         [0, 1, 0],
                         [0.5, 0.5, -1]])

    # mesh faces,这个还不知道是什么意思，怎么定义？
    faces = np.hstack([[4, 0, 1, 2, 3],  # square
                       [3, 0, 1, 4],  # triangle
                       [3, 1, 2, 4]])  # triangle

    surf = pv.PolyData(vertices, faces)
    surf.cell_data['scalars'] = np.arange(3)
    # plot each face with a different color
    # surf.plot(scalars=np.arange(3), cpos=[-1, 1, 0.5])

    p = pv.Plotter()  ## 建一个普通画板
    # p = pv.BackgroundPlotter() ## 建一个交互式画板
    p.camera_position = [-1, 1, 0.5]
    p.add_mesh(surf)
    p.show()

'''
借助于pyvista绘制三维图像
'''
def SurfPlotting():
    '''绘制三维图像
    :return:None 
    '''
    x = np.arange(-10, 10, 0.25)
    y = np.arange(-10, 10, 0.25)
    x, y = np.meshgrid(x, y)
    r = np.sqrt(x ** 2 + y ** 2)
    z = np.sin(r)

    grid = pv.StructuredGrid(x, y, z)
    grid.plot()


def selfTest():
    mesh = examples.download_bunny_coarse()
    points = mesh.points
    mesh = pv.PolyData(points)  # PolyData对象的实例化
    mesh.plot(point_size=2, style='points')

def main():
    # OfficialExample()
    # PointCloud()
    # HexbeamPlot()
    # BunnyCoarsePlot()
    # CellPlot()
    # CubePlot()
    # selfTest()
    PlotDragon()
    # SuperToroid()
    # AdvancedPointCloud()
    # PlotTest()
    # SurfPlotting()
    pass

if __name__ == '__main__':
    main()



