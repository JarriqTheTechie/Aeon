import json

from application.models.Notifications import Notifications


class CreateNotificationAction:
    @classmethod
    def handle(cls, user_id: int, full_name: str, notifiable_type: str, notifiable_id: int, title: str):
        """

        :param user_id:
        :param full_name:
        :param notifiable_type:
        :param notifiable_id:
        :param title:
        :return:
        """
        Notifications.create({
            "user_id": user_id,
            "notifiable_type": notifiable_type,
            "notifiable_id": notifiable_id,
            "data": json.dumps({
                "title": title,
                "body": f"{notifiable_type} added by user {full_name}",
            })
        })

