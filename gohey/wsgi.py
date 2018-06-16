"""
WSGI config for gohey project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""


import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gohey.settings")
import importlib
import sys,django

application = get_wsgi_application()


importlib.reload(sys)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gohey.settings")  #变量gohey.settings为django项目下的settings

django.setup()     #避免在虚拟环境下找不到django的app

#application = WSGIHandler()  #实例化一个WSGI application用作接受nginx服务器传递的envrion、start_response参数

