# code/ch2/6_shapes.py
import py5

def setup():
    py5.size(800, 400)
    my_font = py5.create_font("Noto Sans Thin", 16)
    py5.text_font(my_font)
    py5.text_align(py5.LEFT, py5.TOP)
    
    py5.background(240)
    
    # 把画布分成两排，每排4格，图形居中分布
    cell_w = py5.width // 4
    cell_h = py5.height // 2

    # 1. 画点
    # 使用stroke_wright()设置点的大小
    # 使用point()函数绘制点
    py5.stroke(0)
    py5.stroke_weight(8)  # 点粗一点方便看
    px, py_ = cell_w//2, cell_h//2
    py5.point(px, py_)
    py5.stroke_weight(1)  # 恢复线宽
    py5.fill(0)
    py5.text("点 point()", px-20, py_ + 40)

    # 2. 画直线
    # 使用stroke()设置线条颜色
    # 使用stroke_weight()设置线条宽度
    # line参数说明
    # x1, y1, x2, y2 分别是线条的起点和终点坐标
    # 这里的线条是从左上角到右下角
    # 也可以使用lines()函数绘制多条线
    py5.stroke(255, 0, 0)
    lx = cell_w + cell_w//2
    ly1 = cell_h//2 - 20
    ly2 = cell_h//2 + 20
    py5.line(lx, ly1, lx, ly2)
    py5.fill(255, 0, 0)
    py5.text("直线 line()", lx-30, ly2 + 30)

    # 3. 画三角形
    # 自己阅读py5的文档，了解triangle()函数的用法
    py5.stroke(0, 128, 0)
    tx = cell_w*2 + cell_w//2
    ty = cell_h//2
    py5.fill(0, 180, 0, 100)  # 半透明绿
    py5.triangle(tx, ty-30, tx-30, ty+30, tx+30, ty+30)
    py5.fill(0)
    py5.text("三角形 triangle()", tx-50, ty + 60)

    # 4. 画矩形
    # 自己阅读py5的文档，了解rect()函数的用法
    # 此外，py5还提供了rect_mode()函数来设置矩形的绘制模式
    # 自行阅读py5的文档，了解rect_mode()函数的用法
    py5.stroke(0,0,255)
    rx = cell_w*3 + cell_w//2
    ry = cell_h//2
    py5.fill(0, 0, 255, 80)  # 半透明蓝
    py5.rect_mode(py5.CENTER)
    py5.rect(rx, ry, 60, 40)
    py5.rect_mode(py5.CORNER)  # 恢复默认
    py5.fill(0)
    py5.text("矩形 rect()", rx-40, ry + 40)

    # 5. 画正方形
    # 正方形也是矩形，只要宽高相等即可
    # 使用rect()函数绘制正方形
    py5.stroke(150, 0, 150)
    sx = cell_w//2
    sy = cell_h + cell_h//2
    py5.fill(180, 0, 180, 90)  # 半透明紫
    py5.rect_mode(py5.CENTER)
    py5.rect(sx, sy, 50, 50)  # 正方形，只要宽高相等
    py5.rect_mode(py5.CORNER)
    py5.fill(0)
    py5.text("正方形 rect() ", sx-35, sy+40)

    # 6. 画椭圆
    py5.stroke(0, 170, 170)
    ex = cell_w + cell_w//2
    ey = cell_h + cell_h//2
    py5.fill(0, 200, 200, 100)
    py5.ellipse(ex, ey, 70, 40)
    py5.fill(0)
    py5.text("椭圆 ellipse()", ex-40, ey+40)

    # 7. 画圆形
    # py5也提供了circle()函数来绘制圆形
    # 但这里我们使用ellipse()函数绘制圆形
    # 因为ellipse()函数可以绘制椭圆和圆形
    # 只要宽高相等即可绘制圆形
    # 注意：py5.circle()函数是Processing 4.0版本新增的
    # 在py5中，circle()函数是别名，实际上还是调用的ellipse
    py5.stroke(255, 200, 0)
    cx = cell_w*2 + cell_w//2
    cy = cell_h + cell_h//2
    py5.fill(255, 225, 60, 90)
    py5.ellipse(cx, cy, 50, 50)  # 宽高一样就是圆
    py5.fill(0)
    py5.text("圆 ellipse()", cx-30, cy+40)

    # 8. 画弧线 (半圆)
    py5.stroke(255,128,0)
    ax = cell_w*3 + cell_w//2
    ay = cell_h + cell_h//2
    py5.no_fill()
    py5.arc(ax, ay, 60, 60, 0, py5.PI)  # 0到PI画半圆弧，默认OPEN模式
    py5.fill(0)
    py5.text("弧线 arc()", ax-32, ay+45)
    
def draw():
    pass

py5.run_sketch()