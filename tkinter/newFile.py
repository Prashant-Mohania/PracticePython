import tkinter
from tkinter import ttk
import sys


def cancel():
    sys.exit()


def newfile():
    pass


def pymain():
    py_main = tkinter.Tk()
    py_main.title('New File')

    # file name label and entry box
    nameVar = tkinter.StringVar()
    ttk.Label(py_main, text='Name').grid(row=0, column=0, sticky=tkinter.W)
    ttk.Entry(py_main, textvariable=nameVar).grid(
        row=0, column=1, padx=10, pady=2)

    # file type label and entry box
    typeVar = tkinter.StringVar()
    ttk.Label(py_main, text='File type').grid(
        row=1, column=0, sticky=tkinter.W)
    ttk.Entry(py_main, textvariable=typeVar).grid(
        row=1, column=1, padx=10, pady=2)

    newVar = tkinter.StringVar()
    ttk.Button(py_main, text='OK', value='ok',
               variable=newVar).grid(row=0, column=3)

    # cancelVar = tkinter.StringVar()
    ttk.Button(py_main, text='OK', value='cancel',
               variable=newVar).grid(row=1, column=3)

    # if newVar == 'ok':

    py_main.mainloop()


if __name__ == "__main__":
    pymain()
