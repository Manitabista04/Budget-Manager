import time

# Countdown from 10
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)


# Intentionally throw an error
raise Exception("FAAAAAAHHHHHHH")