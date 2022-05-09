from tkinter import *
import csv

def student_name(user_name):
    try:
        user_name = user_name.upper().strip()
        if user_name.isalpha() == False:
            raise ValueError('Input is not all letters')
        else:
            return user_name
    except ValueError as e:
        print(f"Error = {e}")
        return "Error"

def student_score(user_score):
    try:
        user_score = float(user_score)
        if (user_score < 0) or (user_score > 100):
            raise ValueError('Invalid score range')
        else:
            return user_score
    except ValueError as e:
        print(f"Error = {e}")
        return "Error"

def letter_grade(user_score):
    try:
        user_score = float(user_score)
        if (user_score < 0) or (user_score > 100):
            raise ValueError('Invalid score')
        else:
            if user_score >= 90:
                return("A")
            elif user_score >= 80:
                return("B")
            elif user_score >= 70:
                return("C")
            elif user_score >= 60:
                return("D")
            elif user_score < 60:
                return("F")
    # for values like <0 or >100 or 'ten'
    except ValueError as e:
        print(f"Error = {e}")
        return "Error"


class GUI:
    def __init__(self, window):
        self.window = window

        # name
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Enter Name')
        self.entry_name = Entry(self.frame_name)

        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', pady=10)  # anchor='w' helps to change the frame position from center to west.

        # score
        self.frame_score = Frame(self.window)
        self.label_score = Label(self.frame_score, text='Enter Score')
        self.entry_score = Entry(self.frame_score)

        self.label_score.pack(side='left', padx=5)
        self.entry_score.pack(side='left', padx=5)
        self.frame_score.pack(anchor='w', pady=10)

        # enter button
        self.frame_bottom = Frame(self.window)
        self.button_enter = Button(self.frame_bottom, text='ENTER', command=self.clicked)
        self.button_enter.pack(pady=10)
        self.frame_bottom.pack()

    def clicked(self):
        # loop with exceptions for functions
        user_name = self.entry_name.get()
        user_score = self.entry_score.get()

        person = [student_name(user_name), student_score(user_score), letter_grade(user_score)]
        print(person)
        self.entry_name.delete(0, END)
        self.entry_score.delete(0, END)

        try:
            for value in person:
                if value == "Error":
                    raise ValueError("Invalid student input")
            # append to file
            with open('student_grades.csv', 'a', newline='') as csvfile:
                content = csv.writer(csvfile)
                content.writerow(person)
        except ValueError as e:
            print(f"Error = {e}")
