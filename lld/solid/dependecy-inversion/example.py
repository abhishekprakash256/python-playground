"""
example of dependency inversion, 

The details of the implementation can be changed as per service that is using it 
"""

from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def send(self, message):

        pass


class EmailService(NotificationService) :

    def send(self, message) :

        print(f"Sending the email {message}")


class SMSService(NotificationService):

    def send(self, message):

        print(f"Sending the sms {message}")


class NotificationManager():

    def __init__(self,service : NotificationService):

        self.service = service

    def notify(self, message):

        self.service.send(message)


email_notifier = NotificationManager(EmailService())
email_notifier.notify("Welcome!")

sms_notifier = NotificationManager(SMSService())
sms_notifier.notify("Code 123456")
    
