import logging
from tkinter import *
from tkinter.ttk import *
import cv2
from PIL import Image
from PIL import ImageTk

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

    def __init__(self, root_element):
        print("Ola construido")
        self.root_element = root_element
        self.video_frame_frame = Frame(master=self.root_element)
        self.video_frame_frame.pack()

        self.logger = Logger(logging)

        # Define o tamanho da janela principal para o tamanho da tela menos 200 pixels
        self.root_element.geometry(f"{self.root_element.winfo_screenwidth() - 200}x{self.root_element.winfo_screenheight() - 200}")

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
        self.root_element.configure(menu=menubar, background='black')

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
            image = Image.fromarray(self.camera_1_frames[self.camera_1_frame_count])
            # ...and then to ImageTk format
            image = ImageTk.PhotoImage(image)
            self.video_frame_frame.imge = image
            self.video_frame_frame.pack()

        if event.keysym == 'o':
            camera_counter = 0
            while camera_counter < 4:
                self.load_video_file(camera_counter)
                camera_counter += 1
        if event.keysym == '1':
            self.load_video_file(0)
        if event.keysym == '2':
            self.load_video_file(1)
        if event.keysym == '3':
            self.load_video_file(2)
        if event.keysym == '4':
            self.load_video_file(3)
        if event.keysym == "Left":
            print("arrow l")
            self.camera_1_frame_count -= 1
            self.camera_2_frame_count -= 1
            self.camera_3_frame_count -= 1
            self.camera_4_frame_count -= 1

        if event.keysym == "Right":
            print("arrow r")
            self.camera_1_frame_count += 1
            self.camera_2_frame_count += 1
            self.camera_3_frame_count += 1
            self.camera_4_frame_count += 1

    def create_video_load_progress_bar(self, video_len):
        self.video_load_dialog = Toplevel(self.root_element)
        self.video_load_dialog.configure(background='gray')
        self.video_load_dialog.title("Video Loading Progress")
        self.video_load_dialog.geometry(f"500x50+{int(self.root_element.winfo_screenwidth()/2)}+{int(self.root_element.winfo_screenheight()/2 )}")
        self.video_load_progress_bar = Progressbar(self.video_load_dialog, maximum=video_len, mode="determinate", length=400)
        self.video_load_progress_bar.grid(row=0, column=1, padx=50, pady=100)
        self.video_load_progress_bar.pack()
        self.video_load_progress_text = Label(self.video_load_dialog, text="0%")
        self.video_load_progress_text.pack()

    def update_video_load_progress_bar(self, value, max):
        self.video_load_progress_bar["value"] = value
        self.video_load_progress_text["text"] = f"{value} of {max}"
        self.root_element.update()

    def detroy_video_load_progress_bar(self):
        self.video_load_dialog.destroy()
