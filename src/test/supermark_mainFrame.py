import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Supermark")
        #setting window size
        width=600
        height=420
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_528=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_528["font"] = ft
        GLabel_528["fg"] = "#333333"
        GLabel_528["justify"] = "center"
        GLabel_528["text"] = "Usuario"
        GLabel_528.place(x=0,y=10,width=70,height=30)

        GLineEdit_442=tk.Entry(root)
        GLineEdit_442["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_442["font"] = ft
        GLineEdit_442["fg"] = "#333333"
        GLineEdit_442["justify"] = "center"
        GLineEdit_442["text"] = "Entry"
        GLineEdit_442.place(x=70,y=10,width=200,height=30)

        GLabel_630=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_630["font"] = ft
        GLabel_630["fg"] = "#333333"
        GLabel_630["justify"] = "center"
        GLabel_630["text"] = "Contraseña"
        GLabel_630.place(x=280,y=10,width=82,height=31)

        GLineEdit_795=tk.Entry(root)
        GLineEdit_795["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_795["font"] = ft
        GLineEdit_795["fg"] = "#333333"
        GLineEdit_795["justify"] = "center"
        GLineEdit_795["text"] = "Entry"
        GLineEdit_795.place(x=370,y=10,width=150,height=30)

        GListBox_132=tk.Listbox(root)
        GListBox_132["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_132["font"] = ft
        GListBox_132["fg"] = "#333333"
        GListBox_132["justify"] = "center"
        GListBox_132.place(x=10,y=90,width=580,height=160)

        GLabel_367=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_367["font"] = ft
        GLabel_367["fg"] = "#333333"
        GLabel_367["justify"] = "center"
        GLabel_367["text"] = "Buscar"
        GLabel_367.place(x=10,y=50,width=73,height=30)

        GLineEdit_410=tk.Entry(root)
        GLineEdit_410["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_410["font"] = ft
        GLineEdit_410["fg"] = "#333333"
        GLineEdit_410["justify"] = "center"
        GLineEdit_410["text"] = "Entry"
        GLineEdit_410.place(x=90,y=50,width=470,height=30)

        GLabel_870=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_870["font"] = ft
        GLabel_870["fg"] = "#333333"
        GLabel_870["justify"] = "center"
        GLabel_870["text"] = "Carrito"
        GLabel_870.place(x=40,y=290,width=40,height=30)

        GListBox_0=tk.Listbox(root)
        GListBox_0["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_0["font"] = ft
        GListBox_0["fg"] = "#333333"
        GListBox_0["justify"] = "center"
        GListBox_0.place(x=90,y=300,width=320,height=100)

        GButton_424=tk.Button(root)
        GButton_424["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_424["font"] = ft
        GButton_424["fg"] = "#000000"
        GButton_424["justify"] = "center"
        GButton_424["text"] = "Comprar"
        GButton_424.place(x=420,y=300,width=170,height=30)
        GButton_424["command"] = self.GButton_424_command

        GButton_747=tk.Button(root)
        GButton_747["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_747["font"] = ft
        GButton_747["fg"] = "#000000"
        GButton_747["justify"] = "center"
        GButton_747["text"] = "Cancelar"
        GButton_747.place(x=420,y=340,width=170,height=30)
        GButton_747["command"] = self.GButton_747_command

        GCheckBox_647=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_647["font"] = ft
        GCheckBox_647["fg"] = "#333333"
        GCheckBox_647["justify"] = "center"
        GCheckBox_647["text"] = "Cliente"
        GCheckBox_647.place(x=530,y=10,width=58,height=30)
        GCheckBox_647["offvalue"] = "0"
        GCheckBox_647["onvalue"] = "1"
        GCheckBox_647["command"] = self.GCheckBox_647_command

        GButton_806=tk.Button(root)
        GButton_806["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_806["font"] = ft
        GButton_806["fg"] = "#000000"
        GButton_806["justify"] = "center"
        GButton_806["text"] = "Nuevo"
        GButton_806.place(x=80,y=260,width=60,height=25)
        GButton_806["command"] = self.GButton_806_command

        GButton_776=tk.Button(root)
        GButton_776["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_776["font"] = ft
        GButton_776["fg"] = "#000000"
        GButton_776["justify"] = "center"
        GButton_776["text"] = "Modificar"
        GButton_776.place(x=150,y=260,width=70,height=25)
        GButton_776["command"] = self.GButton_776_command

        GButton_519=tk.Button(root)
        GButton_519["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_519["font"] = ft
        GButton_519["fg"] = "#000000"
        GButton_519["justify"] = "center"
        GButton_519["text"] = "Eliminar"
        GButton_519.place(x=230,y=260,width=70,height=25)
        GButton_519["command"] = self.GButton_519_command

        GButton_464=tk.Button(root)
        GButton_464["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_464["font"] = ft
        GButton_464["fg"] = "#000000"
        GButton_464["justify"] = "center"
        GButton_464["text"] = "Limpiar"
        GButton_464.place(x=10,y=320,width=70,height=25)
        GButton_464["command"] = self.GButton_464_command

        GLabel_262=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_262["font"] = ft
        GLabel_262["fg"] = "#333333"
        GLabel_262["justify"] = "center"
        GLabel_262["text"] = "Productos"
        GLabel_262.place(x=10,y=260,width=70,height=25)

        GLabel_216=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_216["font"] = ft
        GLabel_216["fg"] = "#333333"
        GLabel_216["justify"] = "center"
        GLabel_216["text"] = "Usuario"
        GLabel_216.place(x=310,y=260,width=70,height=25)

        GButton_526=tk.Button(root)
        GButton_526["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_526["font"] = ft
        GButton_526["fg"] = "#000000"
        GButton_526["justify"] = "center"
        GButton_526["text"] = "Agregar"
        GButton_526.place(x=380,y=260,width=70,height=25)
        GButton_526["command"] = self.GButton_526_command

        GButton_578=tk.Button(root)
        GButton_578["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_578["font"] = ft
        GButton_578["fg"] = "#000000"
        GButton_578["justify"] = "center"
        GButton_578["text"] = "Editar"
        GButton_578.place(x=460,y=260,width=60,height=25)
        GButton_578["command"] = self.GButton_578_command

        GButton_103=tk.Button(root)
        GButton_103["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_103["font"] = ft
        GButton_103["fg"] = "#000000"
        GButton_103["justify"] = "center"
        GButton_103["text"] = "Borrar"
        GButton_103.place(x=530,y=260,width=60,height=25)
        GButton_103["command"] = self.GButton_103_command

    def GButton_424_command(self):
        print("command")


    def GButton_747_command(self):
        print("command")


    def GCheckBox_647_command(self):
        print("command")


    def GButton_806_command(self):
        print("command")


    def GButton_776_command(self):
        print("command")


    def GButton_519_command(self):
        print("command")


    def GButton_464_command(self):
        print("command")


    def GButton_526_command(self):
        print("command")


    def GButton_578_command(self):
        print("command")


    def GButton_103_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
