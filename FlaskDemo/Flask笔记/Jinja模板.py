# Jinja设置
'''
    Flask中，Jinja的默认配置如下：
        当使用render_template()时，扩展名为 .html 、 .htm 、 .xml 和 .xhtml的模板中开启自动转义。
        当使用render_template_string()时，字符串开启自动转义。
        在模板中可以使用｛% autoescape %｝来手动设置是否转义。
        Flask在Jinja2环境中加入一些全局函数和辅助对象，以增强模板功能。
'''
# 标准环境
'''
    可以在Jinja2的模板中的使用的全局变量：
    config:当前配置对象，
    request：当前请求对象，
    session：当前会话对象，
    g：请求绑定的全局变量，
    url_for()函数，
    get_flashed_messages()函数

'''