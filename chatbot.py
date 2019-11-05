import requests
import json
import aiml
from sqlite3 import connect
import numpy as np
import matplotlib.pyplot as plt  
import pandas as pd  
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('/home/subhash/Desktop/AI/scorestitles.csv')  # load data set

pred = []
i = 1
while (i < 39):
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(data.iloc[:, 0].values.reshape(-1, 1), data.iloc[:, i].values.reshape(-1, 1))  # perform linear regression
    slope = linear_regressor.coef_
    intercept = linear_regressor.intercept_
    a = (slope*12) + (intercept)
    pred.append(a)
    i = i + 1

conn = connect("conv.db",timeout=10)
chat='create table if not exists '+'conversation'+'(id INT,user TEXT,bot TEXT)'
database='create table if not exists '+'user_details'+'(user_name TEXT NOT NULL,phone_number INTEGER NOT NULL,BITSAT_id INTEGER NOT NULL,score INTEGER NOT NULL,preferred_branch INTEGER NOT NULL)'
conn.execute(chat)
conn.execute(database)
conn.commit()
cursor=conn.execute('SELECT id from conversation')

id=0
for items in cursor:
	id=items[0]
id=id+1
def insert(u,b):
	conn.execute("INSERT INTO conversation (id,user,bot) VALUES (?,?,?) ",(id,u,b))
	conn.commit()

kernel=aiml.Kernel()
kernel.learn("bot/start.aiml")
kernel.respond("learn ai")


