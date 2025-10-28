import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageEnhance

class Editor:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Image Editor")
        self.images, self.current = [], None

        self.frame = Frame(root); self.frame.pack()
        Button(self.frame, text="Open Folder", command=self.load_folder).pack(side=LEFT)
        Button(self.frame, text="Gray", command=self.to_gray).pack(side=LEFT)
        Button(self.frame, text="Blur", command=self.blur).pack(side=LEFT)
        Button(self.frame, text="Contrast+", command=self.boost).pack(side=LEFT)
        Button(self.frame, text="Save As", command=self.save).pack(side=LEFT)

        self.listbox = Listbox(root, width=40); self.listbox.pack(side=LEFT, fill=Y)
        self.listbox.bind("<<ListboxSelect>>", self.show_image)

        self.label = Label(root); self.label.pack(side=RIGHT)

    def load_folder(self):
        folder = filedialog.askdirectory()
        if not folder: return
        self.images = [os.path.join(folder,f) for f in os.listdir(folder)
                       if f.lower().endswith((".jpg",".jpeg",".png"))]
        self.listbox.delete(0,END)
        for f in self.images: self.listbox.insert(END, os.path.basename(f))

    def show_image(self, e=None):
        if not self.listbox.curselection(): return
        path = self.images[self.listbox.curselection()[0]]
        self.current = Image.open(path)
        self.display(self.current)

    def display(self, img):
        tkimg = ImageTk.PhotoImage(img.resize((400,400)))
        self.label.config(image=tkimg); self.label.image = tkimg

    def to_gray(self):
        if self.current: self.display(self.current.convert("L").convert("RGB"))

    def blur(self):
        if self.current: self.display(self.current.filter(ImageFilter.BLUR))

    def boost(self):
        if self.current: self.display(ImageEnhance.Contrast(self.current).enhance(1.5))

    def save(self):
        if self.label.image:
            path = filedialog.asksaveasfilename(defaultextension=".png")
            if path: self.current.save(path)

root = Tk()
Editor(root)
root.mainloop()