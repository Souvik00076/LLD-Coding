
from abc import ABC, abstractmethod
from Notification import Notification


class NotificationCreator(ABC):

    @abstractmethod
    def createNotification(self): Notification
    pass

    def send(self, msg: str):
        notification = self.createNotification()
        notification.send(msg)
