# code/ch2/4_color.py
import py5

# 初始化滑块位置
def setup():
    py5.size(600, 400)
    py5.background(255, 0, 0)  # 设置背景颜色为红色
    
    py5.stroke_weight(10)  # 设置描边宽度为10像素
    
    py5.stroke(0, 255, 0)  # 设置描边颜色为绿色
    py5.point(50, 50)  # 绘制一个点，位置在(50, 50)
    
    py5.stroke(0, 0, 255)  # 设置描边颜色为蓝色
    py5.point(100, 100)  # 绘制一个点，位置在(100, 100)
  
def draw():
    pass

# 运行程序
py5.run_sketch()