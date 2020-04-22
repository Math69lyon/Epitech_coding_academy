#!/usr/bin/env python3
from tkinter import *
import math
window = Tk()
window.title("CALCULATRICE")
window.geometry("525x400")
window.configure(background="#c1b7b0")
button_color=("lightblue")
largeur = 10
hauteur = 3

ops = {
    "*": (lambda a, b: a * b),
    "/": (lambda a, b: a / b),
    "-": (lambda a, b: a - b),
    "+": (lambda a, b: a + b),
    "^": (lambda a, b: a ** b)
    
}

funcs = {
    "sin": (lambda a: sin(a)),
    "log": (lambda a: log(a)),
    "tan": (lambda a: tan(a)),
    "log": (lambda a: log(a))
}

priorities = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3,
}
def eval(expression: str):
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token in ops:
            arg2 = int(stack.pop())
            arg1 = int(stack.pop())
            result = ops[token](arg1,arg2)
            stack.append[result]
        else:
            stack.append(token)
    return stack.pop()

def rpn(expression: str) -> str:
    tokens = expression.split()
    
    operators = []
    output = []
    
    for token in tokens:
        if token.isnumeric():
            output.append(token)
            continue
        
        if token in funcs:
            operators.append(token)
            continue
    
        if token in ops:
            while (len(operators) and
                   operators[-1] != "(" and
                   (operators[-1] in funcs or 
                   priorities[operators[-1]] > priorities[token])):
                output.append(operators.pop())
                   
            operators.append(token)
            continue
        
        if token == "(":
            operators.append(token)
            continue
        
        if token == ")":
            while (len(operators) > 0 and operators[-1] != "("):
                output.append(operators.pop())
                
        if len(operators) == 0:
            raise Exception('mismatching (')
        
        operators.pop()
        continue
        
        raise Exception('token not recognised: {}'.format(token))
    while len(operators):
        output.append(operators.pop())
    
    result = " "
    return result.join(output)


        
        
        
        
       
        
        
calc_input = ""
def input_key(value):
    global calc_input
    calc_input += value
    calc_input_text.set(calc_input)
    print(calc_input)
    
def clear():
    global calc_input
    calc_input=(" ")
    calc_input_text.set("0")
    print(calc_input)
    
def equal():
    global calc_input
    additions = calc_input.split("+")
    result = 0
    for value in additions:
        result += int(value)
    calc_input = ""
    calc_input_text.set(calc_input)
    result_text.set(result)
    print(result)



Button(window, text="Fermer", command=window.quit).grid(row=0, column=5)

Button(window, text="  0  ",bg=button_color,width=largeur,height=hauteur, command=lambda: input_key("0")).grid(row=7, column=1)
Button(window, text="   ,  ",bg=button_color,width=largeur,height=hauteur, command=lambda: input_key(",")).grid(row=7, column=2)
Button(window, text="  =  ",bg=button_color,width=largeur,height=hauteur, command=lambda: rpn()).grid(row=7, column=4)

#row6
Button(window, text="  1  ",bg=button_color,width=largeur,height=hauteur, command=lambda: input_key("1")).grid(row=6, column=1)
Button(window, text="  2  ",bg=button_color,width=largeur,height=hauteur, command=lambda: input_key("2")).grid(row=6, column=2)
Button(window, text="  3  ",bg=button_color,width=largeur,height=hauteur, command=lambda: input_key("3")).grid(row=6, column=3)
Button(window, text="  +  ",bg=button_color,width=largeur,height=hauteur, command=lambda: input_key("+")).grid(row=6, column=4)

#row5
Button(window, text="  4  ",bg=button_color,width=largeur,height=hauteur, command=lambda: input_key("4")).grid(row=5, column=1)
Button(window, text="  5  ",bg=button_color,width=largeur,height=hauteur, command=lambda: input_key("5")).grid(row=5, column=2)
Button(window, text="  6  ",bg=button_color,width=largeur,height=hauteur, command=lambda: input_key("6")).grid(row=5, column=3)
Button(window, text="   -  ",bg=button_color,width=largeur,height=hauteur, command=lambda: input_key("-")).grid(row=5, column=4)

#row4
Button(window, text="  7  ",bg=button_color,width=largeur,height=hauteur, command=lambda: input_key("7")).grid(row=4, column=1)
Button(window, text="  8  ",bg=button_color,width=largeur,height=hauteur, command=lambda: input_key("8")).grid(row=4, column=2)
Button(window, text="  9  ",bg=button_color,width=largeur,height=hauteur, command=lambda: input_key("9")).grid(row=4, column=3)
Button(window, text="  *  ",bg=button_color,width=largeur,height=hauteur, command=lambda: input_key("*")).grid(row=4, column=4)

#row3
Button(window, text=" AC ",bg=button_color,width=largeur,height=hauteur, command=lambda: clear()).grid(row=3, column=1)
Button(window, text=" +/-",bg=button_color,width=largeur,height=hauteur, command=lambda: input_key("p")).grid(row=3, column=2)
Button(window, text="  % ",bg=button_color,width=largeur,height=hauteur, command=lambda: input_key("%")).grid(row=3, column=3)
Button(window, text="   /  ",bg=button_color,width=largeur,height=hauteur, command=lambda: input_key("/")).grid(row=3, column=4)



calc_input_text = StringVar()
Label(window, textvariable=calc_input_text).grid(row=1, column=0)
result_text = StringVar()
Label(window, textvariable=result_text).grid(row=2, column=0)
window.mainloop()