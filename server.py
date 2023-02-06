#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep as time_sleep
import socket
import base64
import threading


class Server:
    def __init__(self, _ip, _port):
        # IP клиента (запуск прослушивания по порту)
        self.__ip = _ip
        # Порт
        self.__port = _port
        # Список клиентов
        self.__clients = []

        # socket -Программный интерфейс для обеспечения инфо. обмена между процессами
        # AF_INET -Используется для семейства адресов
        # SOCK_STREAM -Объект сокета с указанием типа TCP-сокета (для управления передачей данных интернета)
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Прослушивание определённого IP порта
        self.__server.bind((self.__ip, self.__port))
        # Одновременное прослушивание сервером кол-ва человек
        self.__server.listen(10)

        # Запуск потока для отслеживания новых подключений
        threading.Thread(target=self.connection_handler).start()
        print('Server запущен!')

    def connection_handler(self):
        while True:
            # Принимаем подключение от сервера (клиентский сокет и адрес)
            client, address = self.__server.accept()
            # Если клиента нет в списке клиентов
            if client not in self.__clients:
                self.__clients.append(client)
                # Запуск потока для отслеживания новых сообщений
                threading.Thread(target=self.message_handler, args=(client,)).start()
                client.send('Успешное подключение!'.encode('utf-8'))
            # Тайм-аут на 100 млс
            time_sleep(100)

    def message_handler(self, socket_client):
        while True:
            # Принимаем данные от клиента (пакет не больше 1024Байт)
            message = socket_client.recv(1024)

            # ------------------------- #
            print(message)
            # ------------------------- #

            # Если клиент написал 'exit', то удаление тек. сокета
            if message == 'exit':
                self.__clients.remove(socket_client)
                break
            # Чтобы не отправить сообщение самому себе
            for client in self.__clients:
                if client != socket_client:
                    # Отправляем сообщение каждому клиенту
                    client.send(message)
            # Тайм-аут на 100 млс
            time_sleep(100)


Server('127.0.0.1', 4444)
