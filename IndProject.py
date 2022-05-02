
from tkinter import *
from tkinter import messagebox as mb
import json

root =Tk()
root.title ="Quiz"
root.geometry("800x500")
root.resizable(False ,False)
root.configure(bg="pink")

class Squiz:
    def __init__(self):
        self.qno = 0
        self.display_q()
        self.opt_sel = IntVar()
        self.opts = self.radio_buttons()
        self.disp_opt()
        self.next()
        self.total = len(question)
        self.correct = 0

    def resp(self):
        incorrect = self.total - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {incorrect}"
        score = int(self.correct / self.total * 100)
        result = f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def verify(self, qno):
        if self.opt_sel.get() == answer[qno]:
            return True


    def next_btn(self):
        if self.verify(self.qno):
            self.correct += 1
        self.qno += 1
        if self.qno == self.total:
            self.resp()
            root.destroy()
        else:
            self.display_q()
            self.disp_opt()


    def next(self):
        next= Button(root,text="Next",bg="pink",font=("Arial",15),command=self.next_btn)
        next.place(x=350, y=380)

    def disp_opt(self):
        val = 0
        self.opt_sel.set(0)
        for option in options[self.qno]:
            self.opts[val]['text'] = option
            val += 1

    def display_q(self):
        qno = Label(root,text=question[self.qno],bg="pink",font=("Arial",15),anchor='w')
        qno.place(x=70, y=100)

    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = Radiobutton(root,text=" ",variable=self.opt_sel,value=len(q_list) + 1,font=("Arial",15))
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 50
        return q_list

with open('data.json') as f:
    data = json.load(f)


question = (data['question'])
options = (data['options'])
answer = (data['answer'])

quiz = Squiz()

root.mainloop()