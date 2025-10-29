import turtle as t
import random, time

zones = {"red":(-200, -200), "green":(200, -200), "blue":(-200, 200), "yellow":(200, 200)}
pen = t.Turtle(visible=False)
pen.color("white")
    
def init():
    t.setup(600,600)
    t.bgcolor("black")
    t.tracer(0)
    
    draw_zones()
    
def animate(num, color):
    flash_number(num)
    ball = draw_ball(color)
    if color != "roska":
        move_to_zone(ball, color)
    
def flash_number(num, duration=2):
    pen.clear()
    pen.up(); pen.goto(0,0)
    pen.write(str(num), align="center", font=("Arial", 48, "bold"))
    t.update()
    time.sleep(duration)
    t.update()

def draw_ball(color):
    if color == "roska":
        print("Roska, ei piirretä mitään")
        return
    
    ball = t.Turtle("circle")
    ball.up(); ball.speed(0)
    ball.shapesize(1.5)    
    ball.color(color)
    ball.goto(0,250)
    t.update()
    time.sleep(0.3)
    return ball

def move_to_zone(ball, color):
    tx, ty = zones[color]
    for _ in range(40):
        x = ball.xcor() + (tx - ball.xcor())/10
        y = ball.ycor() + (ty - ball.ycor())/10
        ball.goto(x, y)
        t.update()
        time.sleep(0.02)

def draw_zones():
    

    pen = t.Turtle()
    pen.hideturtle()
    pen.color("white")
    for c,(x,y) in zones.items():
        pen.up(); pen.goto(x-60, y-60)
        pen.down(); pen.color(c)
        for _ in range(4):
            pen.forward(120); pen.left(90)
        pen.up(); pen.goto(x, y+70)
        pen.color("white"); pen.write(c, align="center", font=("Arial",12,"bold"))
