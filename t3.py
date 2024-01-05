"""

turtle 画虚线
"""
import turtle as t

# 设置画笔速度
t.speed(0)

# 画虚线
for step in range(100):
    t.fd(3)
    t.up() if t.isdown()  else t.down()

# 移动画笔，并画点
t.up()
t.goto(-200, 200)
t.down()
t.dot(10, 'red')
# 隐藏画笔
t.hideturtle()

t.mainloop()
