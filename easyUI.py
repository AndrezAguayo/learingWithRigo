from tkinter import Tk, Label, Button, StringVar

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Joke a day")

        self.label = Label(master, text="Would you like to hear a chuck norris Joke?")
        self.label.pack()

        self.greet_button = Button(master, text="Yes", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="No", command=master.quit)
        self.close_button.pack()

        self.v = StringVar()

        self.jokeLabel = Label(master, textvariable=self.v)
        self.v.set("Text!")
        self.jokeLabel.pack()


    def greet(self):
        print("Greetings!")
        self.v.set("Changed!")




root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

