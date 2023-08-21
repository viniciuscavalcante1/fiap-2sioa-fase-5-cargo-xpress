import time

def time_pass():
    tempo = 0
    while True:
        time.sleep(1)
        print(f"20:00:{tempo}")
        tempo += 1

time_pass()