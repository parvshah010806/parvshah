import smtplib 
from email.message import EmailMessage
connect()
email = EmailMessage() ## Creating a object for EmailMessage
email['from'] = 'parv'   ## Person who is sending
email['to'] = 'nimisha11668@gmail.com'       ## Whom we are sending
email['subject'] = 'xyz subject'  ## Subject of email
email.set_content("Xyz content of email") ## content of email
with smtplib.SMTP(host='smtp.gmail.com',port=587)as smtp:     
## sending request to server 
    
    smtp.ehlo()          ## server object
smtp.starttls()      ## used to send data between server and client
smtop.login("djdnensidoclcmxn@gmail.com","Easyfreezy@456") ## login id and password of gmail
smtp.send_message(email)   ## Sending email
print("email sent")    ## Printing success message
