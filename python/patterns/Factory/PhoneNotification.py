from Notification import Notification


class PhoneNotification(Notification):

    def send(self, msg: str):
        print(f"Notification from phone {msg}")
