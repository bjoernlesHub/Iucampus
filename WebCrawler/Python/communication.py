def send_mail(text_given, subject, mail_is_from="bjoernle@gmx.net", mail_goes_to="bjoernle@gmx.net", mail_host="", mail_port=465, mail_pass=""):
    #! /usr/bin/python
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    # me == my email address
    # you == recipient's email address
    me = mail_is_from
    you = mail_goes_to
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = you
    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """\
    <html>
      <head></head>
      <body>
    """+text_given+"""
      </body>
    </html>
    """
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    s = smtplib.SMTP_SSL(mail_host, mail_port)
    s.set_debuglevel(1)
    s.ehlo
    # Send user authentication information
    s.login(mail_is_from, mail_pass)
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(me, you, msg.as_string())
    s.quit()
	
def send_mail1(text, subject, mail_is_from="bjoernle@gmx.net", mail_goes_to="bjoernle@gmx.net", mail_host="", mail_port=465, mail_pass=""):
    import smtplib
    from email.message import EmailMessage
	
    import globals
    
    settings_json=globals.get_settings_json

    from_addr = mail_is_from
    to_addrs  = mail_goes_to
    smtp_host = mail_host
    smtp_port = mail_port
    mail_pass = mail_pass

    msg = EmailMessage()
    msg.set_content(text)

    msg['Subject'] = subject
    msg['From'] = mail_is_from
    msg['To'] = mail_goes_to

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL(smtp_host, smtp_port)
    server.login(mail_is_from, "GeEmIksPwd18")
    server.send_message(msg)
    server.quit()

def get_skype_recent_contacts(username, password):
    from skpy import Skype
    import os

    sk = Skype(username, password)
    print(sk.chats.recent())
    #for chat in sk.chats.recent():
        #chat.
    
def send_skype_message(username, password, to_person, content_string="", file_path=""):
    from skpy import Skype
    import os

    sk = Skype(username, password) # connect to Skypesk.user # you
    sk.contacts # your contacts
    sk.chats # your conversationsch = sk.chats.create(["joe.4", "daisy.5"]) # new group conversation
    ch = sk.contacts[to_person].chat # 1-to-1 conversationch.sendMsg(content) # plain-text message
    if file_path!="":
        file=os.path.basename(file_path)
        ch.sendFile(open(file_path, "rb"), file) # file upload
    #ch.sendContact(sk.contacts["daisy.5"]) # contact sharingch.getMsgs() # retrieve recent messages
    if content_string!="":
        ch.sendMsg(content_string)
        
def send_to_skype_group(username, password, channel_id, content_string="", file_path=""): 
    from skpy import Skype

    sk = Skype(username,password) 
    ch = sk.chats.chat(channel_id) 
    if file_path!="":
        file=os.path.basename(file_path)
        ch.sendFile(open(file_path, "rb"), file) # file upload
    #ch.sendContact(sk.contacts["daisy.5"]) # contact sharingch.getMsgs() # retrieve recent messages
    if content_string!="":
        ch.sendMsg(content_string)