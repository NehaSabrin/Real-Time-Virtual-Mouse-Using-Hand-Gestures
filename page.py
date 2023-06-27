import tkinter as tk
from PIL import ImageTk, Image
import atexit
import subprocess

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#37A794')
        self.controller = controller
        self.controller.title("Application")
        self.controller.state("zoomed")
        self.controller.iconphoto(False, ImageTk.PhotoImage(Image.open("logo.png")))

        headinglabel1 = tk.Label(self, text = 'V-Mouse', font=('Garamond bold', 60), foreground='white', background='#37A794')
        headinglabel1.pack(fill='both',pady=350)

        button1 = tk.Button(self, text="Let's Start",
                           command=lambda: controller.show_frame("PageOne"),
                           relief='raised', borderwidth=3, width= 20, height=2,
                           font=('Garamond bold', 15), background='#FFC1CB', foreground='#074650', activebackground='#33AE81')
        button1.place(relx=0.5, rely=0.6, anchor='center')



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        label = tk.Label(self, text="Instruction Page 1", font=('Garamond bold', 30), foreground='black', background='white')
        label.pack(side="top", fill="both", pady=10)
        label_n = tk.Label(self, text="----Use Right Hand Only-----", font=('Garamond bold', 20), foreground='black',
                         background='white')
        label_n.pack(side="top", fill="both", pady=14)
        label_m = tk.Label(self, text="NOTE: IF ALL THE FINGERS ARE UP NO FUNCTIONS WILL BE PERFORMED",
                           font=('Garamond bold', 20), foreground='black',
                           background='white')
        label_m.pack(side="top", fill="both", pady=18)

        label1 = tk.Label(self, text="Right Click", width=21, height=3, font=('Garamond bold', 20), foreground='black', background='#37A794' )
        #label1.pack(side='left', padx=100, pady=10, ipady=10)
        label1.place(relx = 0.2, rely = 0.3, anchor = 'center')
        label1_n = tk.Label(self, text="When index finger is UP\nand middle finger is half closed\nthen right click will be performed.\n(rest all fingers should\nbe fully closed)",
                            width=28, height=8, font=('Garamond bold', 15), foreground='black',
                          background='#37A794')
        # label1.pack(side='left', padx=100, pady=10, ipady=10)
        label1_n.place(relx=0.2, rely=0.5, anchor='center')


        label2 = tk.Label(self, text="Left Click", width=21, height=3, font=('Garamond bold', 20), foreground='black', background='#37A794')
        #label2.pack(side='left', padx=100, pady=10, ipady=10)
        label2.place(relx=0.5, rely=0.3, anchor='center')
        label2_n = tk.Label(self,
                            text="When middle finger is UP\nand index finger is half closed\nthen left click will be performed.\n(rest all fingers should\nbe fully closed)",
                            width=28, height=8, font=('Garamond bold', 15), foreground='black',
                            background='#37A794')
        # label1.pack(side='left', padx=100, pady=10, ipady=10)
        label2_n.place(relx=0.5, rely=0.5, anchor='center')


        label3 = tk.Label(self, text="Double Click", width=21, height=3, font=('Garamond bold', 20), foreground='black', background='#37A794')
        #label3.pack(side='left',padx=100, pady=10, ipady=10)
        label3.place(relx=0.8, rely=0.3, anchor='center')
        label3_n = tk.Label(self,
                            text="When index finger and middle finger\nis UP and the distance between\nthem is less then 40px then\ndouble click will be performed.\n(rest all fingers should\nbe fully closed)",
                            width=28, height=8, font=('Garamond bold', 15), foreground='black',
                            background='#37A794')
        # label1.pack(side='left', padx=100, pady=10, ipady=10)
        label3_n.place(relx=0.8, rely=0.5, anchor='center')

        button = tk.Button(self, text="Next",
                           command=lambda: controller.show_frame("PageTwo"),
                           relief = 'raised', borderwidth = 3, width = 20, height = 2,
                           font = ('Garamond bold',15), background = '#FFC1CB', foreground = '#074650', activebackground = '#33AE81')
        button.place(relx=0.5, rely=0.8, anchor='center')

        def run():
            app.state("iconic")
            subprocess.call(['python','VirtalMouse.py'])

        button1 = tk.Button(self, text="Start Camera",
                           command=run,
                           relief='raised', borderwidth=3, width=20, height=2,
                           font=('Garamond bold', 15), background='#FFC1CB', foreground='#074650',
                           activebackground='#33AE81')
        button1.place(relx=0.5, rely=0.9, anchor='center')


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller

        label = tk.Label(self, text="Instruction Page 2", font=('Garamond bold', 30), foreground='black',
                         background='white')
        label.pack(side="top", fill="both", pady=10)
        label_n = tk.Label(self, text="----Use Right Hand Only-----", font=('Garamond bold', 20), foreground='black',
                           background='white')
        label_n.pack(side="top", fill="both", pady=14)
        label_m = tk.Label(self, text="NOTE: IF ALL THE FINGERS ARE UP NO FUNCTIONS WILL BE PERFORMED", font=('Garamond bold', 20), foreground='black',
                           background='white')
        label_m.pack(side="top", fill="both", pady=18)


        label1 = tk.Label(self, text="Curser Move", width=21, height=3, font=('Garamond bold', 20), foreground='black',
                          background='#37A794')
        # label1.pack(side='left', padx=100, pady=10, ipady=10)
        label1.place(relx=0.2, rely=0.3, anchor='center')
        label1_n = tk.Label(self,
                            text="When index finger and middle finger\nis UP and the gesture make the\n V-shape then curser will move.\n(rest all fingers should\nbe fully closed)",
                            width=28, height=8, font=('Garamond bold', 15), foreground='black',
                            background='#37A794')
        # label1.pack(side='left', padx=100, pady=10, ipady=10)
        label1_n.place(relx=0.2, rely=0.5, anchor='center')

        label2 = tk.Label(self, text="Drag and Drop", width=21, height=3, font=('Garamond bold', 20), foreground='black',
                          background='#37A794')
        # label2.pack(side='left', padx=100, pady=10, ipady=10)
        label2.place(relx=0.5, rely=0.3, anchor='center')
        label2_n = tk.Label(self,
                            text="To drag any object half close\nthe middle and index finger.\nTo Drop any object open\nindex and middle finger.\n(rest all fingers should\nbe fully closed)",
                            width=28, height=8, font=('Garamond bold', 15), foreground='black',
                            background='#37A794')
        # label1.pack(side='left', padx=100, pady=10, ipady=10)
        label2_n.place(relx=0.5, rely=0.5, anchor='center')

        label3 = tk.Label(self, text="MultiItem selection", width=21, height=3, font=('Garamond bold', 20), foreground='black',
                          background='#37A794')
        # label3.pack(side='left',padx=100, pady=10, ipady=10)
        label3.place(relx=0.8, rely=0.3, anchor='center')
        label3_n = tk.Label(self,
                            text="When all the fingers are closed\nthen selection will be performed\nto stop the selection mode\nopen index and middle finger.",
                            width=28, height=8, font=('Garamond bold', 15), foreground='black',
                            background='#37A794')
        # label1.pack(side='left', padx=100, pady=10, ipady=10)
        label3_n.place(relx=0.8, rely=0.5, anchor='center')

        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("PageOne"),
                           relief='raised', borderwidth=3, width=20, height=2,
                           font=('Garamond bold', 15), background='#FFC1CB', foreground='#074650',
                           activebackground='#33AE81')
        button.place(relx=0.5, rely=0.8, anchor='center')

        def run():
            app.state("iconic")
            subprocess.call(['python','VirtalMouse.py'])

        button1 = tk.Button(self, text="Start Camera",
                            command=run,
                            relief='raised', borderwidth=3, width=20, height=2,
                            font=('Garamond bold', 15), background='#FFC1CB', foreground='#074650',
                            activebackground='#33AE81')
        button1.place(relx=0.5, rely=0.9, anchor='center')



if __name__ == "__main__":
    app = SampleApp()


    def doSomethingOnExit():
        pass


    atexit.register(doSomethingOnExit)
    app.mainloop()
