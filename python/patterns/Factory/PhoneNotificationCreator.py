

from NotificationCreator import NotificationCreator
from PhoneNotification import PhoneNotification


class PhoneNotificationCreator(NotificationCreator):
    def createNotification(self):
        return PhoneNotification()
