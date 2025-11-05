# Without exit button

import tkinter

root = tkinter.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost',True)
root.protocol("WM_DELETE_WINDOW", lambda:None)
root.mainloop()

# With Exit button center of the window
import tkinter

root = tkinter.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.protocol("WM_DELETE_WINDOW", lambda: None)

def exit_app():
    root.destroy()
frame = tkinter.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor='center')

exit_button = tkinter.Button(
    frame,
    text="Exit",
    font=("Arial", 28, "bold"),
    bg="red",
    fg="white",
    padx=40, pady=20,
    command=exit_app
)
exit_button.pack()

root.mainloop()
