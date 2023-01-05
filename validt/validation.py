from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import re
import mysql.connector
import pyttsx3



class Resister():
    def __init__(self,root):
        self.root=root
        self.root.title('Resister page')
        self.root.geometry('1600x790+0+0')

        #text-to space
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)


        

        #variable
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.contact_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.country_var=StringVar()
        self.id_var=StringVar()
        self.id_no_var=StringVar()
        self.password=StringVar()
        self.confirm_password=StringVar()
        self.check_var=IntVar()


        #images
        self.bg=ImageTk.PhotoImage(file='back.jpg')
        bg_lbl=Label(self.root,image=self.bg,bd=2,relief=RAISED)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #logo image
        logo_img=Image.open('logo.png')
        logo_img=logo_img.resize((45,45),Image.ANTIALIAS)#resize the image high label to low lable
        self.photo_logo=ImageTk.PhotoImage(logo_img)

        #Tittel frame
        tittle_frame=Frame(self.root,bd=1,relief=RAISED)
        tittle_frame.place(x=590,y=8,width=500,height=60)

        title_lbl=Label(tittle_frame,image=self.photo_logo,compound=LEFT,text='USER  RESISTERATION  FORM',font=('times new roman',15,'bold'),fg='darkblue')
        title_lbl.place(x=10,y=10)



        #information
        main_frame=Frame(self.root,bd=1,relief=RAISED)
        main_frame.place(x=590,y=70,width=500,height=580)


        #username
        user_name=Label(main_frame,text='Username :',font=('times new roman',16,'bold'))
        user_name.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        #userenteryfill
        user_entry=ttk.Entry(main_frame,textvariable=self.name_var,font=('times new roman',15,'bold'),width=25)
        user_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        #bind validation register
        validate_name=self.root.register(self.checkname)
        user_entry.config(validate='key',validatecommand=(validate_name,'%P'))



        #Email
        email_name=Label(main_frame,text='Email ID :',font=('times new roman',16,'bold'))
        email_name.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        #Emailenteryfill
        email_entry=ttk.Entry(main_frame,textvariable=self.email_var,font=('times new roman',15,'bold'),width=25)
        email_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)



        #contect
        contact_name=Label(main_frame,text='Contact :',font=('times new roman',16,'bold'))
        contact_name.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        #contectenteryfill
        entry_contact=ttk.Entry(main_frame,textvariable=self.contact_var,font=('times new roman',15,'bold'),width=25)
        entry_contact.grid(row=2,column=1,padx=10,pady=10,sticky=W)


        #bind validation register
        validate_contact=self.root.register(self.checkcontact)
        entry_contact.config(validate='key',validatecommand=(validate_contact,'%P'))


        #Gender
        gender_name=Label(main_frame,text='Select Gender :',font=('times new roman',16,'bold'))
        gender_name.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        
        #redio button 
        '''redio button is selection of any one variable '''
        gender_frame=Frame(main_frame)
        gender_frame.place(x=205,y=160,width=280,height=35)
        #male
        redio_male=Radiobutton(gender_frame,variable=self.gender_var,value='Male',text='Male',font=('times new roman',13,'bold'))
        redio_male.grid(row=0,column=0,padx=10,pady=0,sticky=W)
        self.gender_var.set('Male')
        #female
        redio_female=Radiobutton(gender_frame,variable=self.gender_var,value='Female',text='Female',font=('times new roman',13,'bold'))
        redio_female.grid(row=0,column=1,padx=10,pady=0,sticky=W)


        #country
        country_name=Label(main_frame,text='Select Country :',font=('times new roman',16,'bold'))
        country_name.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        list=['India','UK','USA','Nepal','Afganistan','Pakistan']
        droplist=OptionMenu(main_frame,self.country_var,*list)
        droplist.config(width=21,font=('times new roman',15),bg='white')
        self.country_var.set('Select your country')
        droplist.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        #ID_TYPE
        id_type=Label(main_frame,text='Select Id Type :',font=('times new roman',16,'bold'))
        id_type.grid(row=5,column=0,padx=10,pady=10,sticky=W)

        self.combo_id_type=ttk.Combobox(main_frame,textvariable=self.id_var,font=('times new riman ',15,),justify='center',state="readonly",width=23)
        self.combo_id_type["values"]=("Select Your Id",'Adhar Card','Pasport','Driving licence')
        self.combo_id_type.grid(row=5,column=1,padx=10,pady=10)
        self.combo_id_type.current(0)
        
        



        #ID_Number
        Id_Number=Label(main_frame,text='ID Number :',font=('times new roman',16,'bold'))
        Id_Number.grid(row=6,column=0,padx=10,pady=10,sticky=W)
        #contectenteryfill
        Id_Number_entry=ttk.Entry(main_frame,textvariable=self.id_no_var,font=('times new roman',15,'bold'),width=25)
        Id_Number_entry.grid(row=6,column=1,padx=10,pady=10,sticky=W)


        #Password
        Password_name=Label(main_frame,text='Password :',font=('times new roman',16,'bold'))
        Password_name.grid(row=7,column=0,padx=10,pady=10,sticky=W)
        #contectenteryfill
        Password_entry=ttk.Entry(main_frame,textvariable=self.password,font=('times new roman',15,'bold'),width=25)
        Password_entry.grid(row=7,column=1,padx=10,pady=10,sticky=W)

        #confirm Password
        RePassword_name=Label(main_frame,text='Confirm Password :',font=('times new roman',16,'bold'))
        RePassword_name.grid(row=8,column=0,padx=10,pady=10,sticky=W)
        #contectenteryfill
        RePassword_entry=ttk.Entry(main_frame,textvariable=self.confirm_password,font=('times new roman',15,'bold'),width=25)
        RePassword_entry.grid(row=8,column=1,padx=10,pady=10,sticky=W)


        #check frame
        check_frame=Frame(main_frame)
        check_frame.place(x=130,y=445,width=400,height=70)

        check_btn=Checkbutton(check_frame,variable=self.check_var,text='Agree our term & condition',font=('times new roman',16),onvalue=1,offvalue=0)
        check_btn.grid(row=0,column=0,padx=10,sticky=W)
        self.check_lbl=Label(check_frame,text='',font=("arial",16),fg='red')
        self.check_lbl.grid(row=1,column=0,padx=10,sticky=W)


        #Button Frame
        btn_frame=Frame(main_frame)
        btn_frame.place(x=30,y=478,width=480,height=70)

        save_data=Button(btn_frame,text='Save',command=self.validation,font=('times new roman',16,'bold'),width=12,cursor='hand2',bg='blue',fg='white')
        save_data.grid(row=0,column=0,padx=1,sticky=W)

        varify_data=Button(btn_frame,command=self.verify_data,text='Varify',font=('times new roman',16,'bold'),width=12,cursor='hand2',bg='blue',fg='white')
        varify_data.grid(row=0,column=1,padx=1,sticky=W)

        clear_data=Button(btn_frame,command=self.clear_data,text='Clear',font=('times new roman',16,'bold'),width=12,cursor='hand2',bg='blue',fg='white')
        clear_data.grid(row=0,column=2,padx=1,sticky=W)
        

    # call back function
    def checkname(self,name):
        if name.isalnum():
            return True
        if name=='':
            return True
        else :
            messagebox.showerror('Invalid','Not Allowed'+name[-1])
            return False

    #chack contect

    def checkcontact(self,contact):
        if contact.isalnum():
            return True
        if len(str(contact))==0:
            return True
        else :
            messagebox.showerror('Invalid','Invalid Entry'+name[-1])
            return False
