from msilib.schema import ListBox
from tkinter import *
from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ListTrainer
from PIL import Image, ImageTk
import pyttsx3 as pp
#import SpeechRecognition as sp
import mysql.connector
import re

engine=pp.init()
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voices',voices[0].id)

#speech recogntion
def print1(x,y,query):
    if query.find(x)+1 and query.find(y)+1 and query.find('cutoff')+1:
        sql = f"SELECT * FROM table1 WHERE field= '{x}' AND campus= '{y}' ;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        msgs.insert(END, "bot: ")
        for x in myresult:
            y = f"{x[1]} cutoff for {x[2]} campus is {x[0]}"
            msgs.insert(END, str(y))
            speak(str(y))
#display branches and cutoffs in the specific campus
def print2(y,query):
    if  query.find(y)+1 :
        sql = f"SELECT * FROM table1 WHERE campus= '{y}' ;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        msgs.insert(END, "bot: ")
        for x in myresult:
            y = f"branch: {x[1]} cutoff: {x[0]}"
            msgs.insert(END, str(y))
            speak(str(y))







#end speech recognition

def speak(word):
    engine.say(word)
    engine.runAndWait()






def ask_from_bot():
    query = textF.get()
    if query.find("clear")!=-1:
        speak("Clearing screen standby")
        msgs.delete(0,END)
    else:
     answer_from_bot=bot.get_response(query)
     msgs.insert(END,"you: "+ query)
     msgs.insert(END,"bot: "+ str(answer_from_bot))
     speak(answer_from_bot)
     textF.delete(0,END)







#training bot

bot=ChatBot("My bot")
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(bot)

trainer.train(conversation)





#end training bot
# handling data_base
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Alekya@736",
    database="mydatabase1",
auth_plugin="mysql_native_password"
)
mycursor = mydb.cursor()
def bitsat_score():
    query=textF.get()
    #extract number from the queries???
    number=re.findall(r'[0-9]+', query)

    if len(number)!=0:

      if len(number)==1:
       sql = f"SELECT * FROM table1 WHERE score <= {int(number[0])} "
      if len(number)==2:
        sql = f"SELECT * FROM table1 WHERE score >= {number[0]} and score <= {int(number[1])} "

      mycursor.execute(sql)

      myresult = mycursor.fetchall()
      msgs.insert(END,"bot: ")
      for x in myresult:
       y=f"You may get {x[1]} at {x[2]}"
       msgs.insert(END, str(y))
       speak(str(y))

    else:
        branch=['Computer Science','EEE','Mechanical','Civil','Chemical','Pharm','ECE','ENI','Msc biology','Msc chemistry','Msc economics','Msc maths','Msc physics']
        campus1=['Pilani','Hyderabad','Goa']
        for x in campus1:
            print2(x,query)

        for x in branch:
            for y in campus1:
                print1(x,y,query)















# end handling database







# Design of Chatbot.....
main=Tk()
main.geometry("500x500")
main.title("My Chat bot")
img=ImageTk.PhotoImage(file="logo2.png")

photoL=Label(main,image=img)

photoL.pack(pady=5)
frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=100,height=10,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
# creating the text field...
textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)
btn=Button(main,text="Ask from bot",font=("Verdana,20"),command=ask_from_bot)
btn.pack()





btn1=Button(main,text="Fetch info about Bitsat score",font=("Verdana,20"),command=bitsat_score)
btn1.pack()
def enter_function(event):
    btn.invoke()
def escape_function(event):
    btn1.invoke()

#going to bind main key with enter button
main.bind('<Return>',enter_function)
main.bind('<Escape>',escape_function)
main.mainloop()




