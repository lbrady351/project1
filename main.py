from gui_main import *

def main():
    # create gui
    window = Tk()
    window.title("Final Project 1")
    window.geometry('250x180')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()