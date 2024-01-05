"""

turtle 画虚线
"""
import turtle as t

for step in range(100):
    t.fd(5)
    t.up() if t.isdown()  else t.down()

t.mainloop()
