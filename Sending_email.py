# Ref link: https://support.google.com/mail/answer/7126229?hl=en
## https://myaccount.google.com/lesssecureapps

import smtplib 
server = smtplib.SMTP('smtp.gmail.com', 587) 
server.starttls() 
server.login("vishalhavingrum@gmail.com","System@098") 
message = "Hello from PY Code"
server.sendmail("vishalhavingrum@gmail.com","vishalonip@gmail.com",message) 
server.quit()