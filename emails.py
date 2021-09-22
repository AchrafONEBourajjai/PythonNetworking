import email.message,email.policy,email.utils,sys
text = """ Hi My name is python """
message = email.message.EmailMessage(email.policy.SMTP)
message['To'] = "achraf.bourajjai97@gmail.com"
message['From'] = 'Test message <achraf.bourajjai97@gmail.com>'
message['subject'] = "This is test"
message['Date'] = email.utils.formatdate(localtime=True)
message['message-id'] = email.utils.make_msgid()
message.set_content(text)
sys.stdout.buffer.write(message.as_bytes())
