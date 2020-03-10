from tkinter import*
from tkinter import filedialog
root=Tk()

def abrefichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="/home/andres/Documents", 
    filetypes=(("archivos pdf","*.pdf"),("archivos txt","*.txt" )))
    print(fichero)

Button(root, text="Abrir fichero", command=abrefichero).pack()
root.mainloop()

