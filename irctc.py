from tkinter import *
import requests
class Irctc:

    def __init__(self):
        self.root=Tk()
        self.root.title("My IRCTC")
        self.root.minsize(400,600) #for fixing min height of window
        self.root.maxsize(400,900) #these two lines fix the window size.
        self.root.configure(background="#0089ae")# for changing window background-color.

        self.label1=Label(self.root,text="Train Route",bg="#0089ae",fg="#ffffff")
        self.label1.configure(font=("Constantia",22,"bold"))
        self.label1.pack(pady=(30,10)) #padding-left(x) and top(y)

        self.trainNo=Entry(self.root) #for creating input field
        self.trainNo.pack(ipadx=50,ipady=10) #for changing the size of input/entry box x:width, y:height

        self.click=Button(self.root,text="Fetch Stations",width=30,height=2,command=lambda:self.fetch())
        self.click.pack(pady=(15,15))


        self.result=Label(self.root,bg="#0089ae",fg="#ffffff")
        self.result.configure(font=("Constantia",12))
        self.result.pack(pady=(5,10)) #padding-left(x) and top(y)


        self.root.mainloop()

    def fetch(self):
        stations=""
        train_no=self.trainNo.get() #for fetching input of entry
        #requested url:https://api.railwayapi.com/v2/route/train/<train number>/apikey/<apikey>/
        url="https://api.railwayapi.com/v2/route/train/{}/apikey/dcfvndu4y3/".format(train_no)
        data=requests.get(url)#thus get() is method of requests, not tinker #this function returns json file from given url
        response=data.json()#for making python understand the json file
        #print(response) #visit jsonviewer.stack.hu for viewing this response
        for i in response['route']:
            #print(i['station']['name'])
            stations=stations+i['station']['name']+"  |  "+i['scharr']+"  |  "+i['schdep']+"  |  "+str(i['distance'])+"KM"+"\n"
        self.result.configure(text=stations)
        
            
        
    
obj=Irctc()

