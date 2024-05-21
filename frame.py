#from tkinter import *
#import os
#from tkinter import filedialog as fd

import tkinter as tk
from PIL import Image, ImageTk

# resizing background logo if user resizes window
def resize_logo(event):
    # get the current size of the root
    new_width = event.width
    new_height = event.height

    # original image resizing to fit new window size
    resized_logo = original_logo.resize((new_width, new_height), Image.LANCZOS)
    new_image = ImageTk.PhotoImage(resized_logo)

    # label update with resized image
    bg_label.config(image=new_image)
    #bg_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    bg_label.image = new_image # garbage collection purposes

def test_window():
    global original_logo, bg_label

    root = tk.Tk()
    root.title('This is my test window')
    root.geometry("1080x1080")  # setting the size for main window'

    # add image to background???

    original_logo = Image.open('medicrypt_logo.jpeg')
    image = ImageTk.PhotoImage(original_logo)

    # hold our logo
    bg_label = tk.Label(root, image=image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.bind("<Configure>", resize_logo)


    # work to keep entry and button shiftable when window is resized
    button = tk.Button(root, text="Hello World!", bg="gray")
    button.place(x=200, y=100, anchor=tk.CENTER)
    entry = tk.Entry(root)
    entry.place(x=500, y=600, anchor=tk.CENTER)

    quit = tk.Button(root, text="Quit", command=root.destroy)
    quit.place(x=100, y=105)

    root.mainloop()

test_window()

# def open_file_selection():
   # files = fd.askopenfilenames(filetypes=[("All Files", "*.*")])
   # for files in files:
      #  print(files)


#if __name__ == '__main__':
    #test_window()
