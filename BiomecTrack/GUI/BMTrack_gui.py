import logging

from BiomecTrack.LOGGER.Logger import Logger


class BMTrack:
    root_element = None
    logger = None

    def __init__(self, root_element):
        self.root_element = root_element
        self.logger = Logger(logging)

        # Define o tamanho da janela principal para o tamanho da tela menos 200 pixels
        self.root_element.geometry(f"{self.root_element.winfo_screenwidth() - 200}x{self.root_element.winfo_screenheight() - 200}")

