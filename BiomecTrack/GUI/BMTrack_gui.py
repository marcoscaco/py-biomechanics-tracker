import logging
from tkinter import *

from BiomecTrack.LOGGER.Logger import Logger


class BMTrack:
    root_element = None
    logger = None
    camera_1_video = None
    camera_2_video = None
    camera_3_video = None
    camera_4_video = None

    def __init__(self, root_element):
        self.root_element = root_element
        self.logger = Logger(logging)

        # Define o tamanho da janela principal para o tamanho da tela menos 200 pixels
        self.root_element.geometry(f"{self.root_element.winfo_screenwidth() - 200}x{self.root_element.winfo_screenheight() - 200}")

        menubar = Menu(root_element)

        # create a pulldown menu, for loading the videos and add it to the menu bar
        video_menu = Menu(menubar, tearoff=0)
        video_menu.add_command(label="Open Camera 1")
        video_menu.add_command(label="Open Camera 2")
        video_menu.add_command(label="Open Camera 3")
        video_menu.add_command(label="Open Camera 4")
        menubar.add_cascade(label="Load Videos", menu=video_menu)
        self.root_element.configure(menu=menubar)
