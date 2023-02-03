from aiohttp import web
import socketio
import os


socket = socketio.AsyncServer()
app = web.Application()
socket.attach(app)

async def webapp(request):
   with open("index.html") as w:
    return web.Response(text=w.read(), content_type='text/html')


@socket.on("message")
async def connected(id, message):
    os.path.basename(message.filename)
@socket.on("sending")
def sending(id, message):
    print(message)

app.router.add_get("/", webapp)
web.run_app(app)