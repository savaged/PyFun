# might need to install python3-tk
import tkinter as tk


def onBtnCloseClicked():
    mw.destroy()


mw = tk.Tk()
mw.title("Greeter")
mw.geometry("200x150")

lblFeedback = tk.Label(mw, text="Hello World!")
btnClose = tk.Button(mw, text="Close", command=onBtnCloseClicked)

lblFeedback.grid(row=0, column=0, padx=10, pady=10)
btnClose.grid(row=1, column=0, padx=10, pady=10)

mw.mainloop()
