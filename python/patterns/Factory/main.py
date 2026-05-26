
from NotificationCreator import NotificationCreator
from PhoneNotification import PhoneNotification
from WhatsappNotificationCreator import WhatsappNotificationCreator


def main():

    creator: NotificationCreator = WhatsappNotificationCreator()
    creator.send("hello")
    creator = PhoneNotification()
    creator.send("hello")


main()
