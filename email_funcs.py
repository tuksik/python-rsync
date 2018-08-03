# Author chomes@github
# E-mail function script V1.0
# Importing functions
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser


# Separate functions created for sending emails to make it more modular and to allow multiple functions to re-use it.
def send_mail_unsecure(username, passwd, from_addr, to_addr, port, smtp_server, email_msg):
    server = smtplib.SMTP(smtp_server, port)
    server.login(username, passwd)
    server.sendmail(from_addr, to_addr, email_msg)
    server.quit()


def send_mail_unsecure_no_auth(from_addr, to_addr, port, smtp_server, email_msg):
    server = smtplib.SMTP(smtp_server, port)
    server.sendmail(from_addr, to_addr, email_msg)
    server.quit()


def send_mail_secure(username, passwd, from_addr, to_addr, ssl_tls, port, smtp_server, email_msg):
    if ssl_tls == "ssl":
        server = smtplib.SMTP_SSL(smtp_server, port)
    else:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
    server.login(username, passwd)
    server.sendmail(from_addr, to_addr, email_msg)
    server.quit()


def send_mail_secure_no_auth(from_addr, to_addr, ssl_tls, port, smtp_server, email_msg):
    if ssl_tls == "ssl":
        server = smtplib.SMTP_SSL(smtp_server, port)
    else:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
    server.sendmail(from_addr, to_addr, email_msg)
    server.quit()


# Function for sending email for starting backup
def backup_start():
    config = configparser.ConfigParser()
    config.read('email_config.ini')
    # Begin importing variables
    username = config.get("server_details", "username")
    passwd = config.get("server_details", "password")
    from_addr = config.get("server_details", "from_addr")
    to_addr = config.get("server_details", "to_addr")
    port = config.get("server_details", "port")
    smtp_server = config.get("server_details", "server")
    ssl_tls = config.get("server_details", "ssl_tls")
    # If value doesn't exit for port, default to 25 for sending mail
    if not port:
        port = 25
    # Converting port into an integer otherwise it would just be a value
    port = int(port)
    # Creating multipart message to send
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = "Backup commencing"
    body = "The backup is now taking place, we will send you a notification once it's done"
    msg.attach(MIMEText(body, 'plain'))
    email_msg = msg.as_string()
    # If statement based on config file conditions will send email secure/unsecure with/without auth
    if config.get("server_details", "auth") == "no":
        if config.get("server_details", "secure") == "no":
            send_mail_unsecure_no_auth(from_addr, to_addr, port, smtp_server, email_msg)
        else:
            send_mail_secure_no_auth(from_addr, to_addr, ssl_tls, port, smtp_server, email_msg)
    else:
        if config.get("server_details", "secure") == "no":
            send_mail_unsecure(username, passwd, from_addr, to_addr, port, smtp_server, email_msg)
        else:
            send_mail_secure(username, passwd, from_addr, to_addr, ssl_tls, port, smtp_server, email_msg)


# Function for sending email for completion
def backup_completed():
    config = configparser.ConfigParser()
    config.read('email_config.ini')
    # Importing variables
    username = config.get("server_details", "username")
    passwd = config.get("server_details", "password")
    from_addr = config.get("server_details", "from_addr")
    to_addr = config.get("server_details", "to_addr")
    port = config.get("server_details", "port")
    smtp_server = config.get("server_details", "server")
    ssl_tls = config.get("server_details", "ssl_tls")
    # If value doesn't exit for port, default to 25 for sending mail
    if not port:
        port = 25
    # Converting port into an integer otherwise it would just be a value
    port = int(port)
    # Creating multipart message to send
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = "Backup is complete"
    body = "The backup is now done, the logs are on the server in the folder of the script"
    msg.attach(MIMEText(body, 'plain'))
    email_msg = msg.as_string()
    # If statement based on config file conditions will send email secure/unsecure with/without auth
    if config.get("server_details", "auth") == "no":
        if config.get("server_details", "secure") == "no":
            send_mail_unsecure_no_auth(from_addr, to_addr, port, smtp_server, email_msg)
        else:
            send_mail_secure_no_auth(from_addr, to_addr, ssl_tls, port, smtp_server, email_msg)
    else:
        if config.get("server_details", "secure") == "no":
            send_mail_unsecure(username, passwd, from_addr, to_addr, port, smtp_server, email_msg)
        else:
            send_mail_secure(username, passwd, from_addr, to_addr, ssl_tls, port, smtp_server, email_msg)


# Function for sending email for work in progress
def backup_in_progress():
    config = configparser.ConfigParser()
    config.read('email_config.ini')
    # Importing variables
    username = config.get("server_details", "username")
    passwd = config.get("server_details", "password")
    from_addr = config.get("server_details", "from_addr")
    to_addr = config.get("server_details", "to_addr")
    port = config.get("server_details", "port")
    smtp_server = config.get("server_details", "server")
    ssl_tls = config.get("server_details", "ssl_tls")
    # If value doesn't exit for port, default to 25 for sending mail
    if not port:
        port = 25
    # Converting port into an integer otherwise it would just be a value
    port = int(port)
    # Creating multipart message to send
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = "Backup is in progress"
    body = "The backup is in progress, please wait for completion before continuing"
    msg.attach(MIMEText(body, 'plain'))
    email_msg = msg.as_string()
    # If statement based on config file conditions will send email secure/unsecure with/without auth
    if config.get("server_details", "auth") == "no":
        if config.get("server_details", "secure") == "no":
            send_mail_unsecure_no_auth(from_addr, to_addr, port, smtp_server, email_msg)
        else:
            send_mail_secure_no_auth(from_addr, to_addr, ssl_tls, port, smtp_server, email_msg)
    else:
        if config.get("server_details", "secure") == "no":
            send_mail_unsecure(username, passwd, from_addr, to_addr, port, smtp_server, email_msg)
        else:
            send_mail_secure(username, passwd, from_addr, to_addr, ssl_tls, port, smtp_server, email_msg)