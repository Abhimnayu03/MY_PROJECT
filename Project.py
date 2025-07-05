#Starting to customize the real project
import threading

import customtkinter as ctk #GUI ka kaam karne ke liye
from tkinter import *  #GUI ka kaam karne ke liye
import tkinter.messagebox   #GUI KA KAAM karne ke liye
from chatterbot import ChatBot  #chatbot model banane ke liye
from chatterbot.trainers import ListTrainer  #data train karne ke liye
from PIL import Image,ImageTk  #images ipport karne ke liye
import tkinter.messagebox as msg  #messagebox popup ke liye
import pandas as pd  # dataset import karne ke liye
import re




Abhi=ChatBot('My Pro')
# Abhi.storage.drop()  #here we have to remeber that we have to give the varibale name in which chatbot is assigned
c=pd.read_csv('general_knowledge_qa.csv')
# d=pd.read_csv('general_knowledge_10000.csv')
e=pd.read_csv('roman_hindi_gk_qa_500.csv')          #IMPORTING DATASETS
f=pd.read_csv('world_general_knowledge_dataset_120.csv')
g=pd.read_csv('world_general_knowledge_dataset_sample.csv')
'''this is the HANDWRITTEN dataset'''
dataset=[
    'What is your name?',
    'My name is Techie',
    'Who built you?',
    'Students of IIT patna built me,from group 138(for capstone project)',
    'What was the purpose to built you?',
    'To understand the working of AI and ML',
    'tujhe hindi aati hai?',
    'haa!! Bilkul',
    'Tab to tujhe enfglish bhi aati hogi?',
    'Ofcourse!!',
    'Accha mujh ye bata ki kya tere pass data hai theek thaak?',
    'Ha bhai, ek theek thaak amount mein hai',
    'Tum kis type ke chatbot ho',
    'mai ek formal conversation ke liye banaya hua Chatbot hu, but mere pass kucch knowledge based info bhi hai',
    'Accha tumhe mera namm pata hai',
    'Abhi mai ek kaafi basic bot hu..to aone users ka naam nhi bata skta',
    'Accha to tum ye to bata sakte ho ki tumhe banaya kisne hai',
    'tu backend ke baarein mein pucch rha hai ya frontend',
    'backend ka bata do',
    'Abhimanyu aur Aman ne',
    'Aur frontend',
    'Amrendra Aur Adesh ne',
    'Hii',
    'Hlo, waise mujhe hindi bhi aati hai!!',
    'Bhai,chai piyega?',
    'Mangale!! Dono bhai pite hai!!',
    'Tumhe kya lagta hai ki tumhare jaisa basic chatbot bana ke kya professor impress honge?',
    'Bhai , mujhe lagta hai ki professors tumhare kaam ko dekh ke impress to ho hi jayenge',
    'Achha',
    'Hmmm!!',
    'Tera naam kya hai?',
    'Mera naam Techie hai!!',



]


trainers=ListTrainer(Abhi)

'''training using HANDWRITTEN dataseT'''

trainers.train(dataset)
# trainers.train(dataset2)

'''Aise datasets jo csv format me hai pehle hame unhe list format me conveert karna hoga tabhi hum data kouse kar payenge train karne ke liye '''

#ye function uss csv format waale datasets ko use karne me help karega
#
# def for_con(var):
#    data_Set= var[['question','answer']].values.tolist()
#    for pair in data_Set:
#      conversation= [pair[0],pair[1]]
#      trainers.train(conversation)
# #now giving datasets:
# for_con(c)
# for_con(d)
# for_con(e)
# for_con(f)
# for_con(g)


'''Ab yaha se shuru hai GUI designing'''

root = ctk.CTk()  #here root is the mainloop
root.title('TECHIE')
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
root.geometry('550x650')

#login page pe kaam karna

login_page= ctk.CTkFrame(root)
login_page.rowconfigure((0,1,2),weight=1)
login_page.columnconfigure(0,weight=1)
login_page.configure(fg_color="#E8F0FE")
login_page.grid(sticky='nsew')

ctk.CTkLabel(login_page,text='Verification',font=("Courier New Bold",50,'bold'),text_color='black').grid(pady=50)
#ab ek entry frame create karna
entry_frame= ctk.CTkFrame(login_page)
entry_frame.configure(width=500,height=200,fg_color="#E8F0FE")

entry_frame.grid(sticky='n',padx=50)
entry_frame.grid_propagate(False)
user_name=StringVar()
pass_word=StringVar()
ctk.CTkLabel(entry_frame,text='UserName',font=("Trebuchet MS",32,'bold'),text_color='black').grid(padx=30,pady=40)
ctk.CTkLabel(entry_frame,text='PassWord',font=("Trebuchet MS",32,'bold'),text_color='black').grid(padx=15,pady=40)

