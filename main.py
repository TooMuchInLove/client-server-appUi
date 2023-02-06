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


if __name__ == '__main__':
  # Создание приложения
  app = QApplication(sys.argv)
  wig = QWidget()
  # Экземпляр объекта класса
  rui = ChatUI(wig, WIDTH_MIN, WIDTH_MAX, HEIGHT_MIN, HEIGHT_MAX)
  # Отобразить главное окно
  wig.show()
  # Конец приложения (закрытие)
  sys.exit(app.exec_())
