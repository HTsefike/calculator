from tkinter import*

root=Tk()
root.title("HT Calculator")
root.config(bg="black")
root.geometry("680x468+100+100")

entryField = Entry(root, font=("ariel",20,"bold"), bg="black",fg="white",bd=10,relief="sunken",width=30)
entryField.grid(row=0,column=0)

button_text_list = ["C", "CE", "./", "+", "n", "cos0", "tan0", "sin0",
                    "1", "2", "3", "-", "2n", "cosh","tanh","sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u0083", "x\u0082",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "o",
                    "0", "-", ",", "%", "=", "log.", "(", ")", "x!"]

root.mainloop()