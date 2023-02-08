from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    root.geometry("800x850+250+5")
    root.title("Performance Analysis On Student Feedback Using Machine Learning Algorithms")
    root.configure(background="#45458B")
    
    teaching = tk.IntVar()
    coursecontent = tk.IntVar()
    examination = tk.IntVar()
    labwork = tk.IntVar()
    library_facilities = tk.IntVar()
    extracurricular = tk.IntVar()
    coursetype = tk.IntVar()
   
    
    #===================================================================================================================
    def Detect():
       
        e1= teaching.get()
        print(e1)
        e2=coursecontent.get()
        print(e2)
        e3= examination.get()
        print(e3)
        e4=labwork.get()
        print(e4)
        e5=library_facilities.get()
        print(e5)
        e6=extracurricular.get()
        print(e6)
        e7=coursetype.get()
        print(e7)
        
        
        #########################################################################################
        
        from joblib import dump ,load
        a1=load('D:/Students Feedback 100% code/student.joblib')
        v= a1.predict([[e1,e2,e3,e4,e5,e6,e7]])
        print(v)
        if v[0]==0:
            print("Student Feedback is Good")
            yes = tk.Label(root,text="Way of Teaching is Good",background="#45458B",foreground="white",font=('times', 30, ' bold '),width=18)
            yes.place(x=200,y=500)
                     
        elif v[0]==1:
            print("Student Feedback is Bad")
            no = tk.Label(root, text="Way of Teaching is Bad", background="#45458B", foreground="white",font=('times', 30, ' bold '),width=18)
            no.place(x=200, y=500)
            
            
    
        

    l1=tk.Label(root,text="Teaching",background="#45458B",foreground="white",font=('times', 20, ' bold '),width=15)
    l1.place(x=50,y=5)
    teaching=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=teaching)
    teaching.place(x=400,y=1)

    l2=tk.Label(root,text="Course Content",background="#45458B",foreground="white",font=('times', 20, ' bold '),width=15)
    l2.place(x=50,y=50)
    coursecontent=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=coursecontent)
    coursecontent.place(x=400,y=50)

    l3=tk.Label(root,text="Examination",background="#45458B",foreground="white",font=('times', 20, ' bold '),width=15)
    l3.place(x=50,y=100)
    examination=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=examination)
    examination.place(x=400,y=100)
    
    l4=tk.Label(root,text="Labwork",background="#45458B",foreground="white",font=('times', 20, ' bold '),width=15)
    l4.place(x=50,y=150)
    labwork=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=labwork)
    labwork.place(x=400,y=160)
    
    l5=tk.Label(root,text="Library Facilities",background="#45458B",foreground="white",font=('times', 20, ' bold '),width=15)
    l5.place(x=50,y=200)
    library_facilities=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=library_facilities)
    library_facilities.place(x=400,y=200)
    
    l6=tk.Label(root,text="Extracurricular",background="#45458B",foreground="white",font=('times', 20, ' bold '),width=15)
    l6.place(x=50,y=250)
    extracurricular=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=extracurricular)
    extracurricular.place(x=400,y=250)  
    
    l7=tk.Label(root,text="Coursetype",background="#45458B",foreground="white",font=('times', 20, ' bold '),width=15)
    l7.place(x=50,y=250)
    coursetype=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=coursetype)
    coursetype.place(x=400,y=250)

    

    
    
    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=300,y=400)


    root.mainloop()

Train()