# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login("surajp9999999@gmail.com", "88406439wp") 

listOf = ["surajprajapati0325@gmail.com"]
# message to be sent 
message = "Message_you_need_to_send"

# sending the mail 
s.sendmail("surajp9999999@gmail.com", listOf, message) 

# terminating the session 
s.quit() 
