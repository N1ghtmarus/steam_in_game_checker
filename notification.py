from notifypy import Notify
import sys

def notification():
    notif = Notify()
    notif.title = "Notification"
    notif.message = "The player entered in the game"

    notif.send()
    sys.exit()
