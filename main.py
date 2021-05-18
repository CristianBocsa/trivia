from tkinter import *
from tkinter import messagebox as mb
import json

root = Tk()
root.geometry("800x500")
root.title("Bocsa Cristian, Magda Alexandru")
with open('intrebari.json') as f:
    x = json.load(f)
intrebari = (x['intr'])
variante = (x['var'])
raspunsuri = (x['rasp'])


class Quiz:
    def __init__(self):
        self.intreb = 0
        self.ques = self.intrebari(self.intreb)
        self.opt_selectata = IntVar()
        self.opts = self.cerculete()
        self.display(self.intreb)
        self.butoane()
        self.corect = 0

    def intrebari(self, qn):
        t = Label(root, text="Triviador", width=48, bg="black", fg="white", font=("arial", 20, "bold", "italic"))
        t.place(x=0, y=5)
        qn = Label(root, text=intrebari[qn], width=60, fg="black", font=("times", 16, "bold"), anchor="center")
        qn.place(x=70, y=100)
        return qn

    def cerculete(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text="", variable=self.opt_selectata, value=val + 1, font=("arial", 15, "bold"))
            b.append(btn)
            btn.place(x=50, y=yp)
            val = val + 1
            yp = yp + 40
        return b

    def display(self, qn):
        val = 0
        self.opt_selectata.set(0)
        self.ques['text'] = intrebari[qn]
        for op in variante[qn]:
            self.opts[val]['text'] = op
            val += 1

    def butoane(self):
        urmator = Button(root, text="Urmatoarea intrebare", command=self.but_urm, width=20, bg="green", fg="black",
                         font=("times", 16, "bold"), anchor="center")
        urmator.place(x=275, y=380)
        exit = Button(root, text="Quit", command=root.destroy, width=10, bg="red", fg="black",
                            font=("times", 16, "bold"), anchor="center")
        exit.place(x=335, y=430)

    def validare(self, qn):
        if self.opt_selectata.get() == raspunsuri[qn]:
            return True

    def but_urm(self):
        if self.validare(self.intreb):
            self.corect =self.corect + 1
        self.intreb = self.intreb + 1
        if self.intreb == len(intrebari):
            self.display_rezultate()
        else:
            self.display(self.intreb)

    def display_rezultate(self):
        scor = int(self.corect / len(intrebari) * 100)
        rezultat = "Procentaj raspunsuri : " + str(scor) + "%"
        ramase = len(intrebari) - self.corect
        correct = "Numarul raspunsurilor corecte: " + str(self.corect)
        gresit = "Numarul raspunsurilor gresite: " + str(ramase)
        mb.showinfo("Rezultat", "\n".join([rezultat, correct, gresit]))


quiz = Quiz()
root.mainloop()
