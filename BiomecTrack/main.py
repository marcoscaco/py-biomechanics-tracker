import tkinter
from BiomecTrack.GUI.BMTrack_gui import BMTrack


if __name__ == "__main__":
    root = tkinter.Tk()

    BMTrack(root_element=root)

    root.mainloop()