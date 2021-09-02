#!/usr/bin/python3
# d2={"harry":{ "m":"burger","a":"roti","n":"fish"}}
# print(d2["harry"])
# print(d2["rohit"])
# print(d2["harry"]["m"])
# d3=d2.copy()
# print(d3["harry"]["m"])
# print(d2.keys())
# print(d2.items())
# del d2["harry"]["n"]
# print(d2.items())
# print(d3.items())#
# del d3["harry"]["m"]
# print(d2.items())
# print(d2.items())
# list=[1,1,2,3,4,5,5,]
# print(22 not in list)
# a=55
# print(a) if a is 5 else print(0)

# def function(a,b):
# """this is function which print hellow world"""
## print(a+b)


# function(5,6)
# print(function.__doc__)

# Try except exception handling.

# print("Enter number")
# num1 = input()
# print("Enter number")
# num2 = input()

# try:
# print("The sum is ",int(num1)+int(num2))

## print(a)

# print("This is very important")
#
# print("This is very important")

# File input output basic

# f = open("simple.txt", "w")
# a = f.write("This is file writing program\n")
# print(a)
# f.close()

# f = open("simple.txt", "a")
# a = f.write("This is file writing program\n")
# print(a)
# f.close()

# *****handle read and write both*****

# f = open("simple.txt", "r+")
# print(f.read())
# f.write("Thank you")
# print(f.read())


# *****seek and tell function of file handling*****

# f = open("simple.txt")
# f.seek(11)#to set the pointer at 11th position
# print(f.tell())#to get the info about file pointer
# print(f.readline())

# *****Using with block to open file*****

# with open("harry.txt") as f:    #when we use it we don't need to close file.
#     a = f.read(4)
#     print(a)
# f = open("simple.txt", "rt")
# print(f.readline())

# Health Management System
# 3 clients - Harry, Rohan and Hammad

# def getdate():
#     import datetime
#     return datetime.datetime.now()


# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


