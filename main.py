import time
import winsound
from plyer import notification
from win10toast import ToastNotifier


def timer(reminder, seconds):

    notificator = ToastNotifier()

    notificator.show_toast("Reminder\u23f1", "\u23F0Alarm will go off in seconds!!!!",  duration = 5)

    notificator.show_toast("Break Reminder\u231B", "****Your 'BREAK' is going to be 'START'*****", duration = 5)


timer("Break Reminder", 5)


for i in range(1, 10):
    
    if __name__ == "__main__":

        notification.notify(
            title = "****PLEASE TAKE A BREAK!!!!\u2615",

            message = "“Do something nice for yourself \U0001F603 today. Find some quiet area, sit in stillness, breathe. Put your problems on pause\u23F8. You deserve a break.\U0001F607”",

            app_icon = "icon1.ico",

            # displaying time
            timeout = 0.5,

            toast = False
        )

        # waiting time
        time.sleep(2)

        #alarm
        winsound.MessageBeep()
