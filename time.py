import time

def countdown_timer(total_seconds):
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("Time's up!")
minutes = int(input("Enter the minutes"))
seconds = int(input("Enter the seconds"))
total_seconds = minutes * 60 + seconds
countdown_timer(total_seconds)