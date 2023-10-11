
import pymongo
from tkinter import *
from cryptography.fernet import Fernet
import os
import dotenv

dotenv.load_dotenv()
fernet = ""
client = pymongo.MongoClient(os.getenv("MONGO_URI"))
dataBase = client["Score"];
collection = dataBase["passwords"];
for i in collection.find():
    try:
        fernet = i["fernetKey"]
    except:
        print(i)

def add_password(windowl): 
    
    window = Tk();
    window.iconbitmap("james.ico")
    window.title("Add Password");
    
    heading = Label(window, text="Enter the heading of the password you want to encrypt: ", font=("Arial", 10));
    heading_input = Entry(window, width=80);
    password = Label(window, text="Enter the password you want to encrypt: ", font=("Arial", 10));
    password_input = Entry(window, width=80);
    heading.pack();
    heading_input.pack(pady=10, padx=10);
    password.pack();
    password_input.pack(pady=10, padx=10);
    sendButton = Button(window, text="Send", command=lambda: number_add(heading_input.get(), password_input.get(),heading));
    sendButton.pack(pady=10, padx=10);
    window.mainloop();  

def remove_window(windowl):
    
    window = Tk();
    window.iconbitmap("james.ico")
    window.title("Remove Password");
    
    heading = Label(window, text="Enter the heading of the password you want to remove: ", font=("Arial", 10));
    heading_input = Entry(window, width=80);
    heading.pack();
    heading_input.pack(pady=10, padx=10);
    sendButton = Button(window, text="Send", command=lambda: remove_passwords(heading_input.get(),heading));
    sendButton.pack(pady=10, padx=10);
    window.mainloop(); 

def get_specific_password_window(windowl):
    
    window = Tk();
    window.iconbitmap("james.ico")
    window.title("Password");
    
    heading = Label(window, text="Enter the heading of the password you want to see: ", font=("Arial", 10));
    heading_input = Entry(window, width=80);
    heading.pack();
    heading_input.pack(pady=10, padx=10);
    sendButton = Button(window, text="Send", command=lambda: get_specific_password_info(heading_input.get(),heading));
    sendButton.pack(pady=10, padx=10);
    window.mainloop(); 
    

def remove_passwords(heading_input,label):
    Heading = heading_input;
    if(Heading == "fernetKey"):
        print("You can't encrypt the fernet key");
        return;
    format = {"Heading": Heading}
    try:
        collection.delete_one(format);
        print("Password removed successfully");
        label.config(text="Password removed successfully");
    except:
        label.config(text="Password does not exsist");

def seeList(windowl):
    window = Tk();
    l = Listbox(window,font=("Arial", 10),width=50, height=20)
    window.iconbitmap("james.ico") 
    actualFernet = Fernet(fernet);
    windowl.destroy();
    
    for x in collection.find():
        if(x.get("fernetKey") != None):
            print("Confidential");
        else:
            # everything = Label(window, text=x.get("Heading") + ": " + actualFernet.decrypt(x.get("Password")).decode(), font=("Arial", 10));
            # everything.pack(pady=10, padx=10)
            text=x.get("Heading")
            password = actualFernet.decrypt(x.get("Password")).decode()
            final = text + " : " + password
            l.insert("1",final)
          
    l.pack()
    window.title("List of Passwords");
    
    window.mainloop();


def get_specific_password_info(heading_input,label):
    Heading = heading_input
    format = {"Heading": Heading}
    actualFernet = Fernet(fernet);
    encPassword = collection.find_one(format)["Password"];
    password = actualFernet.decrypt(encPassword).decode();
    label.config(text=password);


# def send(choice_input,master_window,choiceLabel):
#     choice = choice_input
#     print(type(choice));
#     if(choice == "add"):
#         add_password(master_window);
#     elif(choice == "remove"):
#         remove_window(master_window);
#     elif(choice == "see all"):
#         seeList(master_window);
#     elif(choice == "specific"):
#         get_specific_password_window(master_window);
#     else:
#         choiceLabel.config(text="Invalid Choice");

def number_add(heading_input, password_input,label):
    Heading = heading_input;
    password = password_input;
    if(Heading == "fernetKey"):
        print("You can't encrypt the fernet key");
        return;
    
    actualFernet = Fernet(fernet);
    encPassword = actualFernet.encrypt(password.encode());
    format = {"Heading": Heading, "Password": encPassword};
    try:
        collection.insert_one(format);
        print("Password added successfully");
        label.config(text="Password added successfully");
    except:
        label.config(text="Failed to add password");


