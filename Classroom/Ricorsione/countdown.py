from time import sleep

# Countdown in modo iterativo
def countdown(n):
    counter = n
    while counter >= 0:
        print(counter)
        sleep(1)
        counter-=1

# Countdown in modo ricorsivo
def countdown_recursive(n):
    if n <= 0:
        print("Stop")
    else:
        print(n)
        sleep(1)
        countdown_recursive(n-1)


if __name__ == "__main__":
    countdown_recursive(10)