user_entry=ctk.CTkEntry(entry_frame,placeholder_text='Enter Your Username',textvariable=user_name).grid(row=0,column=1,padx=30,pady=40)
pass_entry=ctk.CTkEntry(entry_frame,placeholder_text='Enter Your Password',textvariable=pass_word).grid(row=1,column=1,padx=15,pady=40)

#submit_button ke liye alag frame create karna ;

submit_frame=ctk.CTkFrame(login_page)

# submit_frame.configure(width=200,height=100)
submit_frame.configure(fg_color="#E8F0FE")

submit_frame.grid(sticky='n',padx=10)

#submit ke liye function create karna

def Submit():
    with open('details.txt','a') as d:
        d.write(f'Name: {user_name.get()} \n Password: {pass_word.get()} \n')
        if user_name.get()=='AbhimanyuSingh' and pass_word.get()=='abhi8825':
            switch_pages(login_page,main_page)

            msg.showinfo('INFO','Submission Successful')
        else:
            msg.showerror('InfoError','Incorrect Inputs')


def switch_pages(from_frame,to_frame):
    from_frame.grid_remove()
    to_frame.grid(sticky='nsew',)




give=ctk.CTkButton(submit_frame,text='SUBMIT',command=Submit,width=150,height=50,font=('',20),fg_color="#1E1E2E").grid()

#side picture ke liye ek or frame create karna


#creating an another frame;
main_page=ctk.CTkFrame(root)
main_page.configure(fg_color="#282C34")
main_page.grid(row=0,column=0,sticky='nsew')
main_page.rowconfigure((0,1,2),weight=1)
main_page.columnconfigure(0,weight=1)
main_page.grid_remove()


#ab yaha se hum apne chatbot ko apne main_frame me rakhenge
logo=Image.open('pic-removebg-preview.png')
pack=ctk.CTkImage(light_image=logo,size=((380,200)),)
img_label=ctk.CTkLabel(main_page,image=pack,text='')
img_label.grid(padx=70,pady=20)


#now creating a listbox;
listbox=Listbox(main_page,width=70,height=20)
listbox.grid()
listbox.configure(bg="light blue",borderwidth=5,relief=RIDGE)
query_var=StringVar()
query=ctk.CTkEntry(main_page,textvariable=query_var,placeholder_text='Enter your query here',width=350,height=30,fg_color='white',text_color='black')
query.grid(pady=30)

#Creating an another frame for buttons  (
button_frame=ctk.CTkFrame(main_page)
button_frame.grid(sticky='ew',padx=10,pady=20)
button_frame.configure(fg_color="#282C34")
#Ab typing effect lagana hai isme:
def typing_effect(text,index=0):
    if index==0:
        listbox.insert(END,"")

    if index<len(text):
        current_index = listbox.size() - 1
        current_text=listbox.get(current_index)
        listbox.delete(current_index)
        listbox.insert(END,current_text + text[index])
        listbox.update()
        listbox.after(50,typing_effect,text,index+1)



#function create karna unn buttons ke liye

def ask():
    ques=query_var.get()
    listbox.insert(END,f'YOU: {ques}')
    # typing_effect(f'YOU: {str(ques)}')
    query.delete(0,END)
    main_page.after(1500,lambda:get_answer(ques))
    # threading.Thread(target=get_answer,args=(ques,)).start() #this will run get_answer in background

def preprocess_input(text):
    text=text.lower()
    text =re.sub(r'[^\w\s]','',text) #ye punctutation hatao
    text=re.sub(r'\bbbhai\b','',text) #bhai jaise words hata>>
    text=text.strip()
    return text

def get_answer(ques):
    ques=preprocess_input(ques)
    try:
       answer=Abhi.get_response(ques)
       # listbox.insert(END,f'TECHIE: {str(answer)}')
       typing_effect(f'BOT: {str(answer)}')
    except Exception as e:
        typing_effect('Bot: Mujhe ye Sawal samjh nhi aya.')
        print('Error:',e)

def Clear():
    listbox.delete(0,END)

def Save():
    with open('CHAT_HISTORY.txt','w') as f:
        for i in range(listbox.size()):
            f.write(f'{listbox.get(i)}\n')



#button create karna

clear=ctk.CTkButton(button_frame,text='CLear',command=Clear)
ask=ctk.CTkButton(button_frame,text='Ask',command=ask)
save=ctk.CTkButton(button_frame,text='Save',command=Save)
clear.grid(row=0,column=0,padx=15,sticky='')
ask.grid(row=0,column=2,padx=15,sticky='')
save.grid(row=0,column=10,padx=15,sticky='e')
clear.configure(hover_color='green')
ask.configure(hover_color='green')
save.configure(hover_color='green')




#defining function


#yaha bhi kaam karna hai login page





#


root.mainloop()


'''Creating a function throught which our chatbot can take input and give responses'''





