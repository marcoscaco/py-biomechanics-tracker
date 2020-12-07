import logging
from tkinter import *
from tkinter.ttk import *
import cv2
from PIL import Image
from PIL import ImageTk
import numpy as np

from BiomecTrack.LOGGER.Logger import Logger
from BiomecTrack.UTILS import file_utils as file_utils


class BMTrack:
    root_element = None
    logger = None
    camera_1_video = None
    camera_1_frames = []
    camera_1_frame_count = 0
    camera_2_video = None
    camera_2_frames = []
    camera_2_frame_count = 0
    camera_3_video = None
    camera_3_frames = []
    camera_3_frame_count = 0
    camera_4_video = None
    camera_4_frames = []
    camera_4_frame_count = 0

    video_load_dialog = None
    video_load_progress_bar = None
    video_load_progress_text = None

    video_frame_frame = None
    camera_been_show = 0

    def __init__(self, root_element):
        print("Ola construido")
        self.root_element = root_element

        self.logger = Logger(logging)

        # Define o tamanho da janela principal para o tamanho da tela menos 200 pixels
        # self.root_element.geometry(f"{self.root_element.winfo_screenwidth() - 200}x{self.root_element.winfo_screenheight() - 200}")
        self.root_element.geometry(f"1500x500")

        # Keyboard Binding
        self.root_element.bind("<Key>", self.keyboard_handler)
        self.root_element.bind("<Left>", self.keyboard_handler)
        self.root_element.bind("<Right>", self.keyboard_handler)

        menubar = Menu(root_element)

        # create a pulldown menu, for loading the videos and add it to the menu bar
        video_menu = Menu(menubar, tearoff=0)
        video_menu.add_command(label="Open Camera 1", command=lambda: self.load_video_file(0))
        video_menu.add_command(label="Open Camera 2", command=lambda: self.load_video_file(1))
        video_menu.add_command(label="Open Camera 3", command=lambda: self.load_video_file(2))
        video_menu.add_command(label="Open Camera 4", command=lambda: self.load_video_file(3))
        menubar.add_cascade(label="Load Videos", menu=video_menu)

        # create a pulldown menu, for loading the videos and add it to the menu bar
        inference_menu = Menu(menubar, tearoff=0)
        inference_menu.add_command(label="Inference on: Camera 1", command=lambda: None)
        inference_menu.add_command(label="Inference on: Camera 2", command=lambda: None)
        inference_menu.add_command(label="Inference on: Camera 3", command=lambda: None)
        inference_menu.add_command(label="Inference on: Camera 4", command=lambda: None)
        menubar.add_cascade(label="Videos Inference", menu=inference_menu)
        self.root_element.configure(menu=menubar, background='gray')

    def load_video_file(self, cam_number):
        if cam_number == 0:
            self.camera_1_video = file_utils.open_video_file(title="Load Cam 1 Video FIle")
            if self.camera_1_video:
                vidcap = cv2.VideoCapture(self.camera_1_video)
                video_len = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
                success, image = vidcap.read()
                count = 1
                self.create_video_load_progress_bar(video_len=video_len)
                while success:
                    # video_read_progress = int(100 * float(count) / float(video_len))
                    success, image = vidcap.read()
                    if image is not None:
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                        self.camera_1_frames.append(image)
                        count += 1
                        self.update_video_load_progress_bar(value=count, max=video_len)
                self.detroy_video_load_progress_bar()
            else:
                print("Nao carregou")

        elif cam_number == 1:
            self.camera_2_video = file_utils.open_video_file(title="Load Cam 2 Video FIle")
            if self.camera_2_video:
                vidcap = cv2.VideoCapture(self.camera_2_video)
                video_len = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
                success, image = vidcap.read()
                count = 1
                self.create_video_load_progress_bar(video_len=video_len)
                while success:
                    # video_read_progress = int(100 * float(count) / float(video_len))
                    success, image = vidcap.read()
                    if image is not None:
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                        self.camera_2_frames.append(image)
                        count += 1
                        self.update_video_load_progress_bar(value=count, max=video_len)
                self.detroy_video_load_progress_bar()
                print(self.camera_2_frames)
            else:
                print("Nao carregou")

        elif cam_number == 2:
            self.camera_3_video = file_utils.open_video_file(title="Load Cam 3 Video FIle")
            if self.camera_3_video:
                vidcap = cv2.VideoCapture(self.camera_3_video)
                video_len = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
                success, image = vidcap.read()
                count = 1
                self.create_video_load_progress_bar(video_len=video_len)
                while success:
                    # video_read_progress = int(100 * float(count) / float(video_len))
                    success, image = vidcap.read()
                    if image is not None:
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                        self.camera_3_frames.append(image)
                        count += 1
                        self.update_video_load_progress_bar(value=count, max=video_len)
                self.detroy_video_load_progress_bar()
            else:
                print("Nao carregou")
        elif cam_number == 3:
            self.camera_4_video = file_utils.open_video_file(title="Load Cam 4 Video FIle")
            if self.camera_4_video:
                vidcap = cv2.VideoCapture(self.camera_4_video)
                video_len = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
                success, image = vidcap.read()
                count = 1
                self.create_video_load_progress_bar(video_len=video_len)
                while success:
                    # video_read_progress = int(100 * float(count) / float(video_len))
                    success, image = vidcap.read()
                    if image is not None:
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                        self.camera_4_frames.append(image)
                        count += 1
                        self.update_video_load_progress_bar(value=count, max=video_len)
                self.detroy_video_load_progress_bar()
            else:
                print("Nao carregou")
    
    def keyboard_handler(self, event):
        print(f"pressed {repr(event.keysym)}")
        print(event)

        if event.keysym == 't':
            self.show_frame(0)
        if event.keysym == 'q':
            self.root_element.destroy()
        if event.keysym == 'o':
            camera_counter = 0
            while camera_counter < 4:
                self.load_video_file(camera_counter)
                camera_counter += 1
        if event.keysym == '1':
            self.load_video_file(0)
        if event.char == '!':
            self.show_frame(0)
        if event.keysym == '2':
            self.load_video_file(1)
        if event.char == '@':
            self.show_frame(1)
        if event.keysym == '3':
            self.load_video_file(2)
        if event.char == '#':
            self.show_frame(2)
        if event.keysym == '4':
            self.load_video_file(3)
        if event.char == '$':
            self.show_frame(3)
        if event.keysym == 'r':
            self.reset_frames()
        if event.keysym == 'h':
            self.show_help()
        if event.keysym == "Left":
            print("arrow l")
            self.camera_1_frame_count -= 1
            self.camera_2_frame_count -= 1
            self.camera_3_frame_count -= 1
            self.camera_4_frame_count -= 1
            self.show_frame(self.camera_been_show)

        if event.keysym == "Right":
            print("arrow r")
            self.camera_1_frame_count += 1
            self.camera_2_frame_count += 1
            self.camera_3_frame_count += 1
            self.camera_4_frame_count += 1
            self.show_frame(self.camera_been_show)

    def create_video_load_progress_bar(self, video_len):
        self.video_load_dialog = Toplevel(self.root_element)
        self.video_load_dialog.configure(background='gray')
        self.video_load_dialog.title("Video Loading Progress")
        self.video_load_dialog.geometry(f"500x50+{int(self.root_element.winfo_screenwidth()/2)}+{int(self.root_element.winfo_screenheight()/2 )}")
        s = Style()
        s.theme_use('clam')
        s.configure("blue.Horizontal.TProgressbar", foreground='blue', background='blue')
        self.video_load_progress_bar = Progressbar(self.video_load_dialog, style="blue.Horizontal.TProgressbar", maximum=video_len, mode="determinate", length=400)
        self.video_load_progress_bar.grid(row=0, column=1, padx=50, pady=100)
        self.video_load_progress_bar.pack()
        self.video_load_progress_text = Label(self.video_load_dialog, text="0%")
        self.video_load_progress_text.pack()

    def update_video_load_progress_bar(self, value, max):
        self.video_load_progress_bar.configure(value=value)
        self.video_load_progress_text.configure(background='gray', text=f"{int(100 * float(value) / float(max))}%")
        self.root_element.update()

    def detroy_video_load_progress_bar(self):
        self.video_load_dialog.destroy()

    def show_help(self):
        help_top = Toplevel(self.root_element)
        Label(help_top, text="press from 1 to 4 to load cameras").pack()
        Label(help_top, text="press ! @ # $ to load cameras").pack()
        Label(help_top, text="press O to open all 4 cameras").pack()
        Label(help_top, text="press the arrows to jump frames").pack()
        Label(help_top, text="press R to reset").pack()
        Label(help_top, text="press H to show help").pack()

    def show_frame(self, cam_number):
        if cam_number == 0:
            self.camera_been_show = 0
            try:
                image = Image.fromarray(self.camera_1_frames[self.camera_1_frame_count])
            except:
                self.camera_1_frame_count -= 1
        if cam_number == 1:
            self.camera_been_show = 1
            try:
                image = Image.fromarray(self.camera_2_frames[self.camera_2_frame_count])
            except:
                self.camera_2_frame_count -= 1
        if cam_number == 2:
            self.camera_been_show = 2
            try:
                image = Image.fromarray(self.camera_3_frames[self.camera_3_frame_count])
            except:
                self.camera_3_frame_count -= 1
        if cam_number == 3:
            self.camera_been_show = 3
            try:
                image = Image.fromarray(self.camera_4_frames[self.camera_4_frame_count])
            except:
                self.camera_4_frame_count -= 1
        # # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        if self.video_frame_frame is None:
            self.video_frame_frame = Label(self.root_element, image=image)
            self.video_frame_frame.image = image
            self.video_frame_frame.grid()
        else:
            self.video_frame_frame.configure(image=image)
            self.video_frame_frame.image = image
        self.root_element.update()

    def reset_frames(self):
        blank_image = np.zeros(shape=[int(self.root_element.winfo_height()), int(self.root_element.winfo_width()), 3], dtype=np.uint8)
        self.camera_1_video = None
        self.camera_1_frames = []
        self.camera_1_frames.append(blank_image)
        self.camera_1_frame_count = 0
        self.camera_2_video = None
        self.camera_2_frames = []
        self.camera_2_frame_count = 0
        self.camera_3_video = None
        self.camera_3_frames = []
        self.camera_3_frame_count = 0
        self.camera_4_video = None
        self.camera_4_frames = []
        self.camera_4_frame_count = 0
        self.camera_been_show = 0
        self.show_frame(0)