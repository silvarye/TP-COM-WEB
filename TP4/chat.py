import websockets
import asyncio
import html


async def communication_handler(websocket, path):
    name = await websocket.recv()
    global clients
    clients.add(websocket)
    for client in clients:
        await client.send("{} à rejoint la conversation.".format(name))
    while True:
        try:
            message = await websocket.recv()
            message = html.escape(message)
            messageTosend = "<b>{}:</b> {}".format(name, message)
            for client in clients:
                await client.send(messageTosend)
        except:
            clients.remove(websocket)


if __name__ == "__main__":
    clients = set()
    server = websockets.serve(communication_handler, 'localhost', 12345)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
