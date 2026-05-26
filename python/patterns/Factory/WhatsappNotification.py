from Notification import Notification


class WhatsappNotification(Notification):

    def send(self, msg: str):
        print(f"Notification from whatsapp {msg}")
