# Author:qyan.li
# Date:2022.3.8
# Topic:借助于python三方库pyopengl实现3D图像绘制
# Reference:https://blog.csdn.net/san1156/article/details/74923025
#           https://eyehere.net/2011/learn-opengl-3d-by-pyopengl-3/

### 使用PyOpenGL叩开3D的心扉-OpenGL全解析(1)
'''
1. OpenGL(全写为Open Graphics Library) 用于生成二维和三维图像
2. PyOpenGL是OpenGl在python中的调用
'''
### 使用PyOpenGL叩开3D的心扉-OpenGL全解析(2)
'''
提及重要概念：透视，光照，纹理，阴影等等
'''
## 使用PyOpenGL叩开3D的心扉-OpenGL全解析(3)
# # pyopengl绘制茶壶-基本命令解析
# from OpenGL.GL import *
# from OpenGL.GLU import *
# from OpenGL.GLUT import *
#
# def drawFunc():
#     '''OpenGl实际绘图函数'''
#     glClear(GL_COLOR_BUFFER_BIT) # 将先前的画面清除，参数指明要清除的buffer
#     # glRotatef(1, 0, 1, 0)
#     glutWireTeapot(0.5) # glut提供的绘制‘犹他茶壶’的函数(glut内部函数)
#     glFlush() # 刷新显示(内部复杂)
#
# glutInit() # 借助于glut初始化opengl
# '''GLUT_SINGLE所有绘图操作都直接在显示的窗口执行，GLUT_RGBA说明采用RGB的颜色显示方式'''
# glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
# glutInitWindowSize(400, 400) # 设置窗口大小(glutInitWindowPosition设置窗口出现的位置)
# glutCreateWindow("First") # 创建窗口，添加标题
# glutDisplayFunc(drawFunc) # 执行函数(函数中包含openGl的诸多基础绘图操作)
# # glutIdleFunc(drawFunc)
# glutMainLoop() # 主循环，画出即时的图像，处理输入等


# ## 绘制旋转的犹他茶壶
# from OpenGL.GL import *
# from OpenGL.GLU import *
# from OpenGL.GLUT import *
#
# def drawFunc():
#     glClear(GL_COLOR_BUFFER_BIT)
#     glRotatef(1, 0, 1, 0) # 参数说明：角度+向量(绕向量旋转一定的角度)
#     glutWireTeapot(0.5)
#     glFlush()
#
# glutInit()
# glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
# glutInitWindowSize(400, 400)
# glutCreateWindow("First")
# glutDisplayFunc(drawFunc)
# glutIdleFunc(drawFunc) # 动画产生
# glutMainLoop()



### 使用PyOpenGL叩开3D的心扉-OpenGL全解析(4)
'''PyOpengl学习
+ OpenGl所有的绘图指令，均必须包含在glBegin()和glEnd()之间，glBegin()中的参数决定点的最终绘制方法
+ glBegin()常用的参数举例 单个顶点集，线段等等
'''

# openGl基础元素绘制：

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

### 使用PyOpenGL叩开3D的心扉-OpenGL全解析(5)
# from OpenGL.GL import *
# from OpenGL.GLU import *
# from OpenGL.GLUT import *
# #from numpy import *
# import sys
#
# def init():
#     glClearColor(1.0, 1.0, 1.0, 1.0)
#     gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
#
# def plotfunc():
#     glClear(GL_COLOR_BUFFER_BIT)
#     glPointSize(3.0) # 仅仅会影响所绘制点的大小，对于线(坐标轴)没有任何影响，线的粗细，借助于glLineWidth
#
#     glColor3f(1.0, 0.0, 1.0)
#     glBegin(GL_LINES) # 绘制坐标轴
#     glVertex2f(-5.0, 0.0)
#     glVertex2f(5.0, 0.0)
#     glVertex2f(0.0, 5.0)
#     glVertex2f(0.0, -5.0)
#     glEnd()
#
#     glColor3f(0.0, 0.0, 0.0)
#     glBegin(GL_POINTS) # 绘制图像中各个点
#     #for x in arange(-5.0, 5.0, 0.1):
#     for x in (i * 0.1 for i in range(-50, 50)):
#         y = x*x
#         glVertex2f(x, y)
#     glEnd()
#
#     glFlush()
#
# def main():
#     glutInit(sys.argv)
#     glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
#     glutInitWindowPosition(50,50)
#     glutInitWindowSize(400,400)
#     glutCreateWindow("Function Plotter")
#     glutDisplayFunc(plotfunc)
#     init()
#     glutMainLoop()
#
# main()


