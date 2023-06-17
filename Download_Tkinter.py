import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import calendar

# Calculator functionality
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = entry_operator.get()

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            result = 'Invalid operator'

        label_result.config(text='Result: {}'.format(result))
    except ValueError:
        messagebox.showerror('Error', 'Invalid input')

# Quiz functionality
def quiz():
    answer = messagebox.askquestion('Quiz', 'Is Python an interpreted language?')
    if answer == 'yes':
        messagebox.showinfo('Quiz', 'Correct!')
    else:
        messagebox.showinfo('Quiz', 'Incorrect!')

# Calendar functionality
def show_calendar():
    year = simpledialog.askinteger('Calendar', 'Enter a year:')
    if year:
        window = tk.Toplevel(root)
        window.title('Calendar')
        cal = calendar.calendar(year)
        label_calendar = tk.Label(window, text=cal, font='Arial 10')
        label_calendar.pack(padx=10, pady=10)
    else:
        messagebox.showwarning('Calendar', 'Invalid year!')

# Create the main window
root = tk.Tk()
root.title('MyApp - Calculator, Quiz, and Calendar')

# Create the notebook for tabbed interface
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10)

# Functions to create GUI elements
def create_calculator_tab():
    tab_calculator = ttk.Frame(notebook)
    notebook.add(tab_calculator, text='Calculator')

    elements = [
        ('First number:', None),
        ('Operator:', None),
        ('Second number:', None)
    ]

    for i, (label_text, entry) in enumerate(elements):
        label = tk.Label(tab_calculator, text=label_text)
        label.pack()
        entry = tk.Entry(tab_calculator)
        entry.pack()
        elements[i] = (label, entry)

    button_calculate = tk.Button(tab_calculator, text='Calculate', command=calculate)
    button_calculate.pack()

    global label_result
    label_result = tk.Label(tab_calculator)
    label_result.pack()

    global entry_num1, entry_operator, entry_num2
    entry_num1 = elements[0][1]
    entry_operator = elements[1][1]
    entry_num2 = elements[2][1]

    return tab_calculator

def create_quiz_tab():
    tab_quiz = ttk.Frame(notebook)
    notebook.add(tab_quiz, text='Quiz')

    button_quiz = tk.Button(tab_quiz, text='Take Quiz', command=quiz)
    button_quiz.pack()

    return tab_quiz

def create_calendar_tab():
    tab_calendar = ttk.Frame(notebook)
    notebook.add(tab_calendar, text='Calendar')

    button_show_calendar = tk.Button(tab_calendar, text='Show Calendar', command=show_calendar)
    button_show_calendar.pack()

    return tab_calendar

# Create the tabs
calculator_tab = create_calculator_tab()
quiz_tab = create_quiz_tab()
calendar_tab = create_calendar_tab()

# Start the main event loop
root.mainloop()