# Call back function
    # passaword validation
    def checkpassword(self,password):
        if len(password)<=21 :
            if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-zA-Z0-9]))",password):
                return True
            else :
                messagebox.showinfo('invalid','Enter Valid Password(Example : Name@123')
                return False
        else :
                messagebox.showerror('invalid','Length try to exceed')
                return False




    #validation of Email
    def checkemail(self,email):
        if len(email)>7 :
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                return True
            else :
                messagebox.showwarning('Alert','invalid email Enter Valid user email (Example : Name@gmail.com')
                return False
        else :
                messagebox.showinfo('invalid','Email Length is too small')
                return False


# validations
    def validation(self):
            x=y=0
            if self.name_var.get()=='':
                self.engine.say('Please Enter your Name')
                self.engine.runAndWait()
                messagebox.showerror('Error','please Enter your name ',parent=self.root)

            elif self.email_var.get()=='':
                self.engine.say('Please Enter your Email id')
                self.engine.runAndWait()
                messagebox.showerror('Error','please Enter your Email id ',parent=self.root)

            elif self.contact_var.get()=='' or len(self.contact_var.get())!=10:
                self.engine.say('Please Enter Valid contact must be 10 digite')
                self.engine.runAndWait()
                messagebox.showerror('Error','please Enter your contact ',parent=self.root)

            elif self.gender_var.get()=='':
                self.engine.say('Please select your Gender')
                self.engine.runAndWait()
                messagebox.showerror('Error','please Enter your Gender ',parent=self.root)

            elif self.country_var.get()=='' or self.country_var.get()=='Select your country':
                messagebox.showerror('Error','please Enter your country ',parent=self.root)

            elif self.id_var.get()=='please select your id':
                self.engine.say('Please select id type')
                self.engine.runAndWait()
                messagebox.showerror('Error','please select your id ',parent=self.root)

            elif self.id_no_var.get()=='':
                self.engine.say('Please Enter your id number')
                self.engine.runAndWait()
                messagebox.showerror('Error','please Enter your id_no ',parent=self.root)
            elif len(self.id_no_var.get())!=12:
                self.engine.say('Please Enter 12 digit your id number')
                self.engine.runAndWait()
                messagebox.showerror('Error','please Enter your 12 digit',parent=self.root)

            elif self.password.get()=='':
                self.engine.say('Please Enter your Password')
                self.engine.runAndWait()
                messagebox.showerror('Error','please Enter your Password ',parent=self.root)

            elif self.confirm_password.get()=='':
                self.engine.say('Please Enter your confirm password')
                self.engine.runAndWait()
                messagebox.showerror('Error','please Enter your confirm_password ',parent=self.root)

            elif self.password.get()!=self.confirm_password.get():
                self.engine.say('Password &confirm password must be same')
                self.engine.runAndWait()
                messagebox.showerror('Error','Password &confirm password must be same',parent=self.root)
    

            elif self.email_var.get()!=None and self.password.get()!=None:
                x=self.checkemail(self.email_var.get())
                y=self.checkpassword(self.password.get())
           

            if (x==True) and (y== True):
               
                self.engine.runAndWait()
                if self.check_var.get()==0:
                    self.engine.say('Please Agree our term & condition')
                    self.check_lbl.config(text='Please Agree our term & condition',fg='red')
                else:
                    self.check_lbl.config(text='checked',fg='green')   


                    try:
                        conn=mysql.connector.connect(host='localhost',username='root',password='root',database='validat' )
                        my_cursur=conn.cursor()
                        my_cursur.execute('insert into user values(%s,%s,%s,%s,%s,%s,%s,%s)',(

                                                                                                 self.name_var.get(),
                                                                                                 self.email_var.get(),
                                                                                                 self.contact_var.get(),
                                                                                                 self.gender_var.get(),
                                                                                                 self.country_var.get(),
                                                                                                 self.id_var.get(),
                                                                                                 self.id_no_var.get(),
                                                                                                 self.password.get(),           

                                                                                                ))

                        conn.commit()
                        conn.close()                  
                                             
                        messagebox.showinfo('Successfully',f'your resistration Successfully completed your username: {self.name_var.get()} and Password:{self.password.get()}' )
               
                    except Exception as es:
                        messagebox.showerror('Error',f'Due to : {str(es)}',parent=self.root)          
    def verify_data(self):
        data=f'Name:{self.name_var.get()}\nEmail:{self.email_var.get()}\nContact:{self.contact_var.get()}\nGender:{self.gender_var.get()}\nCountry:{self.country_var.get()}\nid:{self.id_var.get()}\nId Number:{self.id_no_var.get()}\nPassword:{self.password.get()}'
        messagebox.showinfo('Details',data)

    def clear_data(self):
        #variable
        self.name_var.set('')
        self.email_var.set('')
        self.contact_var.set('')
        self.gender_var.set('Male')
        self.contact_var.set('')
        self.country_var.set('Select your country')
        self.id_var.set('Select your id')
        self.id_no_var.set('')
        self.password.set('')
        self.confirm_password.set('')
        self.check_var.set(0)       


if __name__=='__main__':
    root=Tk()
    obj=Resister(root)
    root.mainloop()  
