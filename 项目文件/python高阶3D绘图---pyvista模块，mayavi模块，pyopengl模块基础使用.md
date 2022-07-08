### python高阶3D绘图---pyvista模块，mayavi模块，pyopengl模块基础使用

---

> Author:qyan.li
>
> Date:2022.6.28
>
> Topic:借助于python进行3D绘图，主要涉及pyvista,mayavi,pyopengl,moviepy模块的基础使用

#### 一、python三维绘图

​	``python``借助于其编写简单，三方库丰富的特点，可以极为方便的进行数据的分析和图像的绘制，在三维绘图方面，``python``同样具有诸多优秀的三方库供大家使用，下面进行简单的介绍，深入了解请查看官方文档，或查阅其他文章。

+ ``pyvista``模块：

  + 简单介绍：

    ​	``Pyvista``是可视化工具包(``VTK-Visualization Toolkit``)的高级``API``，用户可借助此``API``完成复杂的3D图形绘制，功能较为强大。在``Pyvista``给出的官方文档中，提供多种绘图``Demo``，具体详见：[Examples — PyVista 0.33.0 documentation](https://docs.pyvista.org/examples/index.html)。

  + 模块应用：

    1. 基础示例Demo：

       ```python
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
       ```

       <img src = "C:\Users\腻味\Desktop\图片生成\Pyviata\GeometricObjects.png" style = "zoom:50%">

       由上述基础示例``Demo``，可以总结出``Pyvista``绘制``3D``图形的一般步骤：

       > 前提说明：
       >
       > ​	mesh是pyvista模块绘制时的重点部分，官方文档中定义为any spatially referenced dataset as a mesh,usually consists of geometrical representations of s surface or volumn in space.个人理解mesh为三维空间中一系列数据的集合，通常可以包含若干三维空间集合图形。
       >
       > 一般步骤：
   >
       > 1. 模块导入：import pyvista as pv
   > 2. 设置画布：p = pv.Plotter(shape=(3, 3))，画布的大小格局可以自行进行设计
       > 3. 调用add_mesh()函数进行图形绘制，内部传入事先实例化的基础图形对象
    
       关于此示例Demo的小Tips：
    
     > 小Tips：
       >
     > + 上述图形可以借助于鼠标进行动态的交互，可以借助于鼠标推拽转换角度和方位
       > + 图形在调整过程中存在光影的变换，不同的面亮暗程度会发生改变
    
    2. Point_cloud点云绘制：
    
       ```python
       def PointCloud():
           '''pyvista借助PolyData绘制三维空间点云
           :return:None 
           '''
           points = np.random.rand(100000, 3) # 生成1000个xyz坐标
           mesh = pv.PolyData(points) # PolyData对象的实例化
           mesh.plot(point_size=2, style='points')
       ```
    
       <img src = "C:\Users\腻味\Desktop\PointCloud_pyvista.png" style = "zoom:30%">
    
       > 小Tips：
       >
       > + 官方文档中，关于point的定义：points are the vertices of the mesh，点云绘制是独立的将每一个点显示在三维空间中，形成点云point-cloud
       > + 此处points是由random模块随机生成，因此生成的点数越多，绘制出的图形越接近正方体
    
    3. 基础图形绘制
    
       ```python
       def HexbeamPlot():
           '''pyvista的example中六角梁绘制
           :return: None
           '''
           mesh = examples.load_hexbeam() # 导入模型
           cpos = [(6.20, 3.00, 7.50),
                   (0.16, 0.13, 2.65),
                   (-0.28, 0.94, -0.21)]
       
           pl = pv.Plotter() # Plotter class 实例化
           pl.add_mesh(mesh, show_edges=True, color='white') # 绘制图像
           pl.add_points(mesh.points, color='red',
                         point_size=5) # 标明红色点
           pl.camera_position = cpos # 指明观察的位置和角度
           pl.show()
       ```
    
       <img src = "C:\Users\腻味\Desktop\hexgeam_pyvista.png" style = "zoom:30%">
    
        
    
       > 小Tips：
       >
       > + 此处导入pyvista中现有的模型-六角梁，实际上下载下的mesh为一种UnstructedGrid的类型，猜测属于VTK的特定的数据类型
       > + 主要使用两个方法：add_mesh绘制图形，add_point在图形上标注特定的点
    
       ----
    
       ​	这里分界线，下面在上述六角梁的基础上标记出某一个cell来，便于大家理解pyvista绘图的主要要素：
    
       ```python
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
       ```
    
       <img src = "C:\Users\腻味\Desktop\cell&Hexgem_pyvista.png" style = "zoom:30%">
    
       > 小Tips：
       >
       > + 上述蓝色小框突出的位置即为一个小cell，官方文档中对于cell的界定为A cell is the geomerty between points that defines the connectivity or topology of a mesh. 按照自己的理解，cell是由若干点及其连接关系组成的小部分
    
    ----
    
    ​	上述提及展示的几点也是pyvista官方文档中提及的绘图要素要素：mesh,point,cell，下面可以展示一些较为高阶复杂的图形绘制。
    
    + BunnyCoaser绘制
    
      ```python
      def BunnyCoarsePlot():
          '''pyviata复杂的兔子模型绘制
          :return: None
          '''
          mesh = examples.download_bunny_coarse()
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
      ```
    
      <img src = "C:\Users\腻味\Desktop\BunnyCoarse.png" style = "zoom:30%">
    
      > 小Tips：
      >
      > + pyvista初次下载模型时，可能需要科学上网，否则报错
      >
      >   错误显示：TimeoutError: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。
      >
      > + mesh输出：
      >
      >   PolyData (0x223e4567340)
      >     N Cells:	1000
      >     N Points:	872
      >     X Bounds:	-1.316e-01, 1.802e-01
      >     Y Bounds:	-1.205e-01, 1.877e-01
      >     Z Bounds:	-1.430e-01, 9.851e-02
      >     N Arrays:	1
      >
      >   这个PolyData和上面点云类型一致，但是其中不仅仅包含mesh.points，还应该包含有点与点之间的连接情况等等，最后形成由面构成，否则就由点构成，类似于下面：
      >
      >   <img src = "C:\Users\腻味\Desktop\BunnyCoarsePoint_pyvista.png" style = "zoom:30%">
      >
      >   此时输出的PolyData为：
      >
      >   PolyData (0x2e685813d00)
      >     N Cells: 	872
      >     N Points:    872
      >     X Bounds:    -1.316e-01, 1.802e-01
      >     Y Bounds:    -1.205e-01, 1.877e-01
      >     Z Bounds:    -1.430e-01, 9.851e-02
      >     N Arrays:    0
      >
      >   代码修改：
      >
      >   ```python
      >   mesh1 = examples.download_bunny_coarse()
      >   mesh = pv.PolyData(mesh1.points)
      >   ```
    
    + Dragon绘制
    
      ```python
      def PlotDragon():
          mesh = examples.download_dragon()
          mesh['scalars'] = mesh.points[:, 1]
          mesh.plot(cpos='xy', cmap='plasma', pbr=True, metallic=1.0, roughness=0.6,
                    zoom=1.7)
      ```
    
      <img src = "C:\Users\腻味\Desktop\Dragon_pyvista.png" style = "zoom:30%">
    
      > 小Tips：
      >
      > + Dragon的绘制和上面BunnyCoaser的绘制相同，同样是下载模型，首次下载需要科学上网
  
  ----
  
  ​	上面是对pyvista模块绘图情况的简介，为获得更好的交互体验，可以到附录的代码中自行运行代码(其中还有部分模型不不在此展示)，更推荐大家移步官方文档查看学习。
  
  ​	做一个简单的总结：
  
  1. pyvista功能非常强大，从上面的BunnyCoarse和Dradon就可以略知一二，非常值得学习
  2. pyvista背倚VTK，可能需要其他的知识来辅助绘图操作，比如VTK的各种数据类型，结构等等，来进行高阶的自定义绘图（上面仅是调用现成的模型）
  
+ mayavi模块

  + 简单介绍：

    ​	mayavi同样也是python三维绘图方向一个非常优秀的模板库，但是仅就自己的体验而言，自己接触的或许比较浅显，个人感觉在mlab的应用层面，与matlab并没有过多本质上的区别。

    ​	官方文档中也有提及这一点：mayavi.mlab as done in the pylab interface but with an emphasis on 3D visulization，mayavi高阶深入的操作，移步官方文档：https://mayavi.readthedocs.io/zh_CN/latest/index.html

  + 简单应用：

    1. 三维曲面：

       ```python
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
       ```

       <img src = "C:\Users\腻味\Desktop\3D&surf_pyvista.png" style="zoom:30%;" >

       > 小Tips：
       >
       > + 绘图步骤类似于matlab：先生成xy面上的坐标点，而后借助于z坐标向上提拉形成三维空间的曲面
       > + mlab绘制的图形同样可以借助于鼠标进行动态的交互

    2. 复杂图形：

       ```python
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
           s = mlab.mesh(x, y, z,representation = 'surface',line_width = 1.0)
           mlab.outline(s) # 为图形添加边线
           mlab.show()
       ```

       <img src = "C:\Users\腻味\Desktop\Advanced-_mayavi.png" style="zoom:30%;" >

       > 小Tips：
       >
       > + 上述图像在mayavi中算是比较经典的图形，基本上任何mayavi教程都会提及，调用mesh函数进行绘制
       >
       > + mesh函数中存在representation的选项，surface默认绘制曲面，wireframe绘制边线，形成的图形为：
       >
       >   <img src = "C:\Users\腻味\Desktop\Advanced&wireframe_pyvista.png" style="zoom:30%;" >
       >
       >   此处故意放大一点图形，方便大家观察wireframe绘制边线的效果
       >
       > + 个人感觉，mlab图形绘制数学表达式依赖程度很高，个人认为这也是较大的一个限制

    3. 复杂图形：

       ```python
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
       ```

       <img src = "C:\Users\腻味\Desktop\using_pyvista.png" style="zoom:30%;" >

       > 这个与上面图形绘制类似，上面借助于mesh函数，此处借助于plot3d函数，同样依赖于数学表达式

    ------

    ​	上面我们看到一些关于mayavi图形绘制的一些经典案例，下面提及mlab中基础的三维绘图函数，类似于matlab

    + plot3d&&point3d函数：

      上述函数理论上讲是mayavi中最基本的两个函数，分别用于绘制三维空间中的点和线，plot3d用于将三维空间中的一个个点连接起来形成曲线，point3d则将三维空间中的一系列点独立的绘制出来

      ```python
      def Plot3dTest():
          '''测试mayavi中的plot3d，points3d函数
          :return: None
          '''
          x = np.arange(0,20,1)
          y = np.sin(x)
          z = y * np.sin(x)
      
          # plot3d和points3d参数传入一维坐标点，绘制三维空间中的一系列点或者曲线
          mlab.plot3d(x,y,z,color = (1,0,0),tube_radius = 0.1) # 参数指明圆管的粗细
          # mlab.points3d(x,y,z,color = (1,0,1)) # 颜色指定(可以取间隔大，方便观察区别)
          mlab.show()
      ```

      > 1. plot3d函数
      >
      >    <img src = "C:\Users\腻味\Desktop\plot3d.png" style="zoom:30%;" >
      >
      > 2. point3d函数：
      >
      >    <img src = "C:\Users\腻味\Desktop\point3d.png" style="zoom:30%;" >
      >
      > 小总结：
      >
      > + 在二维空间中为点，转化至此处称为球，这一点在point3d函数的应用中可以得到印证
      > + plot3d的绘制原则也是将一系列的点连接起来，点数过少，过于稀疏，绘制出来并非曲线，而是折线

    + imshow&&surf&&contour_surf函数：

      上述函数分别用于绘制三维彩色图，曲线图，登高图，日常绘图应该不太会应用，可能在一些特定的场合应用作用可能会比较大。

      ```python
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
      ```

      > 1. imshow函数
      >
      >    <img src = "C:\Users\腻味\Desktop\二维色彩图.png" style="zoom:30%;" >
      >
      > 2. surf函数
      >
      >    <img src = "C:\Users\腻味\Desktop\三维曲面.png" style="zoom:30%;" >
      >
      > 3. contour_surf函数
      >
      >    <img src = "C:\Users\腻味\Desktop\二维等高线.png" style="zoom:30%;" >
      >
      >    小Tips：
      >
      >    此时等高线是三维的，借助于鼠标拖动即可看出所处的高度层不同

    + barchart函数

      barchart用于在三维空间中绘制柱体图，与matlab中的bar3d函数相对应

      ```python
      def barchartTest():
          '''barchart函数
          :return: None
          '''
          s = np.random.rand(3, 3)
          mlab.barchart(s) # 生成三维空间中的柱状图
          mlab.vectorbar() # 附颜色带
          mlab.show()
      ```

      <img src = "C:\Users\腻味\Desktop\barchart.png" style="zoom:30%;" >

    + contour3d函数

      contour3d函数绘制三维空间中的等高面，与前面contour_surf相对应

      ```python
      def contour3dTest():
          '''contour3d函数
          :return: None
          '''
          x, y, z = ogrid[-5:5:64j, -5:5:64j, -5:5:64j]
          scalars = x * x * 0.5 + y * y + z * z * 2.0
          mlab.contour3d(scalars, contours=6, transparent=True)
          mlab.colorbar()
          mlab.show()
      
      ```

      <img src = "C:\Users\腻味\Desktop\contour3d.png" style="zoom:30%;" >

  ----------

  ​	上述是对mayavi绘图的基本简介，主要是针对于mlab部分进行讲解，更高阶的功能，深入的了解移步官方文档，简单的总结一下：

  1. mlab功能类似于matlab，但是针对于三维绘图功能进行强化，在python3D绘图领域优秀的模块
  2. mlab较为依赖数学公式，针对于复杂生活场景的建模能力不足，当然mayavi应该有其他的解决方案

+ pyopengl模块：

  + 简单介绍：

    ​	pyopengl是opengl的pythonAPI，opengl相信很多人都听说过，OpenGl的全称为Open Graphics Library，常用于二维和三维图像的绘制。

    ​	本文的OpenGl介绍使用并未以官方文档为参考(自己太菜，看着实在是心态崩溃)，此处以网络上大佬的博客(https://eyehere.net/2011/learn-opengl-3d-by-pyopengl-3/)为参考学习，同时对内容进行简要的总结，详细的内容请参考官方文档或者检索其他参考文献。

    ​	OpenGl更加普遍广泛的为C++调用，大家也可以参考C++的调用方式，和Python的差异不会太大。

  + 模块安装：

    ​	此处提一下pyopengl的安装，是因为此模块并不能简单的按照pip install pyopengl的方式进行安装，需要下载镜像文件进行安装，参考文献：https://blog.csdn.net/xufive/article/details/86565130

    ​	个人在安装过程中曾遇到安装失败，报错显示The file is not supported on the platform，最后发现由于下载的镜像文件与个人电脑的python版本不匹配造成的，详细的解决方案参考：https://www.jianshu.com/p/531c4fdbb493

  + 简单应用:

    1. 茶壶小Demo：

       ```python
       # pyopengl绘制茶壶-基本命令解析
       from OpenGL.GL import *
       from OpenGL.GLU import *
       from OpenGL.GLUT import *
       
       def drawFunc():
           '''OpenGl实际绘图函数'''
           glClear(GL_COLOR_BUFFER_BIT) # 将先前的画面清除，参数指明要清除的buffer
           # glRotatef(1, 0, 1, 0)
           glutWireTeapot(0.5) # glut提供的绘制‘犹他茶壶’的函数(glut内部函数)
           glFlush() # 刷新显示(内部复杂)
       
       glutInit() # 借助于glut初始化opengl
       '''GLUT_SINGLE所有绘图操作都直接在显示的窗口执行，GLUT_RGBA说明采用RGB的颜色显示方式'''
       glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
       glutInitWindowSize(400, 400) # 设置窗口大小(glutInitWindowPosition设置窗口出现的位置)
       glutCreateWindow("First") # 创建窗口，添加标题
       glutDisplayFunc(drawFunc) # 执行函数(函数中包含openGl的诸多基础绘图操作)
       # glutIdleFunc(drawFunc)
       glutMainLoop() # 主循环，画出即时的图像，处理输入等
       ```

       <img src = "C:\Users\腻味\Desktop\TeaPlot.png" style="zoom:50%;" >

       > 小Tips：
       >
       > + 此处并为展示任何绘图的技巧，茶壶的绘制调用内部的WireTeapot函数实现，可以借此了解pyopengl绘制图形的一般思路
       > + 此处绘制的茶壶为静态的，同时不支持借助于鼠标动态交互

    2. 动态茶壶小Demo：

       ```python
       ## 绘制旋转的犹他茶壶
       from OpenGL.GL import *
       from OpenGL.GLU import *
       from OpenGL.GLUT import *
       
       def drawFunc():
           glClear(GL_COLOR_BUFFER_BIT)
           glRotatef(1, 0, 1, 0) # 参数说明：角度+向量(绕向量旋转一定的角度)
           glutWireTeapot(0.5)
           glFlush()
       
       glutInit()
       glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
       glutInitWindowSize(400, 400)
       glutCreateWindow("First")
       glutDisplayFunc(drawFunc)
       glutIdleFunc(drawFunc) # 动画产生
       glutMainLoop()
       ```

       <img src = "C:\Users\腻味\Desktop\2022-07-07-10-21-59_.gif" style="zoom:50%;" >

       > 小Tips：
       >
       > 动态旋转的茶壶小Demo添加两行代码：
       >
       > ``glRotatef(1,0,1,0)``用于说明围绕特定向量旋转的角度
       >
       > ``glutIdelFunc(drawFunc)``用于生成动画

    3. ```python
       from OpenGL.GL import *
       from OpenGL.GLU import *
       from OpenGL.GLUT import *
       
       def init():
           glClearColor(0.0, 0.0, 0.0, 1.0)
           gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
       
       def drawFunc():
           glClear(GL_COLOR_BUFFER_BIT)
       
           glBegin(GL_LINES) # 分割线绘制(未指定颜色，前景白色，背景黑色)
           glVertex2f(-1.0, 0.0)
           glVertex2f(1.0, 0.0)
           glVertex2f(0.0, 1.0)
           glVertex2f(0.0, -1.0)
           glEnd()
       
           glPointSize(5.0) # 指明每个像素点的大小为5
           glBegin(GL_POINTS) # 右上部分点的绘制(指定坐标和颜色)
           glColor3f(1.0, 0.0, 0.0)
           glVertex2f(0.3, 0.3)
           glColor3f(0.0, 1.0, 0.0)
           glVertex2f(0.6, 0.6)
           glColor3f(0.0, 0.0, 1.0)
           glVertex2f(0.9, 0.9)
           glEnd()
       
           '''仔细观察，默认情况下，封闭图形会被填充'''
           glColor3f(1.0, 1.0, 0) # 绘制指定颜色的独立四边形(矩形)
           glBegin(GL_QUADS)
           glVertex2f(-0.2, 0.2)
           glVertex2f(-0.2, 0.5)
           glVertex2f(-0.5, 0.5)
           glVertex2f(-0.5, 0.2)
           glEnd()
       
           glColor3f(0.0, 1.0, 1.0)
           glPolygonMode(GL_FRONT, GL_LINE) # 指定绘制面的方式(GL_LINE只画线，GL_FILL进行填充)
           glPolygonMode(GL_BACK, GL_FILL)
           glBegin(GL_POLYGON)
           glVertex2f(-0.5, -0.1)
           glVertex2f(-0.8, -0.3)
           glVertex2f(-0.8, -0.6)
           glVertex2f(-0.5, -0.8)
           glVertex2f(-0.2, -0.6)
           glVertex2f(-0.2, -0.3)
           glEnd()
       
           '''两端代码的区别在于面的渲染，类似于刷油漆，在正面刷和在反面刷的区别'''
           '''此处面理解为是的3D面，正面渲染是可以看到的，但是背面的渲染是无法观察到的'''
       
           glPolygonMode(GL_FRONT, GL_FILL)
           glPolygonMode(GL_BACK, GL_LINE)
           glBegin(GL_POLYGON)
           glVertex2f(0.5, -0.1)
           glVertex2f(0.2, -0.3)
           glVertex2f(0.2, -0.6)
           glVertex2f(0.5, -0.8)
           glVertex2f(0.8, -0.6)
           glVertex2f(0.8, -0.3)
           glEnd()
       
           glFlush()
       
       glutInit()
       glutInitDisplayMode(GLUT_RGBA|GLUT_SINGLE)
       glutInitWindowSize(400, 400)
       glutCreateWindow("Sencond")
       
       glutDisplayFunc(drawFunc)
       init()
       glutMainLoop()
       ```

       <img src = "C:\Users\腻味\Desktop\基础元素.png" style="zoom:50%;" >

       借助于此部分，我们的对于``PyOpenGL``的基础绘图操作做简单的归纳总结：

       > - ``OpenGL``的所有绘图命令必须在``glBegin()和glEnd()``之间，同时，``glBengin()``中的参数知名绘图的方式
       >
       >   > 1. ``GL_LINES``表示绘制线端
       >   > 2. ``GL_POINTS``表示绘制单个顶点集
       >   > 3. ``GL_QUADS``表示绘制独立四边形
       >   > 4. ``GL_POLYGON``表示绘制多边形
       >   >
       >   > 其他绘制方式参考官方文档或者博客
       >
       > - 上述代码最后若干行属于对``OpenGL``的绘图窗口，主循环等等进行设置，绘制图形时必备，内部参数可发生改变
       >
       > - 上图中下面两幅图，作者用于说明``OpenGL``中的渲染问题，简单讲，由于绘制图像的3D特性，存在正面和反面之分，渲染可以理解为涂色，正面的涂色我们是可以看到的，但是背面的涂色我们是无法看到的

    4. 结尾Demo：

       ```python
       from OpenGL.GL import *
       from OpenGL.GLUT import *
       
       
       def draw():
           # ---------------------------------------------------------------
           glBegin(GL_LINES)  # 开始绘制线段（世界坐标系）
       
           # 以红色绘制x轴
           glColor4f(1.0, 0.0, 0.0, 1.0)  # 设置当前颜色为红色不透明
           glVertex3f(-0.8, 0.0, 0.0)  # 设置x轴顶点（x轴负方向）
           glVertex3f(0.8, 0.0, 0.0)  # 设置x轴顶点（x轴正方向）
       
           # 以绿色绘制y轴
           glColor4f(0.0, 1.0, 0.0, 1.0)  # 设置当前颜色为绿色不透明
           glVertex3f(0.0, -0.8, 0.0)  # 设置y轴顶点（y轴负方向）
           glVertex3f(0.0, 0.8, 0.0)  # 设置y轴顶点（y轴正方向）
       
           # 以蓝色绘制z轴
           glColor4f(0.0, 0.0, 1.0, 1.0)  # 设置当前颜色为蓝色不透明
           glVertex3f(0.0, 0.0, -0.8)  # 设置z轴顶点（z轴负方向）
           glVertex3f(0.0, 0.0, 0.8)  # 设置z轴顶点（z轴正方向）
       
           glEnd()  # 结束绘制线段
       
           # ---------------------------------------------------------------
           glBegin(GL_TRIANGLES)  # 开始绘制三角形（z轴负半区）
       
           glColor4f(1.0, 0.0, 0.0, 1.0)  # 设置当前颜色为红色不透明
           glVertex3f(-0.5, -0.366, -0.5)  # 设置三角形顶点
           glColor4f(0.0, 1.0, 0.0, 1.0)  # 设置当前颜色为绿色不透明
           glVertex3f(0.5, -0.366, -0.5)  # 设置三角形顶点
           glColor4f(0.0, 0.0, 1.0, 1.0)  # 设置当前颜色为蓝色不透明
           glVertex3f(0.0, 0.5, -0.5)  # 设置三角形顶点
       
           glEnd()  # 结束绘制三角形
       
           # ---------------------------------------------------------------
           glFlush()  # 清空缓冲区，将指令送往硬件立即执行
       
       
       if __name__ == "__main__":
           glutInit()  # 1. 初始化glut库
           glutCreateWindow('Quidam Of OpenGL')  # 2. 创建glut窗口
           glutDisplayFunc(draw)  # 3. 注册回调函数draw()
           glutMainLoop()  # 4. 进入glut主循环
       ```

       <img src ="C:\Users\腻味\Desktop\结尾Demo.png" style="zoom:50%;" >

  ---

  ​	pyopengl讲述内容不多，主要原因是因为我自己确实也是没怎么弄懂，相比于我更推荐大家去看大佬的博客，写的比较详细，后续应该也会更新。简单总结一下：

  1. 相比于上面两模块，pyopengl的可塑性应该是最强大，可以自定义光照，位置等的影响
  2. 可塑性强，自由灵活，那就意味着自己考虑，操作的部分非常多，上手的难度大，可适当参考视频教程，或许要容易些

#### 二、python动画生成

​	上述介绍python中三维绘图的模块，下面提及如何将绘制的图像转换为动画，当然也是借助于python的库完成-MoviePy。MoviePy是python的一个专业的音视频编辑库。我们可以借助于MoviePy将我们绘制的图形变为动态的动画。MoviePy的官方文档中提及选择MoviePy的一大理由在于你想将从别的Python库里（如Matplotlib、Mayavi、Gizeh、scikit-images等）生成的图片制作成动画。

​	当然，我们此处仅是落脚于MoviePy与绘图模块的交互的部分，但是MoviePy的功能远不止此，其他更多的功能，请移步官方文档：http://doc.moviepy.com.cn/index.html#document-3_%E4%BD%9C%E5%93%81%E5%B1%95%E7%A4%BA/index

+ MoviePy模块应用：

  1. moviepy和mayavi交互动画生成：

     ```python
     # 借助于Moviepy和mayavi实现3D动态图
     import numpy as np
     import mayavi.mlab as mlab
     import  moviepy.editor as mpy
     
     duration= 2 # duration of the animation in seconds (it will loop)
     
     # 用Mayavi制作一个图形
     fig_myv = mlab.figure(size=(220,220), bgcolor=(1,1,1))
     X, Y = np.linspace(-2,2,200), np.linspace(-2,2,200)
     XX, YY = np.meshgrid(X,Y)
     ZZ = lambda d: np.sinc(XX**2+YY**2)+np.sin(XX+d)
     
     # 用MoviePy将图形转换为动画，编写动画GIF
     
     def make_frame(t):
         mlab.clf() # 清掉图形（重设颜色）
         mlab.mesh(YY,XX,ZZ(2*np.pi*t/duration), figure=fig_myv)
         return mlab.screenshot(antialiased=True)
     
     animation = mpy.VideoClip(make_frame, duration=duration)
     animation.write_gif("sinc.gif", fps=20)
     ```

     图形展示：<img src="C:\Users\腻味\Desktop\MovieTest\sinc.gif" alt="sinc" style="zoom:150%;" />

  2. moviepy和matplotlib交互动画生成：

     ```python
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
     ```

     图形展示：

     <img src="C:\Users\腻味\Desktop\MovieTest\matplotlib.gif" alt="matplotlib" style="zoom:50%;" />

     > 小``Tips：``
     >
     > - ``moviepy``生成的动画不仅可以借助``animation.write_gif('matplotlib.gif', fps=20)``生成``gif``文件，同样可以借助``animation.write_videofile('matplotlib.mp4',fps = 24)``生成视频文件。
     > - ``duration``定义图形速度的变化，数值越小，图像的变化速度越快
     > - ``make_frame``

  