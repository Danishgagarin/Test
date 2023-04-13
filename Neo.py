from tkinter import *
from tkinter.font import Font
from cs50 import SQL
import random

#This basically define the container. Above this we include other gui stuff
root = Tk()
db = SQL("sqlite:///data.db")
#Parameters for the container
root.geometry("800x500")
root.title("Neo") 
root.configure(bg="Black")

# Create the canvas , so we can include functionality above this
canvas = Canvas(root, width=800, height=500, bg="black")
canvas.place(x=0, y=0)
#We want a animation like c-matrix on the background 
def animate():
    canvas.delete("all")
    # Set the font and text size
    font = ("Courier", 14)
    # Create a matrix-like effect by randomly generating and drawing characters
    for i in range(0, 800, 20):
        for j in range(0, 500, 20):
            char = chr(random.randint(33, 126))
            color = "#%06x" % random.randint(0, 0xFFFFFF)
            canvas.create_text(i, j, text=char, font=font, fill=color)
    # Call this function again after a short delay
    root.after(100, animate)

animate()

#Here we add our font
my_font = Font(
    size="30",
    weight="bold"
    )

#Frame for our list 
my_frame = Frame(root)
my_frame.pack(pady=10)

#Then we include the paramters for our list
my_list = Listbox(my_frame,
    font=my_font,
    width="30",
    height="5",
    bg="black",
    fg="white",
    highlightthickness="0")
my_list.pack(side=LEFT, fill="both")

# Fetch the "agenda" column from the "data" table and add them to the list
rows = db.execute("SELECT agenda FROM data")
for row in rows:
    my_list.insert(END, row["agenda"])

#Incuding scrollbar
my_scrollbar = Scrollbar(my_frame, troughcolor="black", bg="black", activebackground="white")
my_scrollbar.pack(side=RIGHT, fill="both")

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#Entry box to type the things
my_entry = Entry(root)
my_entry.pack(pady=20)

#Creating a frame for buttons ,so can be used later
button_frame = Frame(root)
button_frame.pack(pady=20)

#Functions
def delete_item():
    selected_item = my_list.get(ANCHOR)
    db.execute("DELETE FROM data WHERE agenda=?", selected_item)
    my_list.delete(ANCHOR)

def add_item():

    item = my_entry.get()
    if not item:
        return 0
    db.execute("INSERT INTO data (agenda) VALUES(?)", item)

    my_list.insert(END, item)

    my_entry(0, END)



#Defining buttons 
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="ADD Item", command=add_item)


#Using grid , we set the positions of the button
delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1)

root.mainloop()

#WE import the module 
#we create a root window
#we add some widgets
#We choose a layout ,a grid or pack or we use the place funstion to create GUI