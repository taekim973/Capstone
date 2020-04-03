import smtplib
import time

def timer():
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

                price(hours, minutes, seconds)

                return;
                
#this method calculates the price of the parking duration
def price(hrs, mins, secs):

                seconds_hours = secs / 3600
                minutes_hours = mins / 60

                rate = 8 # predetermined rate

                total = hrs + seconds_hours + minutes_hours

                cost = rate*total

                rounded = round(cost, 2) #rounding to the nearest two decimal places

                price = '${}'.format(rounded)
                
                print (price)

                sendbill(price)

                return;

def sendbill(price):
                server = smtplib.SMTP('smtp.outlook.com', 587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login("mahnamnauman@hotmail.com", "Bayview!1")
                subject='Thank You for using AGPLS'
                content="Your e-bill is ready: %s" % price
                mailtext='Subject:'+subject+'\n\n'+content
                server.sendmail("mahnamnauman@hotmail.com", "bratzmahi@gmail.com", mailtext)
                server.close()

def main():
                timer()

if __name__ == "__main__":

                main()
