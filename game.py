import os
import cv2
import time
import random
from tkinter import *
from PIL import ImageTk, Image
import threading
import numpy as np
from sys import platform

class Note():
    def __init__(self) -> None:
        self.answer = None
        self.image_path = None
        self.mat = None

def load_data():
    ipatsh = [os.path.join(os.getcwd(), "notes", i) for i in os.listdir(os.path.join(os.getcwd(), "notes"))]
    
    Notes = []

    for i in ipatsh:
        a = Note()
        a.image_path = i
        a.mat = cv2.imread(i, cv2.IMREAD_UNCHANGED)
        if platform == "linux":
            a.answer = i.split("/")[-1].split("_")[1]
        else:
            a.answer = i.split("\\")[-1].split("_")[1]
        Notes.append(a)
    return Notes

global imagelist

class Gui():
    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry("550x300+300+150")
        self.root.attributes("-topmost",True)
        self.panel = Label(self.root)
        self.panel.pack()
        self.update()
        self.root.mainloop()

    def update(self):
        global imagelist
        self.image = imagelist[0]
        self.image = ImageTk.PhotoImage(Image.fromarray(self.image, mode="L"))
        self.panel.configure(image=self.image)
        self.panel.update()
        self.panel.after(100, self.update)

def create_gui():
    aa = Gui()

def game():
    Notes = load_data()
    

    global imagelist
    imagelist = [np.zeros((250,162),dtype=np.uint8)]

    t = threading.Thread(target=create_gui)
    t.start()

    time.sleep(1)
    while True:
        random.shuffle(Notes)

        start = time.time()
        correct_answers = 0
        
        for i in Notes:
            imagelist[0] = cv2.cvtColor(i.mat, cv2.COLOR_BGR2GRAY)
            answer = input("Answer: ")
            if answer == i.answer or answer.lower() == i.answer or answer.capitalize() == i.answer:
                print("Correct")
                correct_answers += 1
            else:
                print(f"Incorrect. Answer is {i.answer}")
                time.sleep(5)

        end = time.time()

        print(f"Took {end-start} and got {correct_answers/len(Notes)*100} % correct")











if __name__ == "__main__":
    game()