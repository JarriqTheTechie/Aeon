""" Notifications Model """

from masoniteorm.models import Model


class Notifications(Model):
    """Notifications Model"""
    __casts__ = {"data": "json"}

    pass
