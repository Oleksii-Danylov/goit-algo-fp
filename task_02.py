#!/usr/bin/python3
'''
Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.
'''
import turtle
import math

def draw_tree(t, branch_length, level):
    if level == 0:
        return
    
    t.forward(branch_length)
    t.left(45)
    draw_tree(t, branch_length * math.sqrt(2) / 2, level - 1)
    t.right(90)
    draw_tree(t, branch_length * math.sqrt(2) / 2, level - 1)
    t.left(45)
    t.backward(branch_length)

def tree(level, size=150):
    window = turtle.Screen()
    window.bgcolor("White")
    
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -size // 2)
    t.pendown()
    
    draw_tree(t, size, level)
    
    t.hideturtle()
    window.exitonclick()

level = int(input("Введіть рівень рекурсії: "))
tree(level)