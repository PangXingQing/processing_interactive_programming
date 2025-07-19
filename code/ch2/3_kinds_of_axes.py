# code/ch2/3_kinds_of_axes.py
import py5
import math

def setup():
    py5.size(800, 600)
    my_font = py5.create_font("Noto Sans Thin", 12)
    py5.text_font(my_font)
    py5.text_align(py5.LEFT, py5.TOP)
    py5.rect_mode(py5.CORNER)
    py5.no_stroke()

def draw():
    py5.background(250)
    # ====== 屏幕坐标网格 ======
    py5.stroke(225)
    for x in range(0, py5.width, 50):
        py5.line(x, 0, x, py5.height)
    for y in range(0, py5.height, 50):
        py5.line(0, y, py5.width, y)
    py5.no_stroke()

    # ===== 屏幕坐标举例点 =====
    py5.fill(60, 130, 210)
    py5.rect(100, 100, 60, 40)
    py5.fill(255)
    py5.text("屏幕坐标: (100,100)", 102, 102)

    # ===== 鼠标屏幕坐标 =====
    py5.fill(0)
    py5.text(f"鼠标屏幕 (mouse): ({py5.mouse_x}, {py5.mouse_y})", 10, 10)
    py5.fill(220, 100, 100)
    py5.ellipse(py5.mouse_x, py5.mouse_y, 12, 12)

    # ====== 相对坐标/归一化坐标 ======
    norm_x = py5.mouse_x / float(py5.width)
    norm_y = py5.mouse_y / float(py5.height)
    py5.fill(0)
    py5.text(f"归一化(0-1): (%.2f, %.2f)" % (norm_x, norm_y), 10, 36)
    py5.fill(60, 220, 100)
    py5.ellipse(norm_x * py5.width, norm_y * py5.height, 10, 10)
    py5.text("中心为(0.5,0.5)", py5.width * 0.5 + 8, py5.height * 0.5 + 8)
    py5.stroke(60, 220, 100, 128)
    py5.line(py5.width * 0.5, 0, py5.width * 0.5, py5.height)
    py5.line(0, py5.height * 0.5, py5.width, py5.height * 0.5)
    py5.no_stroke()

    # ===== 世界坐标变换区 =====
    world_pos = (550, 300)
    world_angle_deg = 30
    world_angle_rad = math.radians(world_angle_deg)
    world_grid_span = 200
    world_grid_step = 40

    with py5.push_matrix():
        # 设置世界坐标原点与旋转
        py5.translate(world_pos[0], world_pos[1])
        py5.rotate(world_angle_rad)

        # ==== 绘制“世界坐标”网格 ====
        py5.stroke(180, 200, 255)
        for x in range(-world_grid_span, world_grid_span + 1, world_grid_step):
            py5.line(x, -world_grid_span, x, world_grid_span)
        for y in range(-world_grid_span, world_grid_span + 1, world_grid_step):
            py5.line(-world_grid_span, y, world_grid_span, y)
        # 世界坐标原点与主轴
        py5.stroke(60, 130, 210)
        py5.stroke_weight(2)
        py5.line(0, 0, 60, 0)
        py5.line(0, 0, 0, 60)
        py5.no_stroke()
        py5.fill(60, 130, 210)
        py5.ellipse(0, 0, 14, 14)
        py5.fill(30)
        py5.text("世界原点 (0,0)", 10, -24)
        py5.text("X", 62, -12)
        py5.text("Y", -14, 62)

        # ==== 在世界坐标固定位置画个对象 ====
        py5.fill(180, 90, 255, 180)
        py5.rect_mode(py5.CENTER)
        py5.rect(80, 50, 40, 40)
        py5.fill(30)
        py5.text("世界坐标 (80,50)", 80 + 12, 50 - 8)
        py5.rect_mode(py5.CORNER)

    # ==== 鼠标在世界坐标区的映射 ====
    # 逆变换：mouse坐标 → 世界坐标（逆旋转+逆平移）
    dx = py5.mouse_x - world_pos[0]
    dy = py5.mouse_y - world_pos[1]
    c = math.cos(-world_angle_rad)
    s = math.sin(-world_angle_rad)
    world_mouse_x = dx * c - dy * s
    world_mouse_y = dx * s + dy * c
    with py5.push_matrix():
        py5.translate(world_pos[0], world_pos[1])
        py5.rotate(world_angle_rad)
        # 显示鼠标在世界的点（红色）
        py5.fill(220, 60, 80)
        py5.ellipse(world_mouse_x, world_mouse_y, 16, 16)
        py5.fill(0)
        py5.text(
            f"鼠标的世界坐标: (%.1f, %.1f)" % (world_mouse_x, world_mouse_y),
            world_mouse_x + 18, world_mouse_y - 8
        )
    # ====== 信息区 ======
    py5.fill(80)
    py5.text(
        "⬅️ 屏幕、鼠标、点阵\n"
        "➡️ 世界坐标系及变换\n"
        "下方为归一化/相对坐标\n"
        "\n拖动鼠标观察变化",
        22, py5.height - 110
    )

py5.run_sketch()
