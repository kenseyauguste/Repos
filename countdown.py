import time

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60) 
        timer = f"{mins:00}:{secs:00}"
        print(timer, end="\r")
        time.sleep(1)   # wait for 1 second
        seconds -= 1
    print("⏰ Time's up!")


countdown(10)