#!/usr/bin/env python
# coding: utf-8

# In[10]:


def send_mail(filename):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders

    email_user = 'debanikroy92@gmail.com'
    email_password = 'Debanik@123'
    email_send = 'debanikroy.in@gmail.com'

    subject = 'Person has been detected'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'Sir, Person has been detected by dji tello drone'
    msg.attach(MIMEText(body,'plain'))

    
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email_send,text)
    server.quit()


# In[11]:


#filename='Face_data/User.1.101.jpg'
#send_mail(filename)


# In[ ]:




