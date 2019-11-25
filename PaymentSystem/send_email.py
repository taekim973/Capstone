import smtplib

server = smtplib.SMTP('smtp.outlook.com', 587)
message = "ebill is ready"
server.ehlo()
server.starttls()
server.login("mahnamnauman@hotmail.com", "bayview<33")
server.sendmail("mahnamnauman@hotmail.com", "bratzmahi@gmail.com", message)
server.close()
