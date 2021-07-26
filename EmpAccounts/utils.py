import random
import string
import smtplib,ssl
import socket
from datetime import datetime

def username_generator(name):
    list_name=name.partition(' ')
    firstname = list_name[0]+'@'
    randomNumber = random.sample(range(0,9),2)
    for i in range(len(randomNumber)):
        firstname+=str(randomNumber[i])
    return firstname

def password_generator():
    letters= string.ascii_letters
    randomLetter = ''.join(random.choice(letters) for i in range(4))
    randomNumbers = random.sample(range(0,9),4)
    for i in range(len(randomNumbers)):
        randomLetter +=str(randomNumbers[i])
    print(randomLetter)
    return randomLetter

def send_email(userID,password,userEmail='ptin3136'):
    port = 465  # For SSL
    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("adrednite0211@gmail.com", 'demosite1')
        message = f"Your credentials for login - username- {userID}, password- {password}"
        server.sendmail('adrednite0211@gmail.com',userEmail,message)
    

def get_ip():
    host = socket.gethostname()
    ip_ad = socket.gethostbyname(host)
    return ip_ad

def generate_id():
    randomNumbers= random.sample(range(0,9),4)
    givenID = 'DS001'
    for i in range(len(randomNumbers)):
       givenID += str(randomNumbers[i])
    return givenID

