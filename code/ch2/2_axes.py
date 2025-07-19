# code/ch2/2_axes.py
import py5

def setup(): # setup()函数在程序开始时执行一次，通常用于初始化设置
    py5.size(400, 400)  # 设置画布大小为400x400像素
    
    py5.stroke_weight(10)
    py5.stroke(255, 0, 0)  # 设置描边颜色为红色
    py5.point(50, 60)  # 绘制一个点，位置在(50, 60)，大小为10像素
    
    py5.stroke(0, 255, 0)  # 设置描边颜色为绿色
    py5.point(-50, -60)  # 绘制一个点，位置在(-50, -60)，大小为10像素
    
    py5.stroke(0, 0, 255)  # 设置描边颜色为蓝色
    py5.point(100, 100)  # 绘制一个点，位置在(100, 100)，大小为10像素
    
    
def draw(): # draw()函数在setup()之后循环执行，通常用于绘制动画或动态效
    pass

py5.run_sketch()  # 启动Py5程序，执行setup()和draw()函数