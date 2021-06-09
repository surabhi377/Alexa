import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

class Widget():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TTS")
        self.root.resizable(0,0)
        self.root.configure(background="black")
        self.lable = tk.Label(self.root,bg="black",fg="white",font="Arial 30 bold",text="What you want me to speak?" )
        self.lable.pack()
        self.entry = tk.Entry(self.root, width=36, font="Arial 26")
        self.entry.pack()
        self.button = tk.Button(self.root,bg="black",fg="white",font="Arial 30 bold",text="!speak!",command=self.clicked )
        self.button.pack()
        self.root.mainloop()    
     
    def clicked(self):
        text = self.entry.get()
        self.speak(text)

    def speak(self,text):
        engine.say(text)
        engine.runAndWait()

if __name__ == "__main__":
    temp = Widget()