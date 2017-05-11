#-*-coding:utf8;-*-
import xadmin
from xadmin.views import ModelFormAdminView, DetailAdminView
from .widgets import SelectizeMultiplePlugin
xadmin.site.register_plugin(SelectizeMultiplePlugin, DetailAdminView)
xadmin.site.register_plugin(SelectizeMultiplePlugin, ModelFormAdminView)