# bhai ye rha program
# import datetime
#
#
# def gettime():
#     return datetime.datetime.now()
#
#
# def take(k):
#     if k == 1:
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("harry-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("harry-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     elif (k == 2):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("rohan-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("rohan-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     elif (k == 3):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("hammad-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("hammad-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     else:
#         print("plz enter valid input (1(harry),2(rohan),3(hammad)")
#

# def retrieve(k):
#     if k == 1:
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             with open("harry-ex.txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("harry-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     elif (k == 2):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             with open("rohan-ex.txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("rohan-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     elif (k == 3):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             with open("hammad-ex.txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("hammad-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     else:
#         print("plz enter valid input (harry,rohan,hammad)")
#
#
# print("health management system: ")
# a = int(input("Press 1 for log the value and 2 for retrieve "))
#
# if a == 1:
#     b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
#     take(b)
# else:
#     b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
#     retrieve(b)


# import datetime
# def gettime():
#     import datetime
#     return datetime.datetime.now()
#
# print(gettime())

# ***Recurtion:Recursive vs Interative Approach***


# note:n! = n * n-1 * n-2 * n-3.......
#      n! = n * (n-1)!

# def factorial_iterative(n):
#     """
#
#         :param n: integer
#         :return: n * n-1 * n-2 * n-3.......
#         """
#     fac = 1
#     for i in range(n):
#         # print(i)
#         fac = fac * (i+1)
#     return fac


# def factorial_recursive(n):
#     """
#
#         :param n: integer
#         :return: n * n-1 * n-2 * n-3.......
#         """
#     if n==1:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)
#
# number = int(input("Enter the no for factorial"))
# print(factorial_recursive(number))


# def fibonacci(no):
#     if no==0:
#         return 0
#     elif no==1:
#         return 1
#     else:
#         return fibonacci(no-1) + fibonacci(no-2)
#
#
# number = int(input("Enter the no for fabonacci series : "))
# print(fibonacci(number))


# ***Anonymous/Lambda functions in pyhon***

# minus = lambda x,y:x-y
# print(minus(9,4))
# def a_first(a):
#     return a[1]

# a = [[1, 4], [5, 6], [8, 34]]
# a.sort(key= lambda x:x[1])
# print(a)


# *** Built in modules inpython ***
# import random

# random_number = random.randint(0, 10)
# print(random_number)

# rand = random.random() * 1000
# print(rand)
#
# rand = int(random.random() * 1000)
# print(rand)


# lst = ["star plus", "DD1", "Aaj tak", "Sony"]
# choice = random.choice(lst)
# print(choice)


# ***F_string and string formatting in python***

# me = "OMkar"
# al = 3
# a = "This is %s %s %s" % (me, 3*5 ,al)
# print(a)

# a = "this is {1} {0}"
# b = a.format(me, al)
# print(b)

# a = f"This is {me} {al}"
# print(a)


# def function_name_print(normal, abnormal):
#     """
#
#     :type args: object
#     """
#     print(normal)
#
#
# my_string = "mukya is am chutiyea"
# your_string = "You are clever"
# function_name_print(abnormal=your_string, normal=my_string)


# ****Time module in python****

# import time
#
# initial = time.time()
# k = 0
# while k < 45:
#     time.sleep(5)
#     print("This is Omkar")
#     k += 1
# while_time = time.time() - initial
# print("while loop run in ", while_time, "Seconds")
#
# for i in range(45):
#     print("This is Omkar")
#     k += 1
#
# for_time = time.time() - initial

# print(time.asctime(time.localtime(time.time())))

# ***Enumerate function***
# i = 1
# ll = ["bhindi", "aloo", "chopstick", "chowmein"]
# for item in ll:
#
#     if i % 2 != 0:
#         print(f"please buy {item}")
#     i+=1

# for inex, item in enumerate(ll):
#
#     if i % 2 != 0:
#         print(f"please buy {inex},{item}")
# a = " and ".join(ll)
# print(a)

# from pygame import mixer
#
# # Starting the mixer
# mixer.init()
#
# # Loading the song
# mixer.music.load("song.mp3")
#
# # Setting the volume
# mixer.music.set_volume(1)
#
# # Start playing the song
# mixer.music.play()
#
# # infinite loop
# while True:
#
#     print("Press 'p' to pause, 'r' to resume")
#     print("Press 'e' to exit the program")
#     query = input("  ")
#
#     if query == 'p':
#
#     # Pausing the music
#     mixer.music.pause()
# elif query == 'r':
#
#     # Resuming the music
#     mixer.music.unpause()
# elif query == 'e':
#
#     # Stop the mixer
#     mixer.music.stop()
#     break

# ************************* Setters, property decorators & deletors ************************


# class Employee:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         # self.email = f"{fname}.{lname}@codewithharry.com"
#
#     def explain(self):
#         return f"This employee is {self.fname} {self.lname}"
#
#     @property
#     def email(self):
#         if self.fname==None or self.lname == None:
#             return "Email is not set. Please set it using setter"
#         return f"{self.fname}.{self.lname}@codewithharry.com"
#
#     @email.setter
#     def email(self, string):
#         print("Setting now...")
#         names = string.split("@")[0]
#         self.fname = names.split(".")[0]
#         self.lname = names.split(".")[1]
#
#     @email.deleter
#     def email(self):
#         self.fname = None
#         self.lname = None
#
#
# hindustani_supporter = Employee("Hindustani", "Supporter")
# nikhil_raj_pandey = Employee("Nikhil", "Raj")
#
# print(hindustani_supporter.email)
#
# hindustani_supporter.fname = "US"
#
# print(hindustani_supporter.email)
# hindustani_supporter.email = "this.that@codewithharry.com"
# print(hindustani_supporter.fname)
#
# del hindustani_supporter.email
# print(hindustani_supporter.email)
# hindustani_supporter.email = "Harry.Perry@codewithharry.com"
# print(hindustani_supporter.email)
#
#********************************* Generators *************************************************

# def getNum (x):
#     for i in range(x):
#         yield i
#
# seq = getNum (2)
# print(seq.__next__())
# print(seq.__next__())
# print(seq.__next__())


# *********************************** Coroutines ************************************************


# def searcher():
#     import time
#     # Some 4 seconds time consuming task
#     book = "This is a book on harry and code with harry and good"
#     time.sleep(4)
#
#     while True:
#         text = (yield)
#         if text in book:
#             print("Your text is in the book")
#         else:
#             print("Text is not in the book")
#
# search = searcher()
# print("search started")
# next(search)
# print("Next method run")
# search.send("harry")
# next(search)

# search.close()
# search.send("harry")
# input("press any key")
# search.send("harry and")
# input("press any key")
# search.send("thi si")
# input("press any key")
# search.send("joker")
# input("press any key")
# search.send("like this video")


# import requests
# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "id": 1,
#     "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
# }
# r = requests.post(url=url, data=data)
# print(r.json())







# ********************************** Command line utility **************************************

# import argparse
# import sys
#
# def calc(args):
#     if args.o == 'add':
#         return args.x + args.y
#
#     elif args.o == 'mul':
#         return args.x * args.y
#
#     elif args.o == 'sub':
#         return args.x - args.y
#
#     elif args.o == 'div':
#         return args.x / args.y
#
#     else:
#         return "Something went wrong"
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--x', type=float, default=1.0,
#                         help="Enter first number. This is a utility for calculation. Please contact harry bhai")
#
#     parser.add_argument('--y', type=float, default=3.0,
#                         help="Enter second number. This is a utility for calculation. Please contact harry bhai")
#
#     parser.add_argument('--o', type=str, default="add",
#                         help="This is a utility for calculation. Please contact harry bhai for more")
#
#     args = parser.parse_args()
#     sys.stdout.write(str(calc(args)))
#
#
#
#
#
#
# # PROJECT 1:
# import pyttsx3 #pip install pyttsx3
# import speech_recognition as sr #pip install speechRecognition
# import datetime
# import wikipedia #pip install wikipedia
# import webbrowser
# import os
# import smtplib
#
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# # print(voices[1].id)
# engine.setProperty('voice', voices[0].id)
#
#
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
#
#
# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("Good Morning!")
#
#     elif hour>=12 and hour<18:
#         speak("Good Afternoon!")
#
#     else:
#         speak("Good Evening!")
#
#     speak("I am Jarvis Sir. Please tell me how may I help you")
#
# def takeCommand():
#     #It takes microphone input from the user and returns string output
#
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")
#
#     except Exception as e:
#         # print(e)
#         print("Say that again please...")
#         return "None"
#     return query
#
# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()
#
# if __name__ == "__main__":
#     wishMe()
#     while True:
#     # if 1:
#         query = takeCommand().lower()

        # Logic for executing tasks based on query
        # if 'wikipedia' in query:
        #     speak('Searching Wikipedia...')
        #     query = query.replace("wikipedia", "")
        #     results = wikipedia.summary(query, sentences=2)
        #     speak("According to Wikipedia")
        #     print(results)
        #     speak(results)
        #
        # elif 'open youtube' in query:
        #     webbrowser.open("youtube.com")
        #
        # elif 'open google' in query:
        #     webbrowser.open("google.com")
        #
        # elif 'open stackoverflow' in query:
        #     webbrowser.open("stackoverflow.com")
        #
        #
        # elif 'play music' in query:
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))
        #
        # elif 'the time' in query:
        #     strTime = datetime.datetime.now().strftime("%H:%M:%S")
        #     speak(f"Sir, the time is {strTime}")
        #
        # elif 'open code' in query:
        #     codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(codePath)
        #
        # elif 'email to harry' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "harryyourEmail@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend harry bhai. I am not able to send this email")

# import os
# import subprocess, sys
#
# query = "play music"
#
# if 'play music' in query:
#     music_dir = '/home/omkar223/Omkar/Study/Programming/Python/Music'
#     songs = os.listdir(music_dir)
#     print(songs)
#     file_path = (os.path.join(music_dir, songs[1]))
#     print(file_path)
#     import subprocess, sys
#
#     opener = "open" if sys.platform == "darwin" else "xdg-open"
#     subprocess.call([opener, filename])



# import speech_recognition as sr
#
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Listning...")
#     audio = r.listen(source)
#
# try:
#     print("Recognizing...")
#     query = r.recognize_google(audio, language='en-in')
#     print(f"You said: {query}\n")
#
# except Exception as e:
#     print(e)
#     print("Can't reconizing, say again please...")
import smtplib



# def SendMail(to, content):
#     """
#     it takes Two arguements as input and send the email to given id
#     :param to: Email id
#     :param content: content to write in mail
#     :return:
#     """
#     server = smtplib.SMTP('smtp.gmail.com', 587) #host − This is the host running your SMTP server. You can specify IP address of the host or a domain name like tutorialspoint.com. 587 ia a port no of gmail.com.
#     server.ehlo()
#     server.starttls()
#     server.login('omkardannak2003@gmail.com', 'Anita@2452000')
#     server.sendmail('omkardannak2003@gmail.com', to, content)
#     server.close()


# if __name__ == '__main__':

    # SendMail("omkardannak24@gmail.com", "Hii")

dic = {"omkar": "omkardannak24@gmail.com", "mukunda": "mmhasalkar@gmail.com"}
to = "omkar"
print(dic[to])



