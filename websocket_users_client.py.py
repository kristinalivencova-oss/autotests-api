import asyncio
from http.client import responses

import websockets


async def client():
    uri = "ws://localhost:8765"  # Адрес сервера
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"  # Сообщение, которое отправит клиент
        print(f"Отправка: {message}")
        await websocket.send(message)  # Отправляем сообщение

        for i in range(5):
            response = await websocket.recv()
            print(response)


asyncio.run(client())

async def client():
    uri = "ws://localhost:8765"  # Адрес WebSocket-сервера
    async with websockets.connect(uri) as websocket:  # Устанавливаем соединение с сервером
        message = "Привет, сервер!"  # Сообщение, которое отправит клиент
        print(f"Отправка: {message}")
        await websocket.send(message)  # Асинхронно отправляем сообщение серверу
