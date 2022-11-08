from string import ascii_lowercase
from time import sleep
import requests
import random
import string

def randAddress():
    return "".join(random.choice(ascii_lowercase) for _ in range(10)) + "@lasagna.email"

class LasagnaMail:
    def __init__(self):
        self.base_url = "https://lasagna.email/"
        self.session = requests.Session()

    def createAddress(self, address=randAddress()):
        self.address = address
        return self.address
    
    def getInbox(self, address=None):
        if address == None:
            address = self.address
        
        r = self.session.get(self.base_url + "api/inbox/" + address)

        return r.json()["emails"]

    def waitForEmail(self, address=None, sender=None):
        if address == None:
            address = self.address
        
        while True:
            emails = self.getInbox(address)
            if len(emails) > 0:
                if sender == None:
                    return emails
                else:
                    for email in emails:
                        if email["Sender"] == sender:
                            return email
            sleep(1)