#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Импортируем некоторые модули
# Библиотека sys
import sys
# Библиотека PyQt5
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
# Локальный config.py и классы
from config import *
from chatUI import ChatUI
from client import Client


if __name__ == '__main__':
  # Создание приложения
  app = QApplication(sys.argv)
  wig = QWidget()
  # Пользовательский интерфейс GUI
  gui = ChatUI(wig, WIDTH_MIN, WIDTH_MAX, HEIGHT_MIN, HEIGHT_MAX)
  # Логика приложения
  client = Client(gui)
  # Отобразить главное окно
  wig.show()
  # Конец приложения (закрытие)
  sys.exit(app.exec_())