while True:
    u=input("Bot:")
    u0 = u.find("BITSAT")
    u1 = u.find("Bitsat")
    u2 = u.find("bitsat")
    u3 = u.find("Previous")
    u4 = u.find("previous")
    s=kernel.respond(u)
    if s == "qwerty" or ((u0 or u1 or u2) and not (u3 or u4)):
        print("Enter your name : " )
        sname = input()
        print("Enter your Phone Number : ")
        snumber = input()
        print("Enter your BITSAT id : ")
        sid = input()
        print("Enter your score :" )
        sscore = int(input())
        print( "Preferred branch : " )
        print(" Enter 0 for Pilani-B.E. Chemical ")
        print(" Enter 1 for Pilani-B.E. Civil ")
        print(" Enter 2 for Pilani-B.E. Electrical & Electronics ")
        print(" Enter 3 for Pilani-B.E. Mechanical ")
        print(" Enter 4 for Pilani-B.E. Manufacturing ")
        print(" Enter 5 for Pilani-B.Pharm. ")
        print(" Enter 6 for Pilani-B.E. Computer Science ")
        print(" Enter 7 for Pilani-B.E. Electronics & Instrumentation ")
        print(" Enter 8 for Pilani-M.Sc. Biological Sciences ")
        print(" Enter 9 for Pilani-M.Sc. Chemistry ")
        print(" Enter 10 for Pilani-M.Sc. Economics ")
        print(" Enter 11 for Pilani-M.Sc. Mathematics ")
        print(" Enter 12 for Pilani-M.Sc. Physics ")
        print(" Enter 13 for Goa-B.E. Chemical ")
        print(" Enter 14 for Goa-B.E. Electrical and Electronics ")
        print(" Enter 15 for Goa-B.E. Mechanical ")
        print(" Enter 16 for Goa-B.E. Computer Science ")
        print(" Enter 17 for Goa-B.E. Electronics & Instrumentation ")
        print(" Enter 18 for Goa-B.E. Electronics & Communication ")
        print(" Enter 19 for Goa-M.Sc. Biological Sciences ")
        print(" Enter 20 for Goa-M.Sc. Chemistry ")
        print(" Enter 21 for Goa-M.Sc. Economics ")
        print(" Enter 22 for Goa-M.Sc. Mathematics ")
        print(" Enter 23 for Goa-M.Sc. Physics ")
        print(" Enter 24 for Hyderabad-B.E. Chemical ")
        print(" Enter 25 for Hyderabad-B.E. Civil ")
        print(" Enter 26 for Hyderabad-B.E. Electrical and Electronics ")
        print(" Enter 27 for Hyderabad-B.E. Mechanical ")
        print(" Enter 28 for Hyderabad-B.E. Computer Science ")
        print(" Enter 29 for Hyderabad-B.E. Electronics & Communication ")
        print(" Enter 30 for Hyderabad-B.E. Electronics & Instrumentation ")
        print(" Enter 31 for Hyderabad-B.E. Manufacturing ")
        print(" Enter 32 for Hyderabad-B.Pharm. ")
        print(" Enter 33 for Hyderabad-M.Sc. Biological Sciences ")
        print(" Enter 34 for Hyderabad-M.Sc. Chemistry ")
        print(" Enter 35 for Hyderabad-M.Sc. Economics ")
        print(" Enter 36 for Hyderabad-M.Sc. Mathematics ")
        print(" Enter 37 for Hyderabad-M.Sc. Physics ")
        sbranch = int(input())
        conn.execute("INSERT INTO user_details (user_name,phone_number,BITSAT_id,score,preferred_branch) VALUES (?,?,?,?,?) ",(sname,snumber,sid,sscore,sbranch))
        conn.commit()
        if pred[sbranch] <= sscore:
            print("You may get your preferred branch")
        else: 
            print("You may not get your preferred branch")
        continue
    elif s == "score" or u3 or u4:
        print("Select the branch code for which you need cutoff")
        print(" Enter 0 for Pilani-B.E. Chemical ")
        print(" Enter 1 for Pilani-B.E. Civil ")
        print(" Enter 2 for Pilani-B.E. Electrical & Electronics ")
        print(" Enter 3 for Pilani-B.E. Mechanical ")
        print(" Enter 4 for Pilani-B.E. Manufacturing ")
        print(" Enter 5 for Pilani-B.Pharm. ")
        print(" Enter 6 for Pilani-B.E. Computer Science ")
        print(" Enter 7 for Pilani-B.E. Electronics & Instrumentation ")
        print(" Enter 8 for Pilani-M.Sc. Biological Sciences ")
        print(" Enter 9 for Pilani-M.Sc. Chemistry ")
        print(" Enter 10 for Pilani-M.Sc. Economics ")
        print(" Enter 11 for Pilani-M.Sc. Mathematics ")
        print(" Enter 12 for Pilani-M.Sc. Physics ")
        print(" Enter 13 for Goa-B.E. Chemical ")
        print(" Enter 14 for Goa-B.E. Electrical and Electronics ")
        print(" Enter 15 for Goa-B.E. Mechanical ")
        print(" Enter 16 for Goa-B.E. Computer Science ")
        print(" Enter 17 for Goa-B.E. Electronics & Instrumentation ")
        print(" Enter 18 for Goa-B.E. Electronics & Communication ")
        print(" Enter 19 for Goa-M.Sc. Biological Sciences ")
        print(" Enter 20 for Goa-M.Sc. Chemistry ")
        print(" Enter 21 for Goa-M.Sc. Economics ")
        print(" Enter 22 for Goa-M.Sc. Mathematics ")
        print(" Enter 23 for Goa-M.Sc. Physics ")
        print(" Enter 24 for Hyderabad-B.E. Chemical ")
        print(" Enter 25 for Hyderabad-B.E. Civil ")
        print(" Enter 26 for Hyderabad-B.E. Electrical and Electronics ")
        print(" Enter 27 for Hyderabad-B.E. Mechanical ")
        print(" Enter 28 for Hyderabad-B.E. Computer Science ")
        print(" Enter 29 for Hyderabad-B.E. Electronics & Communication ")
        print(" Enter 30 for Hyderabad-B.E. Electronics & Instrumentation ")
        print(" Enter 31 for Hyderabad-B.E. Manufacturing ")
        print(" Enter 32 for Hyderabad-B.Pharm. ")
        print(" Enter 33 for Hyderabad-M.Sc. Biological Sciences ")
        print(" Enter 34 for Hyderabad-M.Sc. Chemistry ")
        print(" Enter 35 for Hyderabad-M.Sc. Economics ")
        print(" Enter 36 for Hyderabad-M.Sc. Mathematics ")
        print(" Enter 37 for Hyderabad-M.Sc. Physics ")
        prevscore = int(input())
        print("previous scores from 2008 to 2019")
        print(data.iloc[:, prevscore+1].values.reshape(-1, 1))
    s=s.split('newline')
    ch=False
    v=""
    for item in s:
        print(str(item))
        v=v+str(item)
        if 'Bye' in item:
            ch=True
    insert(u,v)
    if ch :
        break
