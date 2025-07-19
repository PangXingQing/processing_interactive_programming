# code/ch2/1_point.py
import py5

def setup(): # setup()函数在程序开始时执行一次，通常用于初始化设置
    py5.size(400, 400)  # 设置画布大小为400x400像素
    
    py5.stroke_weight(10)
    py5.point(50, 50)  # 绘制一个点，位置在(200, 200)，大小为10像素
    
    # 连续绘制10个点，形成一条线
    for i in range(20):  # 循环20次
        py5.point(50 + i * 5, 100)
        
    # 绘制多个点，形成一个园
    for i in range(100):
        angle = py5.TWO_PI * i / 100  # 计算每个点的角度
        x = 200 + 50 * py5.cos(angle)  # 计算x坐标
        y = 200 + 50 * py5.sin(angle)  # 计算y坐标
        py5.point(x, y)  # 绘制点
    
def draw(): # draw()函数在setup()之后循环执行，通常用于绘制动画或动态效
    pass

py5.run_sketch()  # 启动Py5程序，执行setup()和draw()函数