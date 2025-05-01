# Q17: Drawing Shapes on a Canvas
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Canvas Drawing")

# Create canvas
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# Draw a rectangle
canvas.create_rectangle(50, 50, 150, 100, fill="blue")

# Draw a circle (oval)
canvas.create_oval(170, 50, 270, 150, fill="red")

# Draw a line
canvas.create_line(0, 200, 300, 200, fill="green", width=2)

root.mainloop()