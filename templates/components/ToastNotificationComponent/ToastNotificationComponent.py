""" ToastNotificationComponent Component """
from flask import session

from application.models.Notifications import Notifications


class ToastNotificationComponent:
    def __init__(self):
        self.notification = Notifications
        #self.notification.update({"read": "yes"})
