import tkinter as tk
import math

root = tk.Tk()
root.title("CalcX")
root.geometry("400x600")

entry = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.FLAT, justify="right")
entry.pack(padx=10, pady=20, fill="both")

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    content = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, content[:-1])

def percent():
    try:
        val = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, val / 100)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def evaluate():
    try:
        expression = entry.get().replace("of", "*").replace("%", "/100")
        # Handle redundant signs
        expression = expression.replace('--', '+').replace('++', '+').replace('+-', '-').replace('-+', '-')
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square():
    try:
        val = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, val ** 2)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def sqrt():
    try:
        val = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, math.sqrt(val))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def cube():
    try:
        val = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, val ** 3)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def cbrt():
    try:
        val = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, round(val ** (1/3), 6))  
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

buttons = [
    ('C', clear), ('←', backspace),
    ('7', lambda: click('7')), ('8', lambda: click('8')), ('9', lambda: click('9')), ('*', lambda: click('*')),
    ('4', lambda: click('4')), ('5', lambda: click('5')), ('6', lambda: click('6')), ('-', lambda: click('-')),
    ('1', lambda: click('1')), ('2', lambda: click('2')), ('3', lambda: click('3')), ('+', lambda: click('+')),
    ('0', lambda: click('0')), ('.', lambda: click('.')), ('%', percent),('/', lambda: click('/')), 
    ('x²', square), ('√x', sqrt), ('x³', cube), ('∛x', cbrt), ('(', lambda: click('(')), (')', lambda: click(')')), ('of', lambda: click('of')),('=', evaluate),
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0
for text, command in buttons:
   
    if text == 'C':
        bg = '#ff4d4d'; fg = 'white'; w = 18; colspan = 2
    elif text == '←':
        bg = '#ffa500'; fg = 'white'; w = 18; colspan = 2
    elif text == '=':
        bg = '#4CAF50'; fg = 'white'; w = 9; colspan = 1
    else:
        bg = None; fg = None; w = 8; colspan = 1

    b = tk.Button(frame, text=text, font=("Arial", 16), width=w, height=2, command=command,
                  bg=bg if bg else None, fg=fg if fg else None)
    b.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky="nsew")
    col += colspan
    if col > 3:
        col = 0
        row += 1

root.mainloop()
