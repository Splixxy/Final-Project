import tkinter as tk
window = tk.Tk()
window.title("Quiz Machine")
window.rowconfigure(0, minsize=200, weight=1)
window.columnconfigure([0, 2], minsize=200, weight=1)
txt_edit = tk.Text(window)
frame = tk.Frame(master=window, width=150, height=150)
greeting = tk.Label(master=window, text="Press (YES) if you would like to start the quiz", bg="red")
greeting.grid(row = 0, column = 1)
yesButton = tk.Button(master=window,text = "YES", fg = "black")
yesButton.grid(row = 3, column = 0, sticky= "nsew", padx = 5, pady = 5,)
noButton = tk.Button(master=window,text = "NO", fg = "black")
noButton.grid(row = 3, column = 2, sticky = "nsew", padx = 5, pady = 5)
window.mainloop()
