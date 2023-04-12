import tkinter as tk
import pyfiglet

root = tk.Tk()

root.geometry("500x500")
word=pyfiglet.figlet_format("TODO - LIST")
root.title("Todo-List") 
root.configure(bg="Black")

label = tk.Label(root, text=word)
label.pack(pady=20)

buttonframe =tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

root.mainloop()

#WE import the module 
#we create a root window
#we add some widgets
#We choose a layout ,a grid or pack or we use the place funstion to create GUI