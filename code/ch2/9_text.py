# code/ch2/9_text.py
import py5

def setup():
    py5.size(800, 520)
    py5.background(245)
    # 如果将这里注释掉，就会显示乱码
    # 因为py5默认字体不支持中文
    my_font = py5.create_font("Noto Sans Thin", 16)
    py5.text_font(my_font)
    py5.text_align(py5.LEFT, py5.TOP)

def draw():
    py5.background(245)
    
    # 绘制一行居中大字
    py5.text_size(42)
    py5.fill(16, 70, 170)
    py5.text_align(py5.CENTER, py5.TOP)
    py5.text("Hello, 世界! Py5字体演示", py5.width/2, 70)

    # 不同字号 + 颜色 对比
    py5.text_size(32)
    py5.fill(230, 60, 50)
    py5.text_align(py5.LEFT, py5.TOP)
    py5.text("小一号红色字体（左上角对齐）", 60, 160)

    py5.text_size(24)
    py5.fill(80, 190, 80)
    py5.text_align(py5.LEFT, py5.TOP)
    py5.text("更小号绿色，试试混合中文和English!", 60, 210)

    # 半透明&右对齐文字
    py5.text_size(30)
    py5.fill(120, 50, 200, 120)
    py5.text_align(py5.RIGHT, py5.TOP)
    py5.text("右对齐 / 半透明紫", py5.width - 60, 280)

    # 绘制示意区域分割线
    py5.stroke(150, 150, 150, 80)
    py5.stroke_weight(1)
    for y in [58, 150]:
        py5.line(30, y, py5.width-30, y)
    py5.no_stroke()

py5.run_sketch()