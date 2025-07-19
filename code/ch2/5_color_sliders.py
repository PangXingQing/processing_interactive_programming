# code/ch2/5_color_sliders.py
import py5

# 全局变量
r, g, b, a = 128, 128, 128, 255  # 初始灰色，不透明
active_slider = None  # 当前被激活的滑块索引，0:R, 1:G, 2:B, 3:A

# 四个滑块的轨道位置和尺寸（x, y, 宽度, 高度）
slider_width = 300
slider_height = 20
sliders = []  # 每个元素是(x, y, width, height)，以及一个指向值的引用？实际上我们会用索引访问全局变量

# 初始化滑块位置
def setup():
    py5.size(600, 400)
    # 设置每个滑块的位置
    global sliders
    slider_x = (py5.width - slider_width) // 2  # 水平居中
    # 四个滑块垂直排列，顶部在预览矩形下方
    preview_bottom = 200 + 20  # 预览矩形底部再往下20像素
    slider_y0 = preview_bottom + 20  # 第一个滑块顶部位置
    gap = 40  # 每个滑块之间的垂直间距

    sliders = [
        (slider_x, slider_y0 + 0*gap, slider_width, slider_height),  # R
        (slider_x, slider_y0 + 1*gap, slider_width, slider_height),  # G
        (slider_x, slider_y0 + 2*gap, slider_width, slider_height),  # B
        (slider_x, slider_y0 + 3*gap, slider_width, slider_height)   # A
    ]

# 绘制每一帧
def draw():
    py5.background(200)  # 灰色背景

    # 绘制预览矩形
    py5.fill(r, g, b, a)
    py5.rect_mode(py5.CENTER)
    py5.rect(py5.width//2, 100, 400, 150)  # 中心在(300,100)位置

    # 绘制四个滑块
    py5.rect_mode(py5.CORNER)
    for i, (x, y, w, h) in enumerate(sliders):
        # 绘制轨道（灰色轨道，上面有一条当前值的标记）
        py5.fill(100)
        py5.rect(x, y, w, h)

        # 根据当前值计算滑块头位置（将0-255映射到轨道的x到x+w）
        slider_value = [r, g, b, a][i]
        head_x = py5.remap(slider_value, 0, 255, x, x+w)
        # 绘制滑块头（小圆点或者小矩形）
        py5.fill(255)
        py5.rect(head_x-5, y-5, 10, h+10)  # 滑块头略高于轨道

        # 显示滑块标签和当前值
        labels = ['R', 'G', 'B', 'A']
        py5.fill(0)
        py5.text_size(16)
        py5.text(f"{labels[i]}: {slider_value}", x-60, y+h//2+5)  # 在滑块左侧显示

# 鼠标按下事件
def mouse_pressed():
    global active_slider
    # 检查是否按在某个滑块头上（或轨道上）
    for i, (x, y, w, h) in enumerate(sliders):
        # 获取当前滑块值对应的滑块头位置
        slider_value = [r, g, b, a][i]
        head_x = py5.remap(slider_value, 0, 255, x, x+w)
        # 创建一个滑块头的矩形区域（扩展一些，容易点中）
        head_rect = (head_x-10, y-10, 20, h+20)
        # 或者简单点，检查鼠标是否在轨道矩形内（包括轨道和滑块头）
        # 我们检查鼠标在轨道矩形内就算点击了该滑块
        if (x <= py5.mouse_x <= x+w) and (y <= py5.mouse_y <= y+h):
            active_slider = i
            # 同时更新值，因为点击轨道任意位置也要更新
            update_slider(i)
            return

# 更新当前活动滑块的值（根据鼠标位置）
def update_slider(index):
    global r, g, b, a
    x, y, w, h = sliders[index]
    # 将鼠标x坐标限制在轨道的x到x+w之间，并映射到0-255
    new_value = py5.remap(py5.mouse_x, x, x+w, 0, 255)
    new_value = py5.constrain(new_value, 0, 255)

    # 更新对应变量
    if index == 0:
        r = int(new_value)
    elif index == 1:
        g = int(new_value)
    elif index == 2:
        b = int(new_value)
    elif index == 3:
        a = int(new_value)

def mouse_dragged():
    if active_slider is not None:
        update_slider(active_slider)

def mouse_released():
    global active_slider
    active_slider = None

# 运行程序
py5.run_sketch()