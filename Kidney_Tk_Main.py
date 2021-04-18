import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import Image,ImageTk
import PIL as p
from Kidney_Patient_Doc import Patient
import pickle
import pathlib
import os
from graph import *
from toptradingcycle import *
import copy as cp
from collections import deque
from queue import Queue


font1=("Verdana", 16)


priorQ=deque(())


pref_list_global=[]
flag=[]
flag2=[]


class Window(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.title(self, "KIDNEY-DONOR MATCHING")
        tk.Tk.geometry(self,"1360x720")
        minh = 800
        minw = 600
        tk.Tk.minsize(self,minh,minw)
        path = "/home/ubuntu/Desktop/Codes/Python/kidney_transplant.jpg"
        pic=p.Image.open(path)
        img = ImageTk.PhotoImage(pic)

        container = tk.Frame(self)

        container.pack(side="top",fill = "both", expand = True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)
        #container.configure(self,background='blue')

        self.frames = {}

        for f in (StartPage, PageOne,Reg_Page,PageTwo,PageThree,Admin_Reg,Admin_Log,PageFour,Match_Check):
            frame = f(container,self)
            self.frames[f] = frame
            frame.grid(row=0, column = 0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

    

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='slateblue')
        label = tk.Label(self,text = """SELECT THE TYPE OF USER""",font=font1,bg='slateblue',fg='yellow')
        label.place(x=530,y=1)
        butt1 = ttk.Button(self, text = "PATIENT",command = lambda: controller.show_frame(PageOne))
        butt1.place(x=200,y=100)
        butt2 = ttk.Button(self, text = "DOCTOR/ADMIN",command = lambda: controller.show_frame(Admin_Log))
        butt2.place(x=600,y=100)
        butt3 = ttk.Button(self, text="Exit", command=self.quit)
        butt3.place(x=1050,y=100)
        path = "KidneyMainPage.png"
        canvas = tk.Canvas(self,width=500,height=300)
        canvas.place(x=450,y=200)
        pic=p.Image.open(path)
        #img = ImageTk.PhotoImage(pic)
        img = ImageTk.PhotoImage(Image.open(path).resize((500, 300), Image.ANTIALIAS))
        canvas.background = img  # Keep a reference in case this code is put in a function.
        bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)
        

pat_log=Patient()


class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        global pat_log
        #pat=Patient()
        # newframe1 = tk.Frame(self)
        # newframe1.pack(fill=both,expand=False)
        label=tk.Label(self,text="""WELCOME TO PATIENT LOGIN PAGE""",font=("Times",20),fg='blue')
        label.place(x=500,y=1)
        label2=tk.Label(self,text="""Enter Login Credentials""",font=("Times",16))
        label2.place(x=1,y=40)

        label3=tk.Label(self,text="""Enter Id """,font=("Times",16))
        label3.place(x=1,y=80)
        user_id = tk.Entry(self,width = 20,borderwidth = 5,font=("Times", 16),bg='slateblue',fg='white')
        user_id.place(x=150,y=80)
        label4=tk.Label(self,text="""Enter Password """,font=("Times",16))
        label4.place(x=1,y=120)
        password = tk.Entry(self,show='*',width = 20,borderwidth = 5,font=("Times", 16),bg='slateblue',fg='white')
        password.place(x=150,y=120)
        butt1=ttk.Button(self,text="REGISTER",command = lambda: controller.show_frame(Reg_Page))
        butt1.place(x=10,y=160)
        butt2=ttk.Button(self,text="BACK",command = lambda: controller.show_frame(StartPage))
        butt2.place(x=100,y=160)
        butt3=ttk.Button(self,text="CONTINUE",command = lambda: self.pass_check(user_id.get(),password.get(),controller))
        butt3.place(x=190,y=160)
        path = "kidney_transplant.jpg"
        canvas = tk.Canvas(self,width=500,height=500)
        canvas.place(x=650,y=100)
        pic=p.Image.open(path)
        #img = ImageTk.PhotoImage(pic)
        img = ImageTk.PhotoImage(Image.open(path).resize((500, 500), Image.ANTIALIAS))
        canvas.background = img  # Keep a reference in case this code is put in a function.
        bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

        
    def pass_check(self,uid,pas,control):
        global pat_log
        
        check=False
        mylist= pickleLoader('text.pkl')
        for pat in mylist:
            if(pat.check_pass(uid,pas)):
                    #mb.showerror("Congrats!","Successful Login!")
                    check=True
                    pat_log=cp.deepcopy(pat)
                    control.show_frame(PageTwo)
        
        if(check==False):
            mb.showerror("ERROR!!","Incorrect User Name or Password!")
        
        
