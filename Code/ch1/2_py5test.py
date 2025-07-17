# 这是一个使用 Py5 库绘制矩形的 Processing 程序
import py5  # 引入第三方库，Py5，使用Py5包装好的Processing功能

def setup(): # def 表示设计了一个函数（功能模块），setup()是Processing的一个标准函数
    py5.size(400, 400) # 设置画布大小为400x400像素
    py5.background(255) # 设置背景颜色为白色
    py5.stroke(0) # 设置描边颜色为黑色
    py5.stroke_weight(2) # 设置描边宽度为2像素
    py5.fill(100, 150, 250) # 设置填充颜色为RGB(100, 150, 250)
    py5.rect(50, 50, 300, 300) # 绘制一个矩形，位置在(50, 50)，宽度和高度均为300像素

def draw():
    '''
    draw()函数在setup()之后循环执行，通常用于绘制动画或动态效果
    在这个例子中，draw()函数为空，因为我们只需要绘制一次静态矩形
    '''
    pass # pass语句表示什么都不做，留空函数体

py5.run_sketch() # 函数调用，运行Py5程序，开始执行setup()和draw()函数