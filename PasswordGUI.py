
from tkinter import *;
import Password


    


window= Tk();
window.title("Password Encryption Saver")
window.geometry("600x500")
window.iconbitmap("james.ico")
title_main = Label(window, text="Password Encryption Saver", font=("Arial", 20));
choice= Label(window, text="Do you want to add,remove or see a specific or all passwords?(ADD,REMOVE,SEE ALL,SPECIFIC)", font=("Arial", 10));
choice_input = Entry(window, width=80);

if __name__ == "__main__":

    title_main.pack_configure(pady=10, padx=10);
    choice.pack();
    choice_input.pack(pady=10, padx=10);
    sendButton = Button(window, text="Send", command=lambda: Password.send(choice_input.get().lower(),window,choice));
    sendButton.pack(pady=10, padx=10);
    window.mainloop();



