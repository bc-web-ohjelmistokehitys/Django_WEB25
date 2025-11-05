from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class SimpleViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Image Viewer")
        self.img = None
        Button(root, text="Open Image", command=self.open_image).pack()
        self.label = Label(root, text="No image loaded")
        self.label.pack()

    def open_image(self):
        path = filedialog.askopenfilename(filetypes=[("Images","*.jpg *.png *.jpeg")])
        if not path: return
        self.img = Image.open(path)
        self.show(self.img)

    def show(self, image):
        tk_img = ImageTk.PhotoImage(image.resize((400,400)))
        self.label.config(image=tk_img, text="")
        self.label.image = tk_img


root = Tk()
SimpleViewer(root)
root.mainloop()
