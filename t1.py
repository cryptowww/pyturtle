import turtle as t

# draw a square
def draw_square():
    for i in range(4):
        t.forward(100)
        t.right(90)

# draw a spider web
def draw_spider_web():
    for step in range(100):
        for c in ['red', 'green', 'blue', 'yellow']:
            t.color(c)
            t.forward(step)
            t.left(30)
            #print("step: %d,color: %s" %(step, c))
            #print("step: {},color: {}".format(step, c))
            #print("step: {0},color: {1}".format(step, c))
            #print("step: {step},color: {color}".format(step=step, color=c))
            #print(f"step: {step}, color: {c}")
        #print(step)


if __name__ == '__main__':
    #draw_square()
    draw_spider_web()
    t.mainloop()

