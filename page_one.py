import tkinter as tk
from PIL import Image, ImageTk
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=800, height=600)
        self.controller = controller

        # Load the image using PIL
        self.bg_image = Image.open('medicrypt_HQ.png')
        self.bg_photo = controller.resize_image(self.bg_image, 800, 600)

        # Create a label to display the background image
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create other widgets
        label = tk.Label(self, text='This is page one', font=controller.title_font, bg="white")
        label.pack(side='top', fill='x', pady=10)

        button = tk.Button(self, text='Go to the Start Page', command=lambda: controller.show_frame('StartPage'))
        button.pack()

        # Ensure buttons and labels appear above the background
        label.lift()
        button.lift()
