import turtle as tt


class Huaji(object):
    def __init__(self, radius):
        self.radius = radius  # 初始化半径，控制图像大小

    def my_goto(self, x, y):
        tt.penup()
        tt.goto(x, y)
        tt.pendown()

    def face(self):
        """
        Draw the face
        A  circle
        color: yellow
        """
        tt.pencolor('#EE9A00')  # 浅棕色
        tt.fillcolor('#EEEE00')  # 填充黄色
        tt.begin_fill()
        tt.circle(self.radius)  # 理解成圆的大小即可
        tt.end_fill()

    def mouth(self):
        """
        Draw the mouth
        A half circle
        color: brown
        """
        tt.pencolor('#EE9A00')
        tt.right(90)
        tt.circle(self.radius - 50, 180)  # 理解成圆的大小即可

    def eyebrow(self, kind):
        """
        Draw the eyebrow
        A half circle
        color: black
        """
        tt.pencolor('black')
        if kind == 'left':
            self.my_goto(-60, 70)
            tt.left(45)  # 左转75°
            tt.circle(self.radius - 100, 60)
        elif kind == 'right':
            self.my_goto(100, 90)  # 高度有待商榷
            tt.left(-30)  # 左转75°
            tt.circle(self.radius - 100, 60)

    def eyes(self):
        """
        Draw the eyes
        Hyperbolic curve
        """
        # 左眼
        self.my_goto(-40, 30)
        tt.left(-90)
        tt.circle(self.radius - 90, 100)  # 100°的圆弧
        tt.right(-30)
        tt.circle(self.radius - 120, 40)

        tt.left(100)
        tt.circle(-(self.radius - 90), 100)
        tt.right(-128)
        tt.circle(self.radius - 105, 50)

        self.my_goto(-100, 30)
        tt.fillcolor('black')
        tt.begin_fill()
        tt.circle(self.radius - 140)
        tt.end_fill()

        # 右眼
        self.my_goto(120, 30)  # 起始位置是关键
        # tt.left(-90)
        tt.circle(self.radius - 90, 100)  # 100°的圆弧
        tt.right(-30)
        tt.circle(self.radius - 120, 40)

        tt.left(100)
        tt.circle(-(self.radius - 90), 100)
        tt.right(-128)
        tt.circle(self.radius - 105, 50)

        self.my_goto(60, 40)
        tt.fillcolor('black')
        tt.begin_fill()
        tt.circle(self.radius - 140)
        tt.end_fill()


if __name__ == '__main__':
    tt.screensize(800, 600, "#f0f0f0")  # 画布设置
    tt.pensize(2)  # 画笔宽度
    tt.speed(9)    # 画笔速度
    huaji = Huaji(radius=150)   # 图像大小设置
    huaji.my_goto(0, -200)
    huaji.face()   # 脸
    huaji.my_goto(-100, -80)
    huaji.mouth()  # 嘴巴
    huaji.eyebrow('left')  # 左眉毛
    huaji.eyebrow('right')  # 右眉毛
    huaji.eyes()

    tt.exitonclick()
