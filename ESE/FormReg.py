# Q15: User Registration Form with Vertical Layout

import tkinter as tk

# Create main window
root = tk.Tk()
root.title("User Registration")
root.geometry("300x250")

# Create a vertical layout using pack()
tk.Label(root, text="Full Name:").pack(pady=5)
tk.Entry(root).pack()

tk.Label(root, text="Email:").pack(pady=5)
tk.Entry(root).pack()

tk.Label(root, text="Username:").pack(pady=5)
tk.Entry(root).pack()

tk.Label(root, text="Password:").pack(pady=5)
tk.Entry(root, show="*").pack()

tk.Button(root, text="Register").pack(pady=10)

root.mainloop()