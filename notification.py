from notifypy import Notify
import sys

def notification():
    notif = Notify()
    notif.title = "Оповещение"
    notif.message = "Игрок зашел в игру"

    notif.send()
    sys.exit()
