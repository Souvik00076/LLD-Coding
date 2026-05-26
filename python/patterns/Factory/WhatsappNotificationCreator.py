

from NotificationCreator import NotificationCreator
from WhatsappNotification import WhatsappNotification


class WhatsappNotificationCreator(NotificationCreator):
    def createNotification(self):
        return WhatsappNotification()
