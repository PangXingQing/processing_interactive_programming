# code/ch2/8_fill_stroke.py
import py5

def setup():
    py5.size(800, 600)
    my_font = py5.create_font("Noto Sans Thin", 16)
    py5.text_font(my_font)
    py5.text_align(py5.LEFT, py5.TOP)
    py5.rect_mode(py5.CENTER)  # 以中心点作为矩形基准点

def draw():
    py5.background(240)
    start_x, start_y = 140, 80       # 网格左上角第一个中心点位置
    grid_w, grid_h = 220, 220        # 每个展示区
    w, h = 100, 60                   # 矩形本身大小
    py5.no_stroke()

    # --------- 1. 默认黑描边 灰色填充 ----------------
    py5.push_style() # 保存当前样式
    py5.stroke(0) # 阅读py5文档了解stroke()函数
    py5.fill(180) # 阅读py5文档了解fill()函数
    py5.rect(start_x, start_y, w, h)
    py5.fill(0)
    py5.text("1. 默认 黑描边+灰填充\nstroke(0); fill(180)", start_x-w/2, start_y+h/2+16)
    py5.pop_style() # 恢复样式

    # --------- 2. 只有红色描边（无填充） ---------------
    py5.push_style()
    py5.stroke(255,0,0)
    py5.no_fill() # 阅读py5文档了解no_fill()函数
    py5.rect(start_x+grid_w, start_y, w, h)
    py5.fill(150,0,0)
    py5.text("2. 只有红描边\nstroke(255,0,0); no_fill()", 
             start_x+grid_w-w/2, start_y+h/2+16)
    py5.pop_style()

    # --------- 3. 只有绿色填充（无描边） ---------------
    py5.push_style()
    py5.no_stroke() # 阅读py5文档了解no_stroke()函数
    py5.fill(0, 200, 90)
    py5.rect(start_x+2*grid_w, start_y, w, h)
    py5.fill(0,100,30)
    py5.text("3. 只有绿填充\nno_stroke(); fill(0,200,90)",
             start_x+2*grid_w-w/2, start_y+h/2+16)
    py5.pop_style()

    # --------- 4. 半透明蓝色填充，黑描边 ----------------
    py5.push_style()
    py5.stroke(0)
    py5.fill(80, 120, 255, 120)  # 半透明
    py5.rect(start_x, start_y+grid_h, w, h)
    py5.fill(30,60,160)
    py5.text("4. 半透明蓝色\nfill(80,120,255,120)",
             start_x-w/2, start_y+grid_h+h/2+16)
    py5.pop_style()

    # --------- 5. 带透明度描边 ------------------------
    py5.push_style()
    py5.stroke(200,0,0, 100)    # 红色半透明
    py5.no_fill()
    py5.stroke_weight(8)
    py5.rect(start_x+grid_w, start_y+grid_h, w, h)
    py5.no_stroke()
    py5.fill(150,0,0)
    py5.text("5. 半透明红描边\nstroke(200,0,0,100)", 
             start_x+grid_w-w/2, start_y+grid_h+h/2+16)
    py5.pop_style()

    # --------- 6. 设置描边粗细 --------------------------
    py5.push_style()
    py5.stroke(80,60,200)
    py5.stroke_weight(12)
    py5.no_fill()
    py5.rect(start_x+2*grid_w, start_y+grid_h, w, h)
    py5.no_stroke()
    py5.fill(93,80,120)
    py5.text("6. 粗描边\nstroke_weight(12)", 
             start_x+2*grid_w-w/2, start_y+grid_h+h/2+16)
    py5.pop_style()

py5.run_sketch()