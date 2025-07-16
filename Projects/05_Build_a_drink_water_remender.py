# Drink water reminder

import time

from plyer import notification
while True :
    print("Please sip some water")
    notification.notify(title = "Please drink some water ",
                        message = "you need to drink")
    time.sleep(3600)

