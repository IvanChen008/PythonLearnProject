'''
看完了教程，是不是有这么一种感觉：看的时候觉得很简单，照着教程敲代码也没啥大问题。

于是准备开始独立写代码，就发现不知道从哪开始下手了。

这种情况是完全正常的。好比学写作文，学的时候觉得简单，写的时候就无从下笔了。

虽然这个教程是面向小白的零基础Python教程，但是我们的目标不是学到60分，而是学到90分。

所以，用Python写一个真正的Web App吧！
'''
# 目标：
'''
==================================
我们设定的实战目标是一个Blog网站，包含日志、用户和评论3大部分。
==================================
'''
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web


def index(request):
    return web.Response(text='<h1>Index</h1>',content_type='text/html')


async def create_pool(loop,**kw):
    logging.info('create database connection pool ...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )


async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (await __pool) as connection:
        cur = await conn.cursor(aiomysql.DictCursor)
        await cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fetchall()
        await cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs

# async def init()
webApp = web.Application()
webApp.add_routes([
    web.get('/', index),
    # web.get('/hello/{name}',hello),
    # web.get('/echo',wshandle)
])
web.run_app(webApp,host='127.0.0.1',port=8000)