# # Function to convert decimal number
# # to binary using recursion
# def DecimalToBinary(num):
     
#     if num >= 1:
#         DecimalToBinary(num // 2)
#     print(num % 2, end = '')
 
# # Driver Code
# if __name__ == '__main__':
     
#     # decimal value
#     dec_val = 24
     
#     # Calling function
#     DecimalToBinary(dec_val)


# This is socket.io with python.

from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)


async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


@sio.on('message')
async def print_message(sid, message):
    print(message)

app.router.add_get('/', index)

web.run_app(app)