def pickleLoader(pklFile):
    file = pathlib.Path(pklFile)
    if file.exists ():
        infile = open(pklFile,'rb')
        mylist = pickle.load(infile)
        infile.close()
        return mylist
    else:
        mb.showerror('FAILED','NO RECORDS FOUND!')


class Admin_Log(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        global pat_log
        #pat=Patient()
        # newframe1 = tk.Frame(self)
        # newframe1.pack(fill=both,expand=False)
        label=tk.Label(self,text="""WELCOME TO ADMIN LOGIN PAGE""",font=("Times",20),fg='blue')
        label.place(x=500,y=1)
        label2=tk.Label(self,text="""Enter Login Credentials""",font=("Times",16))
        label2.place(x=1,y=40)

        label3=tk.Label(self,text="""Enter Id """,font=("Times",16))
        label3.place(x=1,y=80)
        user_id = tk.Entry(self,width = 20,borderwidth = 5,font=("Times", 16),bg='slateblue',fg='white')
        user_id.place(x=150,y=80)
        label4=tk.Label(self,text="""Enter Password """,font=("Times",16))
        label4.place(x=1,y=120)
        password = tk.Entry(self,show='*',width = 20,borderwidth = 5,font=("Times", 16),bg='slateblue',fg='white')
        password.place(x=150,y=120)
        butt1=ttk.Button(self,text="REGISTER",command = lambda: controller.show_frame(Admin_Reg))
        butt1.place(x=10,y=160)
        butt2=ttk.Button(self,text="BACK",command = lambda: controller.show_frame(StartPage))
        butt2.place(x=100,y=160)
        butt3=ttk.Button(self,text="CONTINUE",command = lambda: self.pass_check(user_id.get(),password.get(),controller))
        butt3.place(x=190,y=160)
        path = "kidney_transplant.jpg"
        canvas = tk.Canvas(self,width=500,height=500)
        canvas.place(x=650,y=100)
        pic=p.Image.open(path)
        #img = ImageTk.PhotoImage(pic)
        img = ImageTk.PhotoImage(Image.open(path).resize((500, 500), Image.ANTIALIAS))
        canvas.background = img  # Keep a reference in case this code is put in a function.
        bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

        
    def pass_check(self,uid,pas,control):
        global pat_log
        
        check=False
        mylist= pickleLoader('admin.pkl')
        for pat in mylist:
            if(pat.check_pass(uid,pas)):
                    #mb.showerror("Congrats!","Successful Login!")
                    check=True
                    pat_log=cp.deepcopy(pat)
                    control.show_frame(PageFour)
        
        if(check==False):
            mb.showerror("ERROR!!","Incorrect User Name or Password!")


class Admin_Reg(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        label=tk.Label(self,text="""WELCOME TO ADMIN REGIS. PAGE""",font=("Times",20),fg='blue')
        label.place(x=500,y=1)
        label2=tk.Label(self,text="""Fill The Registration Details...""",font=("Times",16))
        label2.place(x=1,y=40)

        label3=tk.Label(self,text="""Enter Id """,font=("Times",16))
        label3.place(x=1,y=80)
        user_id = tk.Entry(self,width = 20,borderwidth = 5,font=("Times", 16))
        user_id.place(x=175,y=80)
        label4=tk.Label(self,text="""Enter Password """,font=("Times",16))
        label4.place(x=1,y=120)
        password = tk.Entry(self,show='*',width = 20,borderwidth = 5,font=("Times", 16))
        password.place(x=175,y=120)
        label5=tk.Label(self,text="""Confirm Password """,font=("Times",16))
        label5.place(x=1,y=160)
        conf_password = tk.Entry(self,show='*',width = 20,borderwidth = 5,font=("Times", 16))
        conf_password.place(x=175,y=160)
        butt1=ttk.Button(self,text="CONTINUE",command = lambda: self.cont(password.get(),conf_password.get(),user_id.get(),controller))
        butt1.place(x=50,y=200)
        butt2=ttk.Button(self,text="BACK",command = lambda: controller.show_frame(Admin_Log))
        butt2.place(x=150,y=200)


    def cont(self,pas,conf,uid,controller):
        pat=Patient()
        if(pas==conf):
        
            pat.getdata(uid,pas)
            file = pathlib.Path("admin.pkl")
            if file.exists ():
                infile = open('admin.pkl','rb')
                oldlist = pickle.load(infile)
                oldlist.append(pat)
                infile.close()
                os.remove('admin.pkl')
            else :
                oldlist = [pat]
            outfile = open('newadmin.pkl','wb')
            pickle.dump(oldlist, outfile)
            outfile.close()
            os.rename('newadmin.pkl', 'admin.pkl')
            
            
            mb.showerror("Congrats!","Successfully Registered!")
            

        else:
            mb.showerror("ERROR!!","Password Did Not Match!")

    
class Reg_Page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        label=tk.Label(self,text="""WELCOME TO PATIENT REGIS. PAGE""",font=("Times",20),fg='blue')
        label.place(x=500,y=1)
        label2=tk.Label(self,text="""Fill The Registration Details...""",font=("Times",16))
        label2.place(x=1,y=40)

        label3=tk.Label(self,text="""Enter Id """,font=("Times",16))
        label3.place(x=1,y=80)
        user_id = tk.Entry(self,width = 20,borderwidth = 5,font=("Times", 16))
        user_id.place(x=175,y=80)
        label4=tk.Label(self,text="""Enter Password """,font=("Times",16))
        label4.place(x=1,y=120)
        password = tk.Entry(self,show='*',width = 20,borderwidth = 5,font=("Times", 16))
        password.place(x=175,y=120)
        label5=tk.Label(self,text="""Confirm Password """,font=("Times",16))
        label5.place(x=1,y=160)
        conf_password = tk.Entry(self,show='*',width = 20,borderwidth = 5,font=("Times", 16))
        conf_password.place(x=175,y=160)
        butt1=ttk.Button(self,text="CONTINUE",command = lambda: self.cont(password.get(),conf_password.get(),user_id.get(),controller))
        butt1.place(x=50,y=200)
        butt2=ttk.Button(self,text="BACK",command = lambda: controller.show_frame(PageOne))
        butt2.place(x=150,y=200)

        # if(password==conf_password):
        #     pat.getdata(user_id,password)
        #     with open('text.pkl','wb') as output:
        #         pickle.dump(pat,output,pickle.HIGHEST_PROTOCOL)

    def cont(self,pas,conf,uid,controller):
        pat=Patient()
        if(pas==conf):
        #     pat.getdata(uid,pas)
        #     with open('text.pkl','wb') as output:
        #         pickle.dump(pat,output,pickle.HIGHEST_PROTOCOL)
        #     mb.showerror("Congrats!","Successfully Registered!")
            

        # else:
        #     mb.showerror("ERROR!!","Password Did Not Match!")
            pat.getdata(uid,pas)
            file = pathlib.Path("text.pkl")
            if file.exists ():
                infile = open('text.pkl','rb')
                oldlist = pickle.load(infile)
                oldlist.append(pat)
                infile.close()
                os.remove('text.pkl')
            else :
                oldlist = [pat]
            outfile = open('newtext.pkl','wb')
            pickle.dump(oldlist, outfile)
            outfile.close()
            os.rename('newtext.pkl', 'text.pkl')
            
            
            mb.showerror("Congrats!","Successfully Registered!")
            

        else:
            mb.showerror("ERROR!!","Password Did Not Match!")


class PageTwo(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='slateblue')

        global pat_log

        label=tk.Label(self,text="""WELCOME TO PATIENT PORTAL""",font=("Times",20),fg='yellow',bg='slateblue')
        label.place(x=500,y=1)

        label1=tk.Label(self,text="""Enter Patient User ID """,font=("Times",16))
        label1.place(x=450,y=80)
        pat_uid = tk.Entry(self,width = 20,borderwidth = 5,font=("Times", 16))
        pat_uid.place(x=750,y=80)
        label2=tk.Label(self,text="""Enter Password """,font=("Times",16))
        label2.place(x=450,y=120)
        pat_pass = tk.Entry(self,show='*',width = 20,borderwidth = 5,font=("Times", 16))
        pat_pass.place(x=750,y=120)
        
        label3=tk.Label(self,text="""Enter Patient Name """,font=("Times",16))
        label3.place(x=450,y=160)
        pat_name = tk.Entry(self,width = 20,borderwidth = 5,font=("Times", 16))
        pat_name.place(x=750,y=160)
        label4=tk.Label(self,text="""Enter Donor Name """,font=("Times",16))
        label4.place(x=450,y=200)
        don_name = tk.Entry(self,width = 20,borderwidth = 5,font=("Times", 16))
        don_name.place(x=750,y=200)
        label5=tk.Label(self,text="""Enter Donor Blood Type """,font=("Times",16))
        label5.place(x=450,y=240)
        bloodgrp = tk.Entry(self,width = 20,borderwidth = 5,font=("Times", 16))
        bloodgrp.place(x=750,y=240)
        butt1=ttk.Button(self,text="SUBMIT",command = lambda: self.submit(pat_name.get(),don_name.get(),bloodgrp.get()))
        butt1.place(x=550,y=400)
        butt2=ttk.Button(self,text="Log Out",command = lambda: controller.show_frame(PageOne))
        butt2.place(x=650,y=400)
        butt3=ttk.Button(self,text="Enter Preference List",command = lambda: controller.show_frame(PageThree))
        butt3.place(x=750,y=400)
        butt4=ttk.Button(self,text="Check Match",command = lambda: controller.show_frame(Match_Check))
        butt4.place(x=655,y=450)

    def submit(self,pat_name,don_name,blood):

        global pat_log
        check=False
        

        file = pathlib.Path("text.pkl")
        if file.exists ():
            infile = open('text.pkl','rb')
            mylist = pickle.load(infile)
            infile.close()
            os.remove('text.pkl')
            for item in mylist :
                if item.user_id == pat_log.user_id :
                    item.getnames(pat_name,don_name,blood)
                    mb.showerror('DONE','PREFERENCES SUBMITTED!')

            outfile = open('newtext.pkl','wb')
            pickle.dump(mylist, outfile)
            outfile.close()
            os.rename('newtext.pkl', 'text.pkl')
            
        else:
            mb.showerror('FAILED','FILE NOT FOUND!')
                    
        



class PageThree(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='slateblue')


        label=tk.Label(self,text="""PREFERENCE FILLING PORTAL""",font=("Times",20),fg='yellow',bg='slateblue')
        label.pack(side='top',padx=2,pady=2)

        
        label5=tk.Label(self,text="""Enter Preferences""",font=("Times",16))
        label5.pack(side='top',padx=2,pady=2)
        pref_list_local = tk.Entry(self,width = 20,borderwidth = 5,font=("Times", 16))
        pref_list_local.pack(side='top',padx=2,pady=2)

        butt3=ttk.Button(self,text="Check List",command = lambda: self.check_list())
        butt3.pack(side='top',padx=2,pady=2)

        butt1=ttk.Button(self,text="SUBMIT",command = lambda: self.submit(pref_list_local.get()))
        butt1.pack(side='top',padx=2,pady=2)

        butt2=ttk.Button(self,text="BACK",command = lambda: controller.show_frame(PageTwo))
        butt2.pack(side='top',padx=2,pady=2)
        

    def check_list(self):
        global flag
        prefFrame = tk.Frame(self, height=650, width=500, bg="white", border=5, relief="sunken")
        prefFrame.pack(side='top',padx=2,pady=2)
        msg=''
        if len(flag) == 0:
            msg='List To Choose From Has Not Been Generated Yet!'+str(111)
        else:
            file = pathlib.Path("text.pkl")
            if file.exists ():
                mylist= pickleLoader('text.pkl')
                for pat in mylist:
                    msg+=pat.don_name+' '+pat.don_blood+'\n'
            else :
                msg='List To Choose From Has Not Been Generated Yet!'+' 0 '

        label3=tk.Label(prefFrame,text=msg,font=("Times",14),fg='brown')
        label3.pack(side='top')

    def submit(self,pref_list_loc):

        global pat_log
        global priorQ
        check=False
        


        file = pathlib.Path("text.pkl")
        if file.exists ():
            infile = open('text.pkl','rb')
            mylist = pickle.load(infile)
            infile.close()
            os.remove('text.pkl')
            for item in mylist :
                if item.user_id == pat_log.user_id :
                    item.get_pref(pref_list_loc)
                    mb.showerror('DONE','PREFERENCES SUBMITTED!')

            outfile = open('newtext.pkl','wb')
            pickle.dump(mylist, outfile)
            outfile.close()
            os.rename('newtext.pkl', 'text.pkl')


            file2 = pathlib.Path("prefQ.pkl")
            if file2.exists ():
                infile2 = open('prefQ.pkl','rb')
                myqueue = pickle.load(infile2)
                infile2.close()
                os.remove('prefQ.pkl')

                pat_log.get_pref(pref_list_loc)
                myqueue.append(pat_log)
                outfile2 = open('newprefQ.pkl','wb')
                pickle.dump(myqueue, outfile2)
                outfile2.close()
                os.rename('newprefQ.pkl', 'prefQ.pkl')

            else:
                pat_log.get_pref(pref_list_loc)
                priorQ.append(pat_log)
                outfile2 = open('newprefQ.pkl','wb')
                pickle.dump(priorQ, outfile2)
                outfile2.close()
                os.rename('newprefQ.pkl', 'prefQ.pkl')
            
        else:
            mb.showerror('FAILED','FILE NOT FOUND!')


class Match_Check(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='slateblue')


        label=tk.Label(self,text="""CHECK YOUR DONOR MATCH""",font=("Times",20),fg='yellow',bg='slateblue')
        label.pack(side='top',padx=2,pady=2)

        

        butt3=ttk.Button(self,text="Check Result",command = lambda: self.check_list())
        butt3.pack(side='top',padx=20,pady=20)

        # butt1=ttk.Button(self,text="SUBMIT",command = lambda: self.submit(pref_list_local.get()))
        # butt1.pack(side='top',padx=20,pady=20)

        butt2=ttk.Button(self,text="BACK",command = lambda: controller.show_frame(PageTwo))
        butt2.pack(side='top',padx=20,pady=20)
        

    def check_list(self):
        global flag2
        global matching
        global mapping
        global finalmatch
        global pat_log
        prefFrame = tk.Frame(self, height=650, width=500, bg="white", border=5, relief="sunken")
        prefFrame.pack(side='top',padx=20,pady=20)
        msg=''
        if len(flag2) == 0:
            msg='Matching Has Not Been Generated Yet!'
        else:
            file = pathlib.Path("match.pkl")
            if file.exists ():
                num=finalmatch[pat_log.name]
                for key,val in mapping.items():
                    if int(val)==num:
                        msg='Congrats!'+'\n'+'You Have Been Matched With '+str(key)+' For Kidney Transplant!!'
            else :
                msg='Matching Has Not Been Generated Yet!'+' 0 '

        label3=tk.Label(prefFrame,text=msg,font=("Times",18),fg='brown')
        label3.pack(side='top')



initDon={}
pats=set()
dons=set()
preferences={}
matching={}
initDon2={}
mapping={}
finalmatch={}

class PageFour(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='lightgreen')
        global flag
        label=tk.Label(self,text="""WELCOME TO ADMIN PORTAL""",font=("Times",20),fg='purple',bg='yellow')
        label.pack(side='top')

        butt1=ttk.Button(self,text="GENERATE PREFERENCE OPTIONS",command = lambda: self.gen_opts())
        butt1.pack(side='top',padx=20,pady=20)
        butt3=ttk.Button(self,text="CHECK PREFERENCE LISTS",command = lambda: controller.show_frame(Admin_Log))
        butt3.pack(side='top',padx=20,pady=20)
        butt4=ttk.Button(self,text="GENERATE MATCHING",command = lambda: self.gen_match())
        butt4.pack(side='top',padx=20,pady=20)
        butt2=ttk.Button(self,text="BACK",command = lambda: controller.show_frame(Admin_Log))
        butt2.pack(side='top',padx=20,pady=20)

    def gen_opts(self):

        global flag
        file2 = pathlib.Path("prefQ.pkl")
        file3 = pathlib.Path('text.pkl')
        q=deque()
        list1=[]
        if file2.exists():
            q=pickleLoader('prefQ.pkl')
            list1=pickleLoader('text.pkl')
        if(len(q)!=len(list1)):
            mb.showerror('FAILED','NOT ALL PREFERENCES RECEIVED')

        else:
            flag.append(1)
            mb.showerror('DONE','Preference List Options Have Been Generated')

    def gen_match(self):
        global pats
        global initDon
        global dons
        global preferences
        global matching
        global initDon2
        global mapping
        prefs=[]
        i=0
        newqueue=deque()
        item=Patient()
        file2 = pathlib.Path("prefQ.pkl")
        if file2.exists ():
            infile2 = open('prefQ.pkl','rb')
            myqueue = pickle.load(infile2)
            newqueue=cp.deepcopy(myqueue)
            infile2.close()
            # os.remove('prefQ.pkl')
            while myqueue:
                item=myqueue.popleft()
                pats.add(item.name)
                #dons.add(item.don_name)
                initDon[item.don_name]=item.name
                
            for obj in initDon.keys():
                mapping[str(obj)]=i+1
                i+=1
                
            # prefs.append(i+1)
            # preferences[item.name]=
            
            while newqueue:
                itemnew=newqueue.popleft()
                for j in range(len(itemnew.pref_list)):
                    prefs.append(mapping[itemnew.pref_list[j]])
                
                initDon2[mapping[itemnew.don_name]]=itemnew.name
                dons.add(int(mapping[itemnew.don_name]))

                preferences[itemnew.name]=list(prefs)
                print(prefs)
                prefs.clear()


            matching=topTradingCycles(pats,dons,preferences,initDon2)
            mb.showerror('SUCCESS','KIDNEY DONOR PAIRS MATCHED')
            putmatches(matching)
            flag2.append(1)
            # myqueue.append(pat_log)
            # outfile2 = open('newprefQ.pkl','wb')
            # pickle.dump(myqueue, outfile2)
            # outfile2.close()
            # os.rename('newprefQ.pkl', 'prefQ.pkl')

def putmatches(match):
    
    global finalmatch
    file = pathlib.Path("match.pkl")
    if file.exists ():
        infile = open('match.pkl','rb')
        finalmatch = pickle.load(infile)
        infile.close()
        os.remove('match.pkl')
    else :
        finalmatch = dict(matching)
    outfile = open('newmatch.pkl','wb')
    pickle.dump(finalmatch, outfile)
    outfile.close()
    os.rename('newmatch.pkl', 'match.pkl')

                


                


        






if __name__ == '__main__':
    app=Window()
    app.mainloop()