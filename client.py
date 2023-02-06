#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Client:
    def __init__(self, _gui):
        # Пользовательский интерфейс и компоненты
        self.gui = _gui
        #
        self.__ip = None
        self.__port = None
        self.__PRIVATE_KEY = None
        # Ключи для шифрования текущего клиента
        self.__CLIENT_PRIVATE_KEY = None
        self.__CLIENT_PUBLIC_KEY = None
        # События нажатий на кнопки
        self.click_events()

    def click_events(self):
        self.gui.PBClearMessage.clicked.connect(self.clear_lineedit)

    def clear_lineedit(self):
        # Очистка поля для воода клиентский сообщений
        self.gui.LETextMessage.clear()
