#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Описание некоторых модулей
#
# Модуль QtCore содержит основные классы, включая цикл событий и механизм сигналов и слотов Qt. Он также включает в себя независимые от платформы абстракции для анимации, конечных автоматов, потоков, сопоставленных файлов, общей памяти, регулярных выражений, а также настроек пользователя и приложения.
#
# Модуль QtGui содержит классы для интеграции оконной системы, обработки событий, 2D-графики, базовых изображений, шрифтов и текста. Он также содержит полный набор привязок OpenGL и OpenGL ES (см. раздел Поддержка OpenGL). Разработчики приложений обычно используют это с API более высокого уровня, такими как те, которые содержатся в модуле QtWidgets.
#
# Модуль QtWidgets содержит классы, которые предоставляют набор элементов пользовательского интерфейса для создания классических пользовательских интерфейсов в стиле рабочего стола.

# Импортируем некоторые модули
# Модуль QtCore
from PyQt5.QtCore import QSize, QRect
from PyQt5.QtCore import QCoreApplication, QMetaObject
# Модуль QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QLineEdit, QPlainTextEdit
from PyQt5.QtWidgets import QPushButton
# Тема приложения
from theme import DARK_THEME, LIGHT_THEME


class ChatUI(object):
    def __init__(self, _widget, _wmin, _wmax, _hmin, _hmax):
        # Определяем виджеты
        self.widget = _widget
        # Ширина приложения
        self.__WIDTH_MIN = _wmin
        self.__WIDTH_MAX = _wmax
        # Высота приложения (минимальная и максимальная)
        self.__HEIGHT_MIN = _hmin
        self.__HEIGHT_MAX = _hmax
        # Определяем параметры виджета и заголовки компонентов
        self.setupUi()
        self.retranslateUi()

    def setupUi(self):
        # Координаты и размеры главной панели
        TP_X = TP_Y = 10
        TP_WIDTH = 481
        TP_HEIGHT = 351
        # Название приложения
        self.widget.setObjectName('Chat')
        # Размер приложения
        self.widget.resize(self.__WIDTH_MIN, self.__HEIGHT_MIN)
        # Стиль приложения и виджетов
        self.widget.setStyleSheet(DARK_THEME)
        # Максимальный и минимальный размер окна
        self.widget.setMinimumSize(QSize(self.__WIDTH_MIN, self.__HEIGHT_MIN))
        self.widget.setMaximumSize(QSize(self.__WIDTH_MAX, self.__HEIGHT_MAX))

        # Главная панель вкладок приложения
        self.__tabPanel = QTabWidget(self.widget)
        self.__tabPanel.setGeometry(QRect(-4, -1, 511, 411))
        self.__tabPanel.setObjectName('__tabPanel')

        # Панель с ЧАТОМ
        self.__TChat = QWidget()
        self.__TChat.setObjectName('__TChat')

        # Виджеты для панели с ЧАТОМ
        self.__TChatWidgets = QWidget(self.__TChat)
        self.__TChatWidgets.setGeometry(QRect(TP_X, TP_Y, TP_WIDTH, TP_HEIGHT))
        self.__TChatWidgets.setObjectName('__TChatWidgets')
        # Слой с компонентами панели "ЧАТ"
        self.__LayoutFormChat = QVBoxLayout(self.__TChatWidgets)
        self.__LayoutFormChat.setObjectName('__LayoutFormChat')
        # Текстовое поле с информацией (СООБЩЕНИЯ ЧАТА)
        self.TEInfoChat = QPlainTextEdit(self.__TChatWidgets)
        self.TEInfoChat.setObjectName('TEInfoChat')
        # Текстовое поле с вводом сообщения
        self.LETextMessage = QLineEdit(self.__TChatWidgets)
        self.LETextMessage.setObjectName('LETextMessage')
        # Слой с компонентами панели "ЧАТ"
        self.__LayoutFormBtn = QHBoxLayout()
        self.__LayoutFormBtn.setObjectName('__LayoutFormBtn')
        # КНОПКА отправки сообщений
        self.PBSendMessage = QPushButton(self.__TChatWidgets)
        self.PBSendMessage.setObjectName('PBSendMessage')
        # КНОПКА подключения
        self.PBConnect = QPushButton(self.__TChatWidgets)
        self.PBConnect.setObjectName('PBConnect')
        # КНОПКА очистки поля ввода сообщений
        self.PBClearMessage = QPushButton(self.__TChatWidgets)
        self.PBClearMessage.setObjectName('PBClearMessage')

        # Панель с НАСТРОЙКАМИ
        self.__TSettings = QWidget()
        self.__TSettings.setObjectName('TSettings')

        # Виджеты для панели с НАСТРОЙКАМИ
        self.__TSettingsWidgets = QWidget(self.__TSettings)
        self.__TSettingsWidgets.setGeometry(QRect(TP_X, TP_Y, TP_WIDTH, TP_HEIGHT))
        self.__TSettingsWidgets.setObjectName('__TSettingsWidgets')
        # Слой с компонентами панели
        self.__LayoutFormSettings = QVBoxLayout(self.__TSettingsWidgets)
        self.__LayoutFormSettings.setObjectName('__LayoutFormSettings')
        # Текстовое поле с вводом адреса сервера
        self.LEAddressServer = QLineEdit(self.__TSettingsWidgets)
        self.LEAddressServer.setObjectName('LEAddressServer')
        # Текстовое поле с вводом порта сервера
        self.LEPortServer = QLineEdit(self.__TSettingsWidgets)
        self.LEPortServer.setObjectName('LEPortServer')
        # Текстовое поле с вводом порта сервера
        self.LEUserName = QLineEdit(self.__TSettingsWidgets)
        self.LEUserName.setObjectName('LEUserName')
        # КНОПКА получения данных для подключения
        self.PBDataForConnection = QPushButton(self.__TSettingsWidgets)
        self.PBDataForConnection.setObjectName('PBDataForConnection')
        # Текстовое поле с информацией (ДАННЫЕ ПО ПОДКЛЮЧЕНИЮ)
        self.TEInfoSettings = QPlainTextEdit(self.__TSettingsWidgets)
        self.TEInfoSettings.setObjectName('TEInfoSettings')

        # УПАКОВКА компонентов на слой __LayoutFormChat
        self.__LayoutFormChat.addWidget(self.TEInfoChat)
        self.__LayoutFormChat.addWidget(self.LETextMessage)
        self.__LayoutFormBtn.addWidget(self.PBSendMessage)
        self.__LayoutFormBtn.addWidget(self.PBConnect)
        self.__LayoutFormChat.addLayout(self.__LayoutFormBtn)
        self.__LayoutFormChat.addWidget(self.PBClearMessage)
        # УПАКОВКА компонентов на слой __LayoutFormSettings
        self.__LayoutFormSettings.addWidget(self.LEAddressServer)
        self.__LayoutFormSettings.addWidget(self.LEPortServer)
        self.__LayoutFormSettings.addWidget(self.LEUserName)
        self.__LayoutFormSettings.addWidget(self.PBDataForConnection)
        self.__LayoutFormSettings.addWidget(self.TEInfoSettings)
        # Видимость панели с ЧАТОМ и НАСТРОЙКАМИ (По умолчанию панель с НАСТРОЙКАМИ)
        self.__tabPanel.addTab(self.__TChat, '')
        self.__tabPanel.addTab(self.__TSettings, '')
        self.__tabPanel.setCurrentIndex(0)

        # Упаковываем компоненты виджета
        QMetaObject.connectSlotsByName(self.widget)

    def retranslateUi(self):
        caption = QCoreApplication.translate
        # Название приложения
        self.widget.setWindowTitle(caption('widget', 'Chat client-server'))
        # Названия некоторых объектов
        self.LETextMessage.setPlaceholderText(caption('widget', 'Текст сообщения...'))
        self.LEAddressServer.setPlaceholderText(caption('widget', 'Адрес сервера...'))
        self.LEUserName.setPlaceholderText(caption('widget', 'Временное имя пользователя...'))
        self.LEPortServer.setPlaceholderText(caption('widget', 'Порт сервера...'))
        self.PBSendMessage.setText(caption('widget', 'Отправить'))
        self.PBConnect.setText(caption('widget', 'Подключиться'))
        self.PBClearMessage.setText(caption('widget', 'Очистить'))
        self.PBDataForConnection.setText(caption('widget', 'Данные для подключения'))
        self.__tabPanel.setTabText(
            self.__tabPanel.indexOf(self.__TChat),
            caption('widget', 'Чат')
        )
        self.__tabPanel.setTabText(
            self.__tabPanel.indexOf(self.__TSettings),
            caption('widget', 'Настройки')
        )
