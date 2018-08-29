# Dependencies 依赖项
'''
    Werkzeug implements WSGI, the standard Python interface between applications and servers.
    # Python 的应用和服务器之间的标准接口
    Jinja is a template language that renders the pages your application serves.
    # 渲染应用服务的页面的模版语言
    MarkupSafe comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.
    # 来自Jinja，在呈现模板时，它会转义不可信的输入，以避免注入攻击。
    ItsDangerous securely signs data to ensure its integrity. This is used to protect Flask’s session cookie.
    # 用来保护Flask的会话cookie
    Click is a framework for writing command line applications. It provides the flask command and allows adding custom management commands.
    # 用来写命令行应用的，提供Flask命令并可以添加通用的管理命令。

'''
# Optional dependencies
'''
Optional dependencies

These distributions will not be installed automatically. Flask will detect and use them if you install them.

    Blinker provides support for Signals.
    # 提供Signals支持
    SimpleJSON is a fast JSON implementation that is compatible with Python’s json module. It is preferred for JSON operations if it is installed.
    # 一个与Python json 模块兼容的快速的Json实现，如果安装了，将会优先的执行json操作。
    python-dotenv enables support for Environment Variables From dotenv when running flask commands.
    # 运行flask 命令时启用来自dotenv的环境变量支持
    Watchdog provides a faster, more efficient reloader for the development server.
    # 为开发服务器提供一个更快,更有效的reloader

'''
# Variables Rules 变量规则
'''
Variable Rules

    You can add variable sections to a URL by marking sections with <variable_name>. 
    Your function then receives the <variable_name> as a keyword argument.
    Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.
    ==========================================
    string 	(default) accepts any text without a slash
    int 	accepts positive integers
    float 	accepts positive floating point values
    path 	like string but also accepts slashes
    uuid 	accepts UUID strings
'''
# Flask 程序的
'''
    所有Flask程序都必须创建一个 程序实例 。Web服务器使用一种名为Web服务器网管接口（WSGI）的协议,把接受自客户端的所有请求
    转交给这个对象处理。程序实例是Flask类的对象。Flask类的构造函数只有一个必须指定的参数，即程序主模块或包的名字。将构造
    函数的name参数传给Flask程序，这一点可能会让Flask开发新手心生迷惑。Flask用这个参数决定程序的根目录，以便稍后能够找到
    相对于程序根目录的资源文件位置。
'''
