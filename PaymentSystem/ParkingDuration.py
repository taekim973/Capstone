import time


# modify later to start when license plate is read and car enters
start = input("press enter to start the timer ")
print("The timer has started")

#timer has started
begin = time.time()

# press enter to end time (in this case)
# going forward this will be modified and the timer will stop when the car
# leaves the parking lot and the license plate is read once again

endtimer = input("press enter to stop timer ")

end = time.time()

# calculation of the time elasped
elapsed = end - begin

hours, rem = divmod(elapsed, 3600)

minutes, seconds = divmod(rem, 60)

print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))


    
