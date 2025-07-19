# code/ch2/7_bezier.py
import py5

# -- 定义每阶贝塞尔曲线的控制点与区域属性 --
regions = [
    {   # 1阶：两点一线（直线）
        'points': [(60, 320), (320, 60)],
        'color': '#FF3333',
        'order': 1,
        't': 0,
    },
    {   # 2阶：三点二次曲线
        'points': [(60, 320), (190, 80), (320, 320)],
        'color': '#33CC66',
        'order': 2,
        't': 0,
    },
    {   # 3阶：四点三次曲线
        'points': [(60, 320), (120, 60), (260, 80), (320, 320)],
        'color': '#3366FF',
        'order': 3,
        't': 0,
    },
    {   # 4阶：五点四次曲线
        'points': [(60, 320), (100, 60), (160, 340), (260, 80), (160, 60)],
        'color': '#FF33CC',
        'order': 4,
        't': 0,
    },
]

region_size = 380  # 每块区域的大小
margin = 10        # 区域与画布或相邻块之间的边距

# -- 德卡斯特里奥算法，递归计算贝塞尔曲线某t点的坐标 --
def de_casteljau(t, pts):
    # pts: 控制点列表，每个元素是(x, y)
    if len(pts) == 1:
        return pts[0]
    new_pts = []
    for i in range(len(pts)-1):
        x = (1-t)*pts[i][0] + t*pts[i+1][0]
        y = (1-t)*pts[i][1] + t*pts[i+1][1]
        new_pts.append((x, y))
    return de_casteljau(t, new_pts)

def setup():
    py5.size(region_size*2 + margin*3, region_size*2 + margin*3)
    py5.background(250)
    my_font = py5.create_font("Noto Sans Thin", 16)
    py5.text_font(my_font)
    py5.text_align(py5.LEFT, py5.TOP)

def draw():
    py5.background(250)
    steps = 120  # 曲线采样点数，越大越平滑

    for i, region in enumerate(regions):
        # -- 计算该区域左上角坐标 --
        rx = margin + (i % 2) * (region_size + margin)
        ry = margin + (i // 2) * (region_size + margin)
        # -- 到区域内部绘图 --
        py5.push_matrix()
        py5.translate(rx, ry)
        
        # 区域背景&边框
        py5.no_stroke()
        py5.fill(245)
        py5.rect(0, 0, region_size, region_size, 20)
        py5.stroke(200)
        py5.no_fill()
        py5.rect(0, 0, region_size, region_size, 20)

        # -- 画虚线控制多边形 --
        pts = region['points']
        py5.stroke(120, 120, 120, 150)
        py5.stroke_weight(1)
        for j in range(len(pts)-1):
            px1, py1 = pts[j]
            px2, py2 = pts[j+1]
            py5.line(px1, py1, px2, py2)

        # -- 画控制点 --
        py5.fill(0)
        py5.stroke(40)
        for j, (px, py_) in enumerate(pts):
            py5.ellipse(px, py_, 12, 12)
            # 控制点编号
            py5.fill(70)
            py5.text_size(14)
            py5.text(f"P{j}", px + 8, py_ - 20)
            py5.fill(0)

        # -- 动态画贝塞尔曲线的“已经写出”部分 --
        py5.stroke(region['color'])
        py5.stroke_weight(3)
        py5.no_fill()
        py5.begin_shape()
        t_now = region['t']
        for s in range(steps+1):
            t_val = s * t_now / steps
            x, y = de_casteljau(t_val, pts)
            py5.vertex(x, y)
        py5.end_shape()

        # -- 动态t点的拖尾小球 --
        if t_now > 0:
            bx, by = de_casteljau(t_now, pts)
            py5.no_stroke()
            py5.fill(region['color'])
            py5.ellipse(bx, by, 16, 16)

        # -- 区域标题（阶数）/解释说明 --
        py5.fill(60)
        py5.text(f'{region["order"]}阶贝塞尔', 20, 15)
        py5.text(f'控制点数：{region["order"]+1}', 20, region_size - 34)

        py5.pop_matrix()

        # -- t动画: 匀速递增，画完再重置 --
        region['t'] += 0.009
        if region['t'] > 1:
            region['t'] = 0

def key_pressed():
    # 按下任意键重置动画
    for region in regions:
        region['t'] = 0

py5.run_sketch()