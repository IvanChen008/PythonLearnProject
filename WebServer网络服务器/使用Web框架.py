# 背景
'''
    了解了WSGI框架，我们发现：其实一个Web App，就是写一个WSGI的处理函数，针对每个HTTP请求进行响应。
    但是如何处理HTTP请求不是问题，问题是如何处理100个不同的URL。
    每一个URL可以对应GET和POST请求，当然还有PUT、DELETE等请求，但是我们通常只考虑最常见的GET和POST请求。
    一个最简单的想法是从environ变量里取出HTTP请求的信息，然后逐个判断。
    就目前了解的知识来说，WSGI接口虽然比HTTP接口高级了不少，但是和WebAPP的处理逻辑比，还是比较低级的，我们需要
    在WSGI接口之上能进一步抽象，让我们专注于用一个函数处理一个URL，至于URL到函数的映射，就交给Web框架来做。
    由于用Python开发Web框架十分容易，所以Python有上百个开源的Web框架。这里我们先不讨论各种Web框架的优缺点，直接
    选择一个比较流行的Web框架————Flask来使用。
'''
# Flask 框架
'''
    Flask通过Python的装饰器，在内部自动的把URL和函数给关联起来，所以，我们写出来的代码就像这样：
'''
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    # return '<h1>Home</h1>'
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_form():
    # return '''<form action="/signin" method="post">
    # <p><input name='username'></p>
    # <p><input name='password' type='password'></p>
    # <p><button type="submit">Sign in</button></p>
    # </form>'''
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
    # #需要从request对象读取表单的内容：
    # if request.form['username']=='admin' and request.form['password']=='password':
    #     return '<h3>Hello,admin!</h3>'
    # return '<h3>Bad username or password.</h3>'
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html',username=username)
    return render_template('form.html',message='Bad Username or Password',username=username)

if __name__ == '__main__':
    app.run()
# 实际上WebAPP应该拿到用户名和口令，去数据库查询对比，来判断用户是否能登录成功。
# 常用的其他框架
'''
    除了Flask，常见的Python web框架，还有：
        Django：全能型的Web框架
        web.py：一个小巧的web框架
        Bottle：和Flask类似的Web框架
        Tornado:Facebook开源异步Web框架

    有了Web框架，我们在编写Web应用时，注意力就从WSGI，处理函数转移到URL+对应的处理函数，这样，
    编写WebAPP就更加简单了。
    在编写URL处理函数时，除了配置URL外，从HTTP请求拿到用户数据也是非常重要的。Web框架都提供了
    自己的API来实现这些功能。Flask通过request.form['name']来获取表单的内容。
'''
# 使用模版
'''
    Web框架把我们从WSGI中拯救出来，现在我们只需要不停地编写函数，带上URL，就可以继续WebAPP开发了。
    但是，WebApp不仅仅是处理逻辑，展示给用户的页面也非常重要。在函数中返回一个包含HTML的字符串，简单
    的页面还可以，但是如果是复杂到几千行的HTML的代码的HTML页面，如果想在Python的字符串中正确写出来几乎
    是不可能的。
    俗话说，不懂前端的Python工程师不是好的产品经理。有Web开发经验的同学都明白，Webapp最复杂的部分就在HTML页面，
    页面不仅要求正确，还要通过CSS美化，再加上复杂的JavaScript脚本来实现各种交互和动画效果，总之，生成HTML页面的难度很大。
    由于在Python代码里拼字符串是不现实的，所以自然而然的就出现了模板技术。
    使用模板，我们需要预先准备一个HTML文档，这个文档不是普通的文档，而是嵌入了一些变量和指令，然后根据我们传入的数据，
    替换后，得到最终的HTML，然后发送给用户。
    这种就是MVC模式的用处了，中文使用的“模型-视图-控制器”。
    Python处理URL的函数就是C：controller，controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等；
    包含变量{{name}}的模版就是view，view负责显示逻辑，通过简单地一些变量，view最终输出的就是用户看到的HTML。
    MVC中的model在哪？Model就是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据。

    只是因为Python支持关键字参数，很多web框架允许传入关键字参数，然后，在框架内部组装一个dict作为model。
    现在，我们把上次直接输出字符串作为HTML的例子用高端MVC模式改写一下。

    通过MVC，我们在Python代码中处理M：model和C：controller,而V:view是通过模版处理的，这样，我们就成功地把Python代码和HTML代码
    最大限度地分离了。
    使用模板的另一个最大的好处是，模板修改起来很方便，而且改完保存后，刷新浏览器就能看到最新的效果，这对于调试
    HTML、CSS和JavaScript的前端工程师来说，实在太重要了。
'''
# 除了Jinja2常见的模版还有
'''
    Mako:用<% ... %>和${xxx}的一个模板；
    Cheetah:也是用<% ... %>和${xxx}的一个模板；
    Django:Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。

    有了MVC，我们就分离了Python代码和HTML代码全部放到模板里，写起来更有效率。
'''