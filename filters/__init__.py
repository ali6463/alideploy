from aiogram import Dispatcher

from . import admin
from . import guruh
from .guruh import IsPrivate
from .admin import AdminFilter

if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    pass