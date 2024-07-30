import tkinter as tk  # `pip3 install pytk`
import ttkbootstrap as ttk  # `pip3 install ttkbootstrap`

# Window
window = ttk.Window(
    title="Basics", themename="darkly"
)  # Using ttkbootstrap to use themes
window.title("Basics")  # Setting window title

# Title
title = ttk.Label(
    master=window,
    text="This is a title.",
    font=("Calibri 24 bold"),
)
title.pack()


def update_outputs():
    output1_var.set(str(window.winfo_width()))
    output2_var.set(str(window.winfo_height()))


# Input Frame
input_frame = ttk.Frame(master=window)
description = ttk.Label(
    master=input_frame, text="Click the button the below to update the dimensions"
)
button = ttk.Button(master=input_frame, text="Click me!", command=update_outputs)
description.pack(side="top")
button.pack(side="bottom")
input_frame.pack()

# Output Frame
output1_var = tk.StringVar(value="Unknown")
output2_var = tk.StringVar(value="Unknown")

output_frame = ttk.Labelframe(master=window, text="Width x Height")
output1 = ttk.Label(master=output_frame, textvariable=output1_var)
output2 = ttk.Label(master=output_frame, textvariable=output2_var)
output1.pack(side="left", padx=10, pady=10)
output2.pack(side="right", padx=10, pady=10)
output_frame.pack()

# Make the window
window.mainloop()
