import tkinter as tk
from tkinter import Tk,Label as lbl,Button as btn,Entry as unitxt,Frame
from tkinter.scrolledtext import ScrolledText as txtarea
from muconv import raw2csv,HDR_ROW
from tkinter.ttk import Combobox as combo,Treeview as tree
from tkinter.filedialog import asksaveasfile as savefile,askopenfile as openfile
import PyPDF2
import csv

def show_res():
    data=txtarea1.get("0.0","end-1c")
    hdr=e1.get()
##    if hdr=="TYCS":
##        hdr=HDR_ROW
    hdr=HDR_ROW
    op=raw2csv(data,hdr)
    txtarea2.configure(state="normal")
    txtarea2.delete("0.0","end-1c")
    txtarea2.insert("end",op)
    txtarea2.configure(state="disabled")

def clripop():
    txtarea1.delete("0.0","end-1c")
    txtarea2.configure(state="normal")
    txtarea2.delete("0.0","end-1c")
    txtarea2.configure(state="disabled")
def cptxt():
    root.clipboard_clear()
    root.clipboard_append(txtarea2.get("0.0",'end-1c'))
    root.update()
def expfile():
    file=savefile(defaultextension=".csv")
    file.write(txtarea2.get("0.0",'end-1c'))
    if file is None:
        return
    file.close()
def opnfile():
##    file=openfile("rb")
##    preader=PyPDF2.PdfFileReader(file.name)
    preader=PyPDF2.PdfFileReader(r"/home/om/Downloads/1S00155 (1).pdf")
    print(preader.getNumPages())
    po=preader.getPage(262)
    e=po.extractText()
    e=" ".join(e.split())
    print(e)
    if file is None:
        return
    file.close()
    txtarea1.delete("0.0","end-1c")
    txtarea1.insert("end",e)
def viewdata():
    reader=csv.DictReader(txtarea2.get("0.0",'end-1c'),delimiter=',')
    txtarea2.grid_forget()
    tree1.grid(column=0,row=4,columnspan=2)
    pass
def viewcsv():
    reader=csv.DictReader(txtarea2.get("0.0",'end-1c'),delimiter=',')
    tree1.grid_forget()
    txtarea2.grid(column=0,row=4,columnspan=2)
    pass
root=Tk()
root.title("MU MARKS CONVERTER GUI")
#root.geometry('650x750')
lbl1 = lbl(root, text="Header")
lbl1.grid(column=0, row=0)
##e1=unitxt(root)
##e1.grid(column=1,row=0)
e1=combo(root,values=["TYCS"])
e1.current(0)
e1.grid(column=1,row=0)
txtarea1=txtarea(root)
txtarea1.grid(column=0,row=2,columnspan=2)
btn1 = btn(root, text="Clear",command=clripop)
btn1.grid(column=0, row=3)
btn2 = btn(root, text="Convert To CSV",command=show_res)
btn2.grid(column=1, row=3)
txtarea2=txtarea(root,state="disabled")
txtarea2.grid(column=0,row=4,columnspan=2)
tree1=tree(columns=["1"],selectmode="browse")
btn3 = btn(root, text="Copy CSV Contents",command=cptxt)
btn3.grid(column=0, row=5)
btn4 = btn(root, text="Export To File",command=expfile)
btn4.grid(column=1, row=5)
btn5 = btn(root, text="View in Table Format",command=opnfile)
btn5.grid(column=0, row=6)
btn6 = btn(root, text="View in CSV Format",command=viewcsv)
btn6.grid(column=1, row=6)
root.mainloop()


