import tkinter as tk

# Function to add text to the display
def button_click(item):
    """This function is called when a number or operator button is clicked."""
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Function to clear the display
def button_clear():
    """This function clears the input field."""
    global expression
    expression = ""
    input_text.set("")

# Function to calculate the expression
def button_equal():
    """This function evaluates the expression in the input field."""
    global expression
    try:
        # The eval() function evaluates the passed string as a Python expression.
        result = str(eval(expression))
        input_text.set(result)
        # To allow for further calculations with the result
        expression = result
    except:
        # If there is an error in the expression
        input_text.set("Error")
        expression = ""

# Main window configuration
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")
window.resizable(0, 0) # Make the window not resizable

# Global variable to store the expression
expression = ""

# StringVar to hold the text for the display
input_text = tk.StringVar()

# --- GUI Layout ---

# Frame for the display
display_frame = tk.Frame(window, bd=0, relief=tk.SUNKEN)
display_frame.pack(side=tk.TOP)

# Display (Entry widget)
display = tk.Entry(display_frame, font=('arial', 18, 'bold'), textvariable=input_text,
                   width=50, bg="#eee", bd=0, justify=tk.RIGHT)
display.grid(row=0, column=0)
display.pack(ipady=10) # Internal padding

# Frame for the buttons
button_frame = tk.Frame(window, bg="grey")
button_frame.pack()

# --- Button Rows ---

# First row (7, 8, 9, /)
tk.Button(button_frame, text="7", fg="black", width=7, height=2, bd=0,
          command=lambda: button_click(7)).grid(row=1, column=0, padx=1, pady=1)
tk.Button(button_frame, text="8", fg="black", width=7, height=2, bd=0,
          command=lambda: button_click(8)).grid(row=1, column=1, padx=1, pady=1)
tk.Button(button_frame, text="9", fg="black", width=7, height=2, bd=0,
          command=lambda: button_click(9)).grid(row=1, column=2, padx=1, pady=1)
tk.Button(button_frame, text="/", fg="black", width=7, height=2, bd=0,
          command=lambda: button_click("/")).grid(row=1, column=3, padx=1, pady=1)

# Second row (4, 5, 6, *)
tk.Button(button_frame, text="4", fg="black", width=7, height=2, bd=0,
          command=lambda: button_click(4)).grid(row=2, column=0, padx=1, pady=1)
tk.Button(button_frame, text="5", fg="black", width=7, height=2, bd=0,
          command=lambda: button_click(5)).grid(row=2, column=1, padx=1, pady=1)
tk.Button(button_frame, text="6", fg="black", width=7, height=2, bd=0,
          command=lambda: button_click(6)).grid(row=2, column=2, padx=1, pady=1)
tk.Button(button_frame, text="*", fg="black", width=7, height=2, bd=0,
          command=lambda: button_click("*")).grid(row=2, column=3, padx=1, pady=1)

# Third row (1, 2, 3, -)
tk.Button(button_frame, text="1", fg="black", width=7, height=2, bd=0,
          command=lambda: button_click(1)).grid(row=3, column=0, padx=1, pady=1)
tk.Button(button_frame, text="2", fg="black", width=7, height=2, bd=0,
          command=lambda: button_click(2)).grid(row=3, column=1, padx=1, pady=1)
tk.Button(button_frame, text="3", fg="black", width=7, height=2, bd=0,
          command=lambda: button_click(3)).grid(row=3, column=2, padx=1, pady=1)
tk.Button(button_frame, text="-", fg="black", width=7, height=2, bd=0,
          command=lambda: button_click("-")).grid(row=3, column=3, padx=1, pady=1)

# Fourth row (0, ., C, +)
tk.Button(button_frame, text="0", fg="black", width=7, height=2, bd=0,
          command=lambda: button_click(0)).grid(row=4, column=0, padx=1, pady=1)
tk.Button(button_frame, text=".", fg="black", width=7, height=2, bd=0,
          command=lambda: button_click('.')).grid(row=4, column=1, padx=1, pady=1)
tk.Button(button_frame, text="C", fg="black", width=7, height=2, bd=0,
          command=button_clear).grid(row=4, column=2, padx=1, pady=1)
tk.Button(button_frame, text="+", fg="black", width=7, height=2, bd=0,
          command=lambda: button_click("+")).grid(row=4, column=3, padx=1, pady=1)

# Fifth row (=)
tk.Button(button_frame, text="=", fg="black", width=29, height=2, bd=0,
          command=button_equal).grid(row=5, column=0, columnspan=4, padx=1, pady=1)

# Start the GUI event loop
window.mainloop()