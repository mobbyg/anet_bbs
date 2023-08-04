import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont

def open_new_window(title):
    new_window = tk.Toplevel(root)
    new_window.title(title)
    new_window.geometry("300x600")

def create_top_row_command(label):
    def top_row_command():
        open_new_window(label)
    return top_row_command

def create_node_command(index):
    def node_command():
        open_new_window(f"Node {index}")
    return node_command

def quit_app():
    confirm = messagebox.askyesno("Confirm Quit", "Are you sure you want to quit?")
    if confirm:
        root.destroy()

root = tk.Tk()
root.title("ANet Control Panel")

# Set the width and height of the root window
root.geometry("1000x600")

# Set the background color of the root window to light gray
root.configure(bg="light gray")

# Load the CuppaJoe font for the "node" buttons
node_font = tkfont.Font(family="CuppaJoe", size=16)

# Create top row buttons
buttons = [
    ("SysInfo", 100),
    ("User Info", 100),
    ("Config", 100),
    ("Mail", 100),
    ("Files", 100),
    ("Yanks", 100),
    ("News", 100),
    ("Edit", 100),
    ("Quit", 100),
]

top_row_commands = [
    create_top_row_command(label) for label, _ in buttons
]

# Create and place top row buttons on the root window
for i, (label, width) in enumerate(buttons):
    btn = tk.Button(root, text=label, command=top_row_commands[i], width=width)
    btn.grid(row=0, column=i, padx=5, pady=5)

# Create a scrollable frame for the node buttons
canvas = tk.Canvas(root)
frame = tk.Frame(canvas)
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

# Place the scrollable frame on the canvas
canvas.grid(row=1, column=0, columnspan=len(buttons), sticky="nsew")
vsb.grid(row=1, column=len(buttons), sticky="ns")
canvas.create_window((4, 4), window=frame, anchor="nw")

# Create "node" buttons and place them on the scrollable frame
for i in range(11):  # Create 11 "node" buttons
    btn = tk.Button(frame, text=str(i), command=create_node_command(i), width=1000, height=3, anchor='w', justify='left', font=node_font)
    btn.grid(row=i, column=0, padx=5, pady=5, sticky="w")

# Update the canvas scrolling region
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Configure columns and rows to expand when the window is resized
for i in range(len(buttons)):
    root.columnconfigure(i, weight=1)

root.rowconfigure(1, weight=1)

root.mainloop()

