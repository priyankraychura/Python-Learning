from win10toast import ToastNotifier
import time

toast = ToastNotifier()

REPET_INTERVAL = 3600 #Reminer in every one hour

def remind():
    toast.show_toast(
        "Drink Water",
        "For the good health in this summer frink water is very much important",
        duration = 2,
        icon_path = "./drink.ico",
        threaded = True,
    )

while True:
    remind()
    time.sleep(REPET_INTERVAL)