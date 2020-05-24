import logging
from tkinter import *

from BiomecTrack.LOGGER.Logger import Logger
from BiomecTrack.UTILS import file_utils as file_utils


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
        video_menu.add_command(label="Open Camera 1", command=lambda: self.load_video_file(1))
        video_menu.add_command(label="Open Camera 2", command=lambda: self.load_video_file(2))
        video_menu.add_command(label="Open Camera 3", command=lambda: self.load_video_file(3))
        video_menu.add_command(label="Open Camera 4", command=lambda: self.load_video_file(4))
        menubar.add_cascade(label="Load Videos", menu=video_menu)
        self.root_element.configure(menu=menubar)

    def load_video_file(self, cam_number):
        if cam_number == 1:
            self.camera_1_video = file_utils.open_video_file(title="Load Cam 1 Video FIle")
        elif cam_number == 2:
            self.camera_2_video = file_utils.open_video_file(title="Load Cam 2 Video FIle")
        elif cam_number == 3:
            self.camera_3_video = file_utils.open_video_file(title="Load Cam 3 Video FIle")
        elif cam_number == 4:
            self.camera_4_video = file_utils.open_video_file(title="Load Cam 4 Video FIle")
