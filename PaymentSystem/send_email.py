import smtplib

server = smtplib.SMTP('smtp.outlook.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("mahnamnauman@hotmail.com", "bayview<33")

subject='Thank You for using AGPLS'
content="Your e-bill is ready"
mailtext='Subject:'+subject+'\n\n'+content





server.sendmail("mahnamnauman@hotmail.com", "bratzmahi@gmail.com", mailtext)
server.close()
