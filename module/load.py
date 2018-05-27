# coding:utf-8
from __future__ import unicode_literals
from __future__ import print_function
import os
import imp


def load_module():
    modules = []
    if not os.path.exists("plugins"):
        os.makedirs("plugins")
    for plugin in os.listdir('plugins/'):
        plugin = plugin.split('.')
        print("[+++] 加载模块",plugin[0])
        if plugin[-1] != 'py':
            continue
        try:
            module = imp.new_module('.'.join(plugin[:-1]))
            exec open('plugins/' + '.'.join(plugin)).read() in module.__dict__
            modules.append(module)
        except Exception, e:
            print (e)
    return modules


def work(modules, func_name, params):
    for module in modules:
        func = getattr(module, func_name, None)
        if func:
            try:
                func(*params)
            except:
                pass
