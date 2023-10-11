import Password
from tkinter import *;



    


window= Tk();
window.title("Password Encryption Saver")
window.iconbitmap("james.ico")
title_main = Label(window, text="Password Encryption Saver", font=("Arial", 20));
# choice= Label(window, text="Do you want to add,remove or see a specific or all passwords?(ADD,REMOVE,SEE ALL,SPECIFIC)", font=("Arial", 10));
# choice_input = Entry(window, width=80);
add_button = Button(window,text="ADD",font=("Arial", 20),command= lambda:Password.add_password(window))
remove_button = Button(window,text="REMOVE",font=("Arial", 20),command=lambda: Password.remove_window(window))
see_all_button = Button(window,text="SEE ALL",font=("Arial", 20),command=lambda: Password.seeList(window))
specific_button = Button(window,text="SPECIFIC",font=("Arial", 20),command=lambda: Password.get_specific_password_window(window))

if __name__ == "__main__":

    title_main.pack_configure(pady=10, padx=10);
    add_button.pack(pady=10,padx=10);
    remove_button.pack(pady=10,padx=10);
    see_all_button.pack(pady=10,padx=10);
    specific_button.pack(pady=10,padx=10)
    window.mainloop();



