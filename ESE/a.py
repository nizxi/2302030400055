import tkinter as tk
root = tk.Tk()
label1 = tk.Label(root, text="Label One", bg="red")
label2 = tk.Label(root, text="Label Two", bg="green")
label1.pack(side="top", fill="x")
label2.pack(side="bottom", fill="x")
root.mainloop()

import tkinter as tk
root = tk.Tk()
btn = tk.Button(root, text="Click Me")
btn.place(x=100, y=50)
root.mainloop()


text = "Silver Oak University"

for char in text:
    if char.lower() != 'e' and char.lower() != 's':
        print(char, end='')