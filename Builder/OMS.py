#OMS
import fitz,re,os,sys,subprocess
from tkinter import Tk,Menu,Label,Entry,Button,messagebox,Image,PhotoImage,Toplevel,Text,LEFT,Frame,Scrollbar,Canvas,OptionMenu,StringVar,RIGHT,Listbox,YES,CENTER
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfile,asksaveasfile
from tkinter import END,dnd

fcolor="#d9d0d9"#"#d9d0d9"
bcolor="#551a8b"#"#500080"
mfcolor="#d9d0d9"
mbcolor="#6f2da8"#"#5000a0"

entryipad=76
opmnwidth=7
class OMS:
    def __init__(self,master):
        self.master=master
        self.master.title("OMS MARKSHEET SIMPLIFIER")
        #self.master.overrideredirect(True)
        self.master.geometry('411x195+200+200')
        
        self.currfilename=""
        self.setMenu()
        self.interval=50
        self.setUI()
    def setMenu(self):
        self.menubar=Menu(self.master,bg=bcolor,fg=fcolor,relief="raised")
        self.master.config(menu=self.menubar)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open",command=self.sel_file)
        self.filemenu.add_command(label="Exit",command=self.master.destroy)
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        #self.helpmenu = Menu(self.menubar, tearoff=0)
        #self.menubar.add_cascade(label="Help",menu=self.helpmenu)
        #self.aboutmenu = Menu(self.menubar, tearoff=0,command=self.aboutdev)
        self.menubar.add_command(label="About Dev",command=self.aboutdev)
    def aboutdev(self):
        messagebox.showinfo('About OMS','OMS Marksheet Simplifier\nDeveloped by Omprakash Kambli\n')
    def setUI(self):
        self.master.configure(background=bcolor)
        self.lblh = Label(self.master, text="Select File")
        self.lblh.grid(row=0,column=0,columnspan=5,ipady=15)
        self.lbl1 = Label(self.master, text="Filepath:         ")
        self.lbl1.grid(row=1,column=0)
        self.entry1 = Entry(self.master)
        self.entry1.grid(row=1,column=1,columnspan=3,ipadx=entryipad)
        #self.entry1.insert(0,r"/home/om/Downloads/1S00155.pdf")
        self.entry1.configure(disabledforeground=fcolor,disabledbackground=bcolor,highlightthickness=0,state='disabled')
        self.btnvdata = Button(self.master, text="Browse",command=self.sel_file)
        self.btnvdata.grid(row=1,column=4)
        self.selsublbl=Label(self.master,text="Format:          ")
        self.selsublbl.grid(row=2,column=0)
        self.pgrnglbl=Label(self.master,text="Page Range:   ")
        self.pgrnglbl.grid(row=2,column=2)
        self.srchlbl=Label(self.master,text="Search Query:")
        self.srchlbl.grid(row=4,column=0)
        self.textvar,self.textvar2=StringVar(),StringVar()
        self.options=["CS","IT1","IT2"]
        self.textvar.set(self.options[0])
        self.selsub=OptionMenu(self.master,self.textvar,*self.options)   
        self.selsub.grid(row=2,column=1)
        self.selsub.configure(bg=bcolor,fg=fcolor,width=4)
        self.selsub['menu'].configure(bg=bcolor,fg=fcolor)
        self.btn2 = Button(self.master, text="Extract Contents",command=self.func_ext)
        self.btn2.grid(row=5,column=2,pady=15)
        #self.totpg=420
        # self.var1=self.totpg%50
        # self.var2=self.totpg//50
        # self.var3=self.var1+self.var2*50
        # self.li,self.options2=[],[]
        # for i in range(0,self.totpg,50):
        #     self.li.append(i)
        # self.li.append(self.totpg)
        # print(self.li)
        # for i in range(len(self.li)):
        #     if(i!=0):
        #         print(self.li[i-1],self.li[i])
        #         self.options2.append([self.li[i-1],self.li[i]])
        # print(self.options2)
        #print(self.var3)
        self.options2=[""]
        self.selrng=OptionMenu(self.master,self.textvar2,*self.options2)
        self.selrng.grid(row=2,column=3)
        self.selrng.configure(width=opmnwidth)
        self.entry2 = Entry(self.master)
        self.entry2.grid(row=4,column=1,columnspan=3,ipadx=entryipad)
        self.master.rowconfigure(0)
        self.master.rowconfigure(1)
        self.master.rowconfigure(2)
        self.master.rowconfigure(3)
        self.master.rowconfigure(4)
        
        for widget in self.master.winfo_children():
            widget.configure(bg=bcolor,fg=fcolor)
        self.menubar.configure(bg=mbcolor,fg=mfcolor)

    def func_set_pgnos(self):
        try:
            self.pread=fitz.open(self.entry1.get())
            # print(self.pread.pageCount)
            
            # print(str(self.pread)[10:-2])
            # self.entry1.delete(0,END)
            # self.entry1.insert(0,self.pread.getNumPages())
        except Exception as e:
            #print(r"An Error Occured Not a PDF")
            #print(e)
            pass
    def sel_file(self):
        try:
            self.selected_file=askopenfile("rb",filetypes=[("PDF Files Only","*.pdf")])
            if(bool(self.selected_file)):
                self.entry1.configure(state='normal')
                
                self.entry1.delete(0,END)
                self.entry1.insert(0,self.selected_file.name)
                self.entry1.configure(state='disabled')
                
                try:
                    self.func_set_pgnos()
                    self.upd_page_rng(self.pread.pageCount,100)
                except Exception as e:
                    print(e)
        except:
            messagebox.showerror("File Not Selected","Please Select a Proper File")
    def sel_regex(self,sel_format):
        if(sel_format=="CS"):
            S1="LSA"
            S2="STQA"
            P1=S1+r"+"+S2+"_Prac"
            S3="INS"
            S4="WS"
            P2=S3+r"+"+S4+"_Prac"
            S5="GP"
            P3=S5+r"_Prac"
            P4="PROJ"
            
            return self.stret(r"SNO,M/F,NAME"+
            r",{0}_Th,{0}_Th_G,{0}_In,{0}_In_G,{0}_Total,{0}_C,{0}_G,{0}_GP,{0}_C*GP".format(S1)+
            r",{0}_Th,{0}_Th_G,{0}_In,{0}_In_G,{0}_Total,{0}_C,{0}_G,{0}_GP,{0}_C*GP".format(S2)+
            r",{0}_Total,{0}_C,{0}_G,{0}_GP,{0}_C*GP".format(P1)+
            r",{0}_Th,{0}_Th_G,{0}_In,{0}_In_G,{0}_Total,{0}_C,{0}_G,{0}_GP,{0}_C*GP".format(S3)+
            r",RES,COLLEGE"+
            r",{0}_Th,{0}_Th_G,{0}_In,{0}_In_G,{0}_Total,{0}_C,{0}_G,{0}_GP,{0}_C*GP".format(S4)+
            r",{0}_Total,{0}_C,{0}_G,{0}_GP,{0}_C*GP".format(P2)+
            r",{0}_Th,{0}_Th_G,{0}_In,{0}_In_G,{0}_Total,{0}_C,{0}_G,{0}_GP,{0}_C*GP".format(S5)+
            r",{0}_Total,{0}_C,{0}_G,{0}_GP,{0}_C*GP".format(P3)+
            r",{0}_Total,{0}_C,{0}_G,{0}_GP,{0}_C*GP".format(P4)+
            r",CP_Total,GP_Total,Grade"
            )
        elif(sel_format=="IT1"):
            return r"SNO,M/F,NAME,PRN,CLG,M1,G1,M2,G2,M3,G3,M4,G4,M5,G5,M6,G6,M7,G7,M8,G8,M9,G9,M10,G10,TOT1,GP1,G1,C1,CG1,TOT2,GP2,G2,C2,CG2,TOT3,GP3,G3,C3,CG3,TOT4,GP4,G4,C4,CG4,TOT5,GP5,G5,C5,CG5,TOTM,RESREM,TOT1,GP1,G1,C1,CG1,TOT2,GP2,G2,C2,CG2,TOT3,GP3,G3,C3,CG3,TOT4,GP4,G4,C4,CG4,TOT5,GP5,G5,C5,CG5,TC,TCG,TGPA,"
        else:
            return r"T"
    def find_missing(self,lst):
        start = int(lst[0])
        end = int(lst[-1])
        #print(start)
        #print(end)
        for i in range(start,end):
            if(str(i) not in lst):
                #print(i)
                pass
        
    def func_ext(self):
        self.resset=[]
        self.pgnos=[]
        self.q=[]
        s=self.textvar2.get()
        self.currtext=""
        if(self.entry1.get()==""):
            messagebox.showinfo("File Not Selected","Click on the browse button and select a file")
        
        
        else:
            stuple = tuple(map(int, s.replace('(','').replace(')','').split(',')))
            start=stuple[0]
            end=stuple[1]
            qtext=self.entry2.get().upper()
            print(qtext)
            self.slist=[]
            if(qtext.isspace()):
                messagebox.showinfo("Please enter valid query","String contains only spaces")
            elif(qtext=="" or qtext==None):
                for i in range(start,end):
                    #print(i)
                    self.currtext=self.currtext+self.pread.getPageText(i)
                    self.currtext=" ".join(self.currtext.split()).upper()
                    self.currtext=self.currtext.replace(r",","").replace(r" +","+").replace(r"0A","0 A").replace(r"E1","E 1").replace(r"F-","F -").replace(r"$"," ").replace(r" + ","").replace(r"@1","").replace(r"@2","").replace(r"@3","").replace(r"@4","").replace(r"@5","").replace(r"@6","").replace(r"*","").replace(r"#","").replace(r"0+","0").replace(r"1+","1").replace(r"2+","2").replace(r"3+","3").replace(r"4+","4").replace(r"5+","5").replace(r"6+","6").replace(r"7+","7").replace(r"8+","8").replace(r"9+","9").replace("----","-- --").replace(r"+0","+ 0").replace(r"+1","+ 1").replace(r"+2","+ 2").replace(r"+3","+ 3").replace(r"+4","+ 4").replace(r"+5","+ 5").replace(r"+6","+ 6").replace(r"+7","+ 7").replace(r"+8","+ 8").replace(r"+9","+ 9").replace("1 E","1E").replace("2 E","2E").replace("3 E","3E").replace("4 E","4E").replace("5 E","5E").replace("6 E","6E").replace("7 E","7E").replace("8 E","8E").replace("9 E","9E").replace("0 E","0E")
                    self.q=re.findall(self.return_regex(self.textvar.get()),self.currtext)
                    #print(self.q)
                #print(len(self.q))
                #print(self.q[0])

                for i in self.q:
                    if(str(qtext) in str(i)):
                        self.resset.append(i)
                        self.slist.append(i[0])
                self.find_missing(self.slist)
                #messagebox.showinfo("Results of Query",str(len(self.resset))+" Records Found")
                self.expdata=""
                self.rexexp=self.sel_regex(self.textvar.get())
                if(len(self.resset)!=0):
                    for i in self.resset:
                        for j in i:
                            self.expdata=self.expdata+str(j)+r","
                        self.expdata=self.expdata+"\n"
                    self.rexexp=self.rexexp+"\n"+self.expdata
                    #print(self.rexexp[-1])
                    mbox=messagebox.askquestion("Results of Query",str(len(self.resset))+" Records Found\nDo you want to save these to a file")
                    if mbox=="yes":
                        self.file_save(self.rexexp)
                        self.file_open(self.currfilename)
                    else:
                        pass

            else:
                #print(qtext)
                for i in range(start,end):
                    #print(i)
                    self.currtext=self.pread.getPageText(i)
                    self.currtext=" ".join(self.currtext.split()).upper()
                    self.currtext=self.currtext.replace(r",","").replace(r" +","+").replace(r"0A","0 A").replace(r"E1","E 1").replace(r"F-","F -").replace(r"$","").replace(r" + ","").replace(r"@1","").replace(r"@2","").replace(r"@3","").replace(r"@4","").replace(r"@5","").replace(r"@6","").replace(r"*","").replace(r"#","").replace(r"0+","0").replace(r"1+","1").replace(r"2+","2").replace(r"3+","3").replace(r"4+","4").replace(r"5+","5").replace(r"6+","6").replace(r"7+","7").replace(r"8+","8").replace(r"9+","9").replace("----","-- --").replace(r"+0","+ 0").replace(r"+1","+ 1").replace(r"+2","+ 2").replace(r"+3","+ 3").replace(r"+4","+ 4").replace(r"+5","+ 5").replace(r"+6","+ 6").replace(r"+7","+ 7").replace(r"+8","+ 8").replace(r"+9","+ 9").replace("1 E","1E").replace("2 E","2E").replace("3 E","3E").replace("4 E","4E").replace("5 E","5E").replace("6 E","6E").replace("7 E","7E").replace("8 E","8E").replace("9 E","9E").replace("0 E","0E")
                    self.q=re.findall(qtext,self.currtext)
                    if(len(self.q)!=0):
                        # print("Page"+str(n))
                        self.pgnos.append(i)
                    self.q=[]
                #print(self.pgnos)
                self.currtext=""
                for i in self.pgnos:
                    self.currtext=self.currtext+self.pread.getPageText(i)
                    self.currtext=" ".join(self.currtext.split()).upper()
                    self.currtext=self.currtext.replace(r",","").replace(r" +","+").replace(r"0A","0 A").replace(r"E1","E 1").replace(r"F-","F -").replace(r"$","").replace(r" + ","").replace(r"@1","").replace(r"@2","").replace(r"@3","").replace(r"@4","").replace(r"@5","").replace(r"@6","").replace(r"*","").replace(r"#","").replace(r"0+","0").replace(r"1+","1").replace(r"2+","2").replace(r"3+","3").replace(r"4+","4").replace(r"5+","5").replace(r"6+","6").replace(r"7+","7").replace(r"8+","8").replace(r"9+","9").replace("----","-- --").replace(r"+0","+ 0").replace(r"+1","+ 1").replace(r"+2","+ 2").replace(r"+3","+ 3").replace(r"+4","+ 4").replace(r"+5","+ 5").replace(r"+6","+ 6").replace(r"+7","+ 7").replace(r"+8","+ 8").replace(r"+9","+ 9").replace("1 E","1E").replace("2 E","2E").replace("3 E","3E").replace("4 E","4E").replace("5 E","5E").replace("6 E","6E").replace("7 E","7E").replace("8 E","8E").replace("9 E","9E").replace("0 E","0E")
                    self.q=re.findall(self.return_regex(self.textvar.get()),self.currtext)
                #print(len(self.q))
                for i in self.q:
                    if(str(qtext) in str(i)):
                        self.resset.append(i)
                #messagebox.showinfo("Results of Query",str(len(self.resset))+" Records Found")
                self.expdata=""
                self.rexexp=self.sel_regex(self.textvar.get())
                if(len(self.resset)!=0):
                    for i in self.resset:
                        tlist=list(i)
                        if(i[1]==r'/'):
                            tlist[1]='F'
                            #print('F')
                        else:
                            tlist[1]='M'
                            #print('M')
                        i=tuple(tlist)
                        for j in i:
                            self.expdata=self.expdata+str(j)+r","
                        self.expdata=self.expdata+"\n"
                    self.rexexp=self.rexexp+"\n"+self.expdata
                    print(self.rexexp)
                    mbox=messagebox.askquestion("Results of Query",str(len(self.resset))+" Records Found\nDo you want to save these to a file")
                    if mbox=="yes":
                        self.file_save(self.rexexp)
                        self.file_open(self.currfilename)
                    else:
                        pass
                else:
                    messagebox.showinfo("Results of Query",str(len(self.resset))+" Records Found")
            








            
        # else:
        #     for i in range(start,end):
        #         self.currtext=self.pread.getPageText(i)
        #         self.currtext=" ".join(self.currtext.split()).upper()
        #         self.currtext=self.currtext.replace(r"$","").replace(r"@1","").replace(r"@2","").replace(r"@3","").replace(r"@4","").replace(r"@5","").replace(r"@6","").replace(r"*","").replace(r"#","")
        #         self.q=re.findall(self.return_regex(self.textvar.get()),self.currtext)
        #         if(len(self.q)!=0):
        #             # print("Page"+str(n))
        #             self.pgnos.append(i)
        #         self.q=[]
                
        #     print(self.pgnos)
        # if(len(self.pgnos)!=0):
        #     for i in self.pgnos:
        #         #print(i)
        #         self.currtext=self.pread.getPageText(i)
        #         self.currtext=" ".join(self.currtext.split()).upper()
        #         self.currtext=self.currtext.replace(r"$","").replace(r"@1","").replace(r"@2","").replace(r"@3","").replace(r"@4","").replace(r"@5","").replace(r"@6","").replace(r"*","").replace(r"#","")
        #         self.q=re.findall(qtext,self.currtext)
        #         #print(self.q)
        #     print(self.q[0])
            
        # else:
        #     messagebox.showinfo("No Records Found","Nothing")
        # #print(self.q)
    def file_save(self,data):
        f = asksaveasfile(mode='w', defaultextension=".csv")
        if f is None:
            return
        else:
            f.write(data)
        self.currfilename=f.name
        f.close()
        #print(self.currfilename)
        
        
    def file_open(self,file):
        print(file)
        print(sys.platform)
        if(sys.platform=="win32"):
            os.startfile(file)
        elif(sys.platform=="darwin"):
            subprocess.call(["open",file])
        else:
            subprocess.call(["xdg-open",file])
            
    def return_regex(self,val):
        if(val=="IT1"):
            value=self.stret(r"""(\d{7})\s?"""+
            r"""(\/?)([A-Z\s\.\']*)\s?"""+
            r"""\((\d{0,})\)\s?"""+
            r"""(\d{1,}\:{1}[\D]*)"""+
            r"""(\d{0,2}E?A?F?\+?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}E?A?F?\+?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}E?A?F?\+?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}E?A?F?\+?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}E?A?F?\+?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}E?A?F?\+?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}E?A?F?\+?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}E?A?F?\+?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}E?A?F?\+?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}E?A?F?\+?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            
            r"""(\d{0,3}E?A?F?\+?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,3}E?A?F?\+?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,3}E?A?F?\+?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,3}E?A?F?\+?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,3}E?A?F?\+?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{1,3})\s+?"""+
            r"""(\D{0,10})\s+?"""+
             

             
            r"""(\d{0,3}E?A?F?\+?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}E?A?F?\+?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}E?A?F?\+?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,3}E?A?F?\+?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,3}E?A?F?\+?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
             
            r"""(\d{0,2})\s+?"""+
            r"""(\d{0,3})\s+?"""+
            r"""(\d{0,2}\.?\d{0,2}\-{0,2})"""+
            r"""""")
        elif(val=="IT2"):
            value=self.stret(
            r"""(\d{7})\s?"""+
            r"""(\/?)([A-Z\s\.\']*)\s?"""+
            r"""\((\d{0,})\)\s?"""+
            r"""(\d{1,}\:{1}[\D]*)"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            
            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{1,3})\s+?"""+
            r"""(\D{0,10})\s+?"""+

            
            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{1,2})\s+?"""+
            r"""(\d{1,3})\s+?"""+
            r"""(\d{0,2}\.?\d{0,2}\-{0,2})\s+?"""+
            r"""([A-FO\-\+]{0,2})"""+
            r""""""
            )
        elif(val=="CS"):
            value=self.stret(
                r"(\d{7})\s?"+
                r"""(\/?)"""+
                r"""([A-Z\s\.\']*)"""+

                r"""(\d{1,2}[FE]?|[AFE]|\-{2})\s"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,2}[FE]?|[AFE]|\-{2})\s"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,3}[FE]?|[AFE]|\-{2})\s"""+
                r"""([3]|\-{2})\s"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,2}|\-{2})\s"""+
                r"""(\d{1,2}\.\d{2}|\-{2}|[A])\s"""+

                r"""(\d{1,2}[FE]?|[AFE]|\-{2})\s"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,2}[FE]?|[AFE]|\-{2})\s"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,3}[FE]?|[AFE]|\-{2})\s"""+
                r"""([3]|\-{2})\s"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,2}|\-{2})\s"""+
                r"""(\d{1,2}\.\d{2}|\-{2}|[A])\s"""+

                r"""(\d{1,3}[FE]?|[AFE]|\-{2})\s"""+
                r"""([2]|\-{2})\s"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,2}|\-{2})\s"""+
                r"""(\d{1,2}[EF]?|\-{2})\s?"""+

                r"""(\d{1,2}[FE]?|[AFE]|\-{2})\s"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,2}[FE]?|[AFE]|\-{2})\s"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,3}[FE]?|[AFE]|\-{2})\s"""+
                r"""([3]|\-{2})\s"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,2}|\-{2})\s"""+
                r"""(\d{1,2}\.\d{2}|\-{2}|[A])\s"""+

                r"""([PAF]\s|\sRPV|\sABS|\sRPV\sABS)"""+
                r"""(\D*)"""+
                
                ##Third Line
                r"""(\d{1,2}[FE]?|[AFE]|\-{2})\s"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,2}[FE]?|[AFE]|\-{2})\s"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,3}E?|[AFE]|\-{2})\s"""+
                r"""([3]|\-{2})\s"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,2}|\-{2})\s"""+
                r"""(\d{1,2}\.\d{2}|\-{2}|[A])\s?"""+

                
                r"""(\d{1,3}[EAF]?|[AFE]|\-{2})\s?"""+
                
                r"""([2]|\-{2}|[AF])\s?"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,2}|\-{2})\s"""+
                r"""(\d{1,2}|\-{2})\s"""+
                
                r"""(\d{1,2}[FE]?|[AFE]|\-{2})\s"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,2}[FE]?|[AFE]|\-{2})\s"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,3}E?|[AFE]|\-{2})\s"""+
                r"""([2]|\-{2}|[AF])\s?"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,2}|\-{2})\s"""+
                r"""(\d{1,2}\.\d{2}|\-{2}|[A])\s"""+

                r"""(\d{1,3}[FE]?|[AFE]|\-{2})\s"""+
                r"""([1]|\-{2})\s"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,2}|\-{2})\s"""+
                r"""(\d{1,2}|\-{2})\s"""+

                r"""(\d{1,3}[FE]?|[AFE]|\-{2})\s?"""+
                r"""([1]|\-{2})\s"""+
                r"""([\D]{0,2})\s"""+
                r"""(\d{1,2}|\-{2})\s"""+
                r"""(\d{1,2}|\-{2})\s"""+

                r"""(\d{1,2}\.\d{2}|\-{2}|[A])\s"""+
                r"""(\d{1,3}\.\d{2}|\-{2}|[A])\s"""+
                r"""(\d{1,2}\.\d{2}|\-{2}|[A])\s"""+
                # r""""""+

                r""
            )
        else:
            value=self.stret(
            r"""(\d{7})\s?"""+
            r"""(\/?)([A-Z\s\.\']*)\s?"""+
            r"""\((\d{0,})\)\s?"""+
            r"""(\d{1,}\:{1}[\D]*)"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            r"""(\d{0,2}\+?F?E?A?)\s+?"""+
            
            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{1,3})\s+?"""+
            r"""(\D{0,10})\s+?"""+

            
            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{0,3}\+?F?E?A?\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?)\s+?"""+
            r"""([A-FO\+\-]{1,2})\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+
            r"""(\d{0,2}\-?\-?)\s+?"""+

            r"""(\d{1,2})\s+?"""+
            r"""(\d{1,3})\s+?"""+
            r"""(\d{0,2}\.?\d{0,2}\-{0,2})\s+?"""+
            r"""([A-FO\-\+]{0,2})"""+
            r""""""
            )

        return value
    def stret(self,string):
        return string
        
    def upd_page_rng(self,no_of_pages,interval=0):
        if(interval==0):
            interval=self.interval
        self.totpg=no_of_pages
        self.var1=self.totpg%interval
        self.var2=self.totpg//interval
        self.var3=self.var1+self.var2*interval
        self.li,self.options2=[],[]
        for i in range(0,self.totpg,interval):
            self.li.append(i)
        self.li.append(self.totpg)
        print(self.li)
        for i in range(len(self.li)):
            if(i!=0):
                print(self.li[i-1],self.li[i])
                self.options2.append([self.li[i-1],self.li[i]])
        print(self.options2)
        self.textvar2.set(self.options2[0])
        self.selrng.destroy()
        self.selrng=OptionMenu(self.master,self.textvar2,*self.options2)
        self.selrng['menu'].configure(bg=bcolor,fg=fcolor)
        self.selrng.configure(bg=bcolor,fg=fcolor,width=opmnwidth)
        self.selrng.grid(row=2,column=3)

if __name__ == "__main__":
    root = Tk()
    try:
        if(getattr(sys,'frozen',False)):
           wd=sys._MEIPASS
        else:
           wd=''
        img=Image('photo',file=os.path.join(wd,'pdfreaders-f.png'))
        root.tk.call("wm","iconphoto",root._w,img)
    except:
        messagebox.showerror('no work','nah')
    
    my_gui = OMS(root)
    root.mainloop()

