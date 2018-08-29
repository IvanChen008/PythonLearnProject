'''
    asyncio 是python3.4版本引入的标准库，直接内置了对异步IO的支持。asyncio的编程模型就是一个消息循环。我们从asyncio模块中
    直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
    用asyncio实现一下hello world：
'''
# ===================================
# import asyncio

# @asyncio.coroutine
# def hello():
#     print('Hello world!')
#     # 异步调用asyncio.sleep(1)
#     r = yield from asyncio.sleep(1)
#     print('Hello again!')

# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()
# ===================================
# 执行结果：
# 2018年8月20日 11:02:09
# ==========================
# D:\GitHub\PythonLearnProject\异步IO>python asyncios.py
# Hello world!
# Hello again!
# ==========================
'''
    @asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。hello()会首先
    打印出Hello world！，然后，yield from 语法可以让我们方便的调用另一个generator。由于asyncio.sleep()也是一个coroutine，
    所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，线程就可以从yield from拿到
    返回值（此处是None），然后执行下一行语句。把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去
    执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
'''
# 我们用Task封装两个coroutine
# ===================================
# import threading
# import asyncio

# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())

# loop = asyncio.get_event_loop()
# tasks = [hello(),hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
# ===================================
# 执行结果：
# 2018年8月20日 11:09:55
# ========================
# D:\GitHub\PythonLearnProject\异步IO>python asyncios.py
# Hello world! (<_MainThread(MainThread, started 7104)>)
# Hello world! (<_MainThread(MainThread, started 7104)>)
# Hello again! (<_MainThread(MainThread, started 7104)>)
# Hello again! (<_MainThread(MainThread, started 7104)>)
# ========================
'''
    由打印出的当前线程的名称可以看出，两个coroutine是由同一个线程并发执行的。如果把asyncio.sleep()换成正真的IO操作，则多个
    coroutine就可以由一个线程并发执行。我们用asyncio的异步网络连接来获取一些网站的首页：
'''
# =====================================
# import asyncio

# @asyncio.coroutine
# def wget(host):
#     print('wget %s' % host)
#     connect = asyncio.open_connection(host,80)
#     reader,writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host,line.decode('utf-8').rstrip()))
#     writer.close()

# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn','www.sohu.com','www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
# =====================================
# 输出结果：
# 2018年8月20日 11:22:37
# ========================
# D:\GitHub\PythonLearnProject\异步IO>python asyncios.py
# wget www.sohu.com
# wget www.sina.com.cn
# wget www.163.com
# www.sina.com.cn header > HTTP/1.1 302 Moved Temporarily
# www.sina.com.cn header > Server: nginx
# www.sina.com.cn header > Date: Mon, 20 Aug 2018 03:21:52 GMT
# www.sina.com.cn header > Content-Type: text/html
# www.sina.com.cn header > Content-Length: 154
# www.sina.com.cn header > Connection: close
# www.sina.com.cn header > Location: https://www.sina.com.cn/
# www.sina.com.cn header > X-Via-CDN: f=edge,s=ctc.chengdu.ha2ts4.26.nb.sinaedge.com,c=182.138.101.45;
# www.sina.com.cn header > X-Via-Edge: 15347353123702d658ab63850d3de3f099492
# www.163.com header > HTTP/1.0 302 Moved Temporarily
# www.163.com header > Server: Cdn Cache Server V2.0
# www.163.com header > Date: Mon, 20 Aug 2018 03:21:52 GMT
# www.163.com header > Content-Length: 0
# www.163.com header > Location: http://www.163.com/special/0077jt/error_isp.html
# www.163.com header > Connection: close
# www.sohu.com header > HTTP/1.1 200 OK
# www.sohu.com header > Content-Type: text/html;charset=UTF-8
# www.sohu.com header > Connection: close
# www.sohu.com header > Server: nginx
# www.sohu.com header > Date: Mon, 20 Aug 2018 03:21:36 GMT
# www.sohu.com header > Cache-Control: max-age=60
# www.sohu.com header > X-From-Sohu: X-SRC-Cached
# www.sohu.com header > Content-Encoding: gzip
# www.sohu.com header > FSS-Cache: HIT from 3890028.5725046.5284232
# www.sohu.com header > FSS-Proxy: Powered by 2972510.3890024.4366700
# ========================
'''
    可见3个连接由一个线程通过coroutine并发完成。asyncio提供了完善的异步IO支持；异步操作需要在coroutine中通过yield from
    完成；多个coroutine可以封装成一组Task然后并发完成。
'''
# async/await
'''
    用asyncio提供的@asyncio.coroutine可以把一个generator标记成一个coroutine类型，然后在coroutine内部用yield from 调用
    另一个coroutine实现异步操作。为了简化并更好的标识异步IO，从Python3.5开始引入新的语法async和await，可以让coroutine的
    代码更简介易读。
    注意：async和await是针对coroutine的新语法，要使用新的语法只需要做两步简单的替换：
        1、把@asyncio.coroutine替换成async；
        2、把yield from 替换为await
'''
# =====================================
import asyncio

async def wget(host):
    print('wget %s' % host)
    connect = asyncio.open_connection(host,80)
    reader,writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host,line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn','www.sohu.com','www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
# =====================================