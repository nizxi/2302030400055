# 3x3 Game Board with Grid Layout
import tkinter as tk

# Create window
root = tk.Tk()
root.title("3x3 Game Board")

# Create 3x3 grid of buttons
for row in range(3):
    for col in range(3):
        btn = tk.Button(root, text="", width=10, height=4)
        btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()