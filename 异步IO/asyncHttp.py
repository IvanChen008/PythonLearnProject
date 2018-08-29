import asyncio
from aiohttp import web


async def index(request):
    await asyncio.sleep(0.5)
    # return web.Response(body=b'<h1>Index</h1>',content_type='text/html')
    # return web.Response(body='<h1>Index</h1>',content_type='text/html')
    # return web.Response(body='<h1>Index</h1>')
    return web.Response(text='<h1>Index</h1>',content_type='text/html')


async def hello(request):
    await asyncio.sleep(0.2)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    # return web.Response(body=text.encode('utf-8'),content_type='text/html')
    # return web.Response(text=text,content_type='text/html')
    return web.Response(text=text)


# async def init(loop):
#     aapp = web.Application(loop=loop)
#     aapp.router.add_route('GET','/',index)
#     aapp.router.add_route('GET','/hello/{name}',hello)
#     srv = await loop.create_server(aapp.make_handler(),'127.0.0.1',8000)
#     print('Server started at http://127.0.0.1:8000...')
#     return srv
async def wshandle(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.text:
            await ws.send_str('Hello,{}'.format(msg.data))
        elif msg.type == web.WSMsgType.binary:
            await ws.send_bytes(msg.data)
        elif msg.type == web.WSMsgType.close:
            break
            
    return ws

# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()

app = web.Application()
app.add_routes([
    web.get('/', index),
    web.get('/hello/{name}',hello),
    web.get('/echo',wshandle)
])
web.run_app(app,host='127.0.0.1',port=8080)


'''
    asyncio可以实现单线程并发IO操作。如果仅用在客户端，发挥的威力不大。如果把asyncio用在服务器端，例如Web服务器，由于http
    连接就是IO操作，因此可以用单线程+coroutine实现多用户的高并发支持。
    asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的http框架。
